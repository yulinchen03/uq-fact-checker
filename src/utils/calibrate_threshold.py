import json
import os
import sys
import random
from transformers import set_seed
import numpy as np
import torch
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score
from pathlib import Path
import hydra
from omegaconf import DictConfig

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

def lock_random_seeds(seed: int = 42):
    """Locks all random number generators for deterministic pipeline execution."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    set_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def clean_label(label: str) -> str:
    lbl = str(label).upper().replace(".", "").replace("_", " ")
    return " ".join(lbl.split())


def load_and_clean_calibration_data(file_path, dataset_name, uq_method):
    """Parses JSONL logs, strictly filters invalid labels, and extracts arrays for a specific uq_method."""
    print(f"Loading {uq_method} calibration data from: {file_path}")
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    if not data:
        return None, None, None, 0

    allowed_labels = ["TRUE", "FALSE", "CONFLICTING"] if dataset_name.lower() == "quantemp" else ["SUPPORT", "CONTRADICT", "NOT ENOUGH INFO"]

    raw_scores, y_true_list, y_para_list = [], [], []
    excluded_count = 0

    for d in data:
        uq_scores = d.get('uq_scores', {})
        score = uq_scores.get(uq_method)
        score = np.inf if score is None or np.isnan(score) else score
            
        gold = clean_label(d.get('gold_label', 'NOT ENOUGH INFO'))
        para = clean_label(d.get('parametric_verdict', 'NOT ENOUGH INFO'))

        # require a valid parametric verdict
        if para not in allowed_labels:
            excluded_count += 1
            continue

        raw_scores.append(score)
        y_true_list.append(gold)
        y_para_list.append(para)

    return np.array(raw_scores), np.array(y_true_list), np.array(y_para_list), excluded_count

def calculate_guaranteed_risk_bound(m_accepted: int, k_errors: int, delta_confidence: float = 0.01) -> float:
    if m_accepted == 0:
        return 1.0
    return float(stats.beta.ppf(1 - delta_confidence, k_errors + 1, m_accepted - k_errors))


def plot_calibration_curves(fpr, tpr, auroc, best_fpr, best_tpr,
                            coverages, risks, best_coverage, best_risk,
                            optimal_threshold, dataset_name, uq_method, save_dir,
                            output_format, check_logic, logic_eval_method):
    """
    Generates a side-by-side visualization of the ROC curve and Risk-Coverage curve.
    Now includes ablation config in titles and separates filenames.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Descriptive Super Title
    trap_str = f"ON ({logic_eval_method})" if check_logic else "OFF"
    config_desc = f"Format: {output_format} | Logic Check: {trap_str}"
    fig.suptitle(f"Calibration Analysis: {uq_method} ({dataset_name.capitalize()})\n[{config_desc}]", 
                 fontsize=14, fontweight='bold', y=1.05)

    # Panel 1: ROC Curve
    ax1.plot(fpr, tpr, color='#2563eb', linewidth=2, label=f'{uq_method} (AUROC: {auroc:.4f})')
    ax1.plot([0, 1], [0, 1], 'k--', alpha=0.4, label='Random Chance')
    ax1.scatter([best_fpr], [best_tpr], color='red', s=80, zorder=5,
               label=f"Youden's J (t={optimal_threshold:.3f})")
    ax1.set_title('ROC Curve')
    ax1.set_xlabel('False Positive Rate (1 - Specificity)')
    ax1.set_ylabel('True Positive Rate (Sensitivity)')
    ax1.legend(loc='lower right')
    ax1.grid(True, linestyle='--', alpha=0.4)
    ax1.set_xlim([-0.02, 1.02])
    ax1.set_ylim([-0.02, 1.02])

    # Panel 2: Risk-Coverage Curve
    sorted_idx = np.argsort(coverages)
    sorted_cov = coverages[sorted_idx]
    sorted_risk = risks[sorted_idx]

    ax2.plot(sorted_cov, sorted_risk, color='#2563eb', linewidth=2, label=f'{uq_method}')
    ax2.fill_between(sorted_cov, sorted_risk, color='#2563eb', alpha=0.08)
    ax2.scatter([best_coverage], [best_risk], color='red', s=80, zorder=5,
               label=f'Operating Point (C={best_coverage:.2f}, R={best_risk:.3f})')
    ax2.set_title('Risk-Coverage Curve')
    ax2.set_xlabel('Coverage (Fraction handled parametrically)')
    ax2.set_ylabel('Risk (Error rate on covered claims)')
    ax2.legend(loc='upper left')
    ax2.grid(True, linestyle='--', alpha=0.4)

    plt.tight_layout()
    
    # Dynamic filename based on config
    logic_suffix = f"_logic_{logic_eval_method}" if check_logic else "_logic_OFF"
    filename = f"calibration_curves_{output_format}{logic_suffix}.png"
    plot_path = Path(save_dir) / filename
    
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"\n📈 Calibration curves saved to: {plot_path.relative_to(ROOT_DIR)}")


# Threshold Sweep Calibration

def sweep_threshold(file_path, dataset_name, uq_method, save_dir=None, output_format="label_only", check_logic=False, logic_eval_method="discrete"):
    """
    Mode-agnostic calibration using the AUROC-optimal operating point (Youden's J statistic).
    """
    from sklearn.metrics import roc_curve, roc_auc_score

    scores, y_true, y_para, excluded_count = load_and_clean_calibration_data(file_path, dataset_name, uq_method)
    if scores is None:
        print("Error: No data found in file.")
        return None, None, None, None, None, None, None, None, None

    print(f"\n--- Data Filtering ---")
    print(f"Total Evaluated Claims: {len(scores) + excluded_count}")
    print(f"Valid Claims Retained:  {len(scores)}")
    print(f"Excluded Claims:        {excluded_count} (Invalid label output)")

    # Filter out infinite scores
    finite_mask = np.isfinite(scores)
    finite_scores = scores[finite_mask]
    finite_true = y_true[finite_mask]
    finite_para = y_para[finite_mask]

    if len(finite_scores) == 0:
        print("Error: No valid uncertainty scores found.")
        return None, None, None, None, None, None, None, None, None

    # Binary error labels: 1 = parametric was wrong, 0 = parametric was correct
    errors = (finite_para != finite_true).astype(int)

    # Need both classes present for AUROC
    if len(set(errors)) < 2:
        print("Error: All predictions are either correct or incorrect. Cannot compute AUROC-optimal threshold.")
        return None, None, None, None, None, None, None, None, None

    # Compute ROC curve
    fpr, tpr, thresholds = roc_curve(errors, finite_scores)
    auroc = roc_auc_score(errors, finite_scores)

    # Youden's J = TPR + (1 - FPR) - 1 = TPR - FPR
    j_scores = tpr - fpr
    best_idx = np.argmax(j_scores)

    optimal_threshold = float(thresholds[best_idx])
    best_sensitivity = float(tpr[best_idx])        # TPR: correctly flagging errors
    best_specificity = float(1 - fpr[best_idx])    # TNR: correctly preserving correct preds
    best_j = float(j_scores[best_idx])

    # Calculate coverage and empirical risk at this threshold
    covered_mask = finite_scores < optimal_threshold
    coverage = float(np.mean(covered_mask))
    risk = float(np.mean(errors[covered_mask])) if coverage > 0 else 0.0

    # Guaranteed risk bound (Lemma 3.1)
    m_accepted = int(np.sum(covered_mask))
    k_errors = int(np.sum(errors[covered_mask])) if m_accepted > 0 else 0
    guaranteed_risk = calculate_guaranteed_risk_bound(m_accepted, k_errors)

    # Flag rate: fraction of samples flagged for retrieval augmentation
    flag_rate = 1.0 - coverage

    print(f"\n--- Threshold Sweep Calibration ---")
    print(f"AUROC:              {auroc:.4f}")
    print(f"Optimal Threshold:  {optimal_threshold:.4f}")
    print(f"Sensitivity (TPR):  {best_sensitivity:.4f} (Error detection rate)")
    print(f"Specificity (TNR):  {best_specificity:.4f} (Correct preservation rate)")
    print(f"Coverage:           {coverage:.2%} (Claims handled parametrically)")
    print(f"Flag Rate:          {flag_rate:.2%} (Claims flagged for retrieval)")
    print(f"Empirical Risk:     {risk:.4f} (Error rate on parametric claims)")
    print(f"Guaranteed Max Risk:{guaranteed_risk:.4f} (99% confidence)")
    print("-" * 30)

    # Generate calibration curve plots if save_dir is provided
    if save_dir is not None:
        rc_coverages, rc_risks = [], []
        for t in thresholds:
            t_covered = finite_scores < t
            t_cov = float(np.mean(t_covered))
            t_risk = float(np.mean(errors[t_covered])) if t_cov > 0 else 0.0
            rc_coverages.append(t_cov)
            rc_risks.append(t_risk)

        uq_method = Path(save_dir).name  # dynamically grab the UQ method folder name
        plot_calibration_curves(
            fpr, tpr, auroc,
            best_fpr=float(fpr[best_idx]), best_tpr=float(tpr[best_idx]),
            coverages=np.array(rc_coverages), risks=np.array(rc_risks),
            best_coverage=coverage, best_risk=risk,
            optimal_threshold=optimal_threshold,
            dataset_name=dataset_name, uq_method=uq_method, save_dir=save_dir,
            output_format=output_format, check_logic=check_logic, logic_eval_method=logic_eval_method
        )

    return optimal_threshold, best_sensitivity, best_specificity, best_j, auroc, coverage, risk, guaranteed_risk, flag_rate

# Main Execution

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="Calibrate threshold bounds")
    parser.add_argument("--dataset", type=str, default=None, help="Override dataset name")
    parser.add_argument("--split", type=str, default=None, help="Override split name")
    parser.add_argument("--model", type=str, default=None, help="Override model name")
    
    parser.add_argument("--check_logic", action="store_true", help="Enable the Logical Contradiction check")
    parser.add_argument("--output_format", type=str, default="label_only", help="Format suffix of the target file")
    parser.add_argument("--logic_eval_method", type=str, choices=["discrete", "probabilistic"], default="discrete", help="Evaluation method for the logical contradiction")
    
    return parser.parse_known_args()

def main():
    args, unknown = parse_args()
    from hydra import compose, initialize_config_dir
    initialize_config_dir(config_dir=str(ROOT_DIR / "config"), version_base=None)
    cfg = compose(config_name="config", overrides=unknown)

    if "AUTO_CONFIG" in os.environ:
        auto_cfg = json.loads(os.environ["AUTO_CONFIG"])
        if "dataset" in auto_cfg: cfg.data.dataset_name = auto_cfg["dataset"]
        if "calibration_split" in auto_cfg: cfg.data.split = auto_cfg["calibration_split"]
            
    if args.dataset: cfg.data.dataset_name = args.dataset
    if args.split: cfg.data.split = args.split
    if args.model: cfg.llm.model_name = args.model

    lock_random_seeds(42)
    dataset_name = cfg.data.dataset_name
    split = cfg.data.split
    model_name = cfg.llm.model_name.split("/")[-1]

    if args.check_logic:
        logic_str = f"logic_{args.logic_eval_method}"
    else:
        logic_str = "logic_OFF"

    base_dir = ROOT_DIR / "run_results" / dataset_name / model_name / "calibration"
    path = base_dir / f"uq_scores_{split}_{args.output_format}_{logic_str}.jsonl"
    
    print(f"\n{'='*60}")
    print(f"Running all calibration methods on: {path.relative_to(ROOT_DIR)}")
    print(f"{'='*60}")

    if not path.exists():
        print(f"❌ Error: Calibration file not found at {path.relative_to(ROOT_DIR)}")
        return

    estimators_present = []
    with open(path, 'r') as f:
        for line in f:
            try:
                d = json.loads(line)
                if "uq_scores" in d:
                    estimators_present = list(d["uq_scores"].keys())
                    break
            except json.JSONDecodeError:
                continue

    if not estimators_present:
        print("❌ Error: Valid UQ scores not found in the JSONL file.")
        return

    # AUROC-Optimal
    print(f"\n{'─'*40}")
    print(f"📐 Computing AUROC-Optimal Thresholds")
    print(f"{'─'*40}")

    optimal_thresholds_pack = {}

    for uq_method in estimators_present:
        print(f"\n====== Processing estimator: {uq_method} ======")
        method_dir = base_dir / uq_method
        method_dir.mkdir(parents=True, exist_ok=True)
        
        # Pass the format, trap flag, and eval method down to sweep_threshold!
        result = sweep_threshold(
            path, dataset_name, uq_method, save_dir=method_dir,
            output_format=args.output_format, check_logic=args.check_logic, logic_eval_method=args.logic_eval_method
        )
        optimal_thresh, sensitivity, specificity, j_score, auroc, ao_coverage, ao_risk, ao_guaranteed, ao_flag_rate = result

        if optimal_thresh is not None:
            optimal_thresholds_pack[uq_method] = {
                "dataset": dataset_name,
                "uq_method": uq_method,
                "calibration_method": "threshold_sweep",
                "optimal_threshold": float(optimal_thresh),
                "youden_j": float(j_score) if j_score is not None else None,
                "auroc": float(auroc),
                "sensitivity": float(sensitivity),
                "specificity": float(specificity),
                "coverage": float(ao_coverage),
                "flag_rate": float(ao_flag_rate),
                "empirical_risk": float(ao_risk),
                "guaranteed_max_risk": float(ao_guaranteed),
            }
        else:
            print(f"❌ Threshold sweep failed for {uq_method}.")

    # Save aggregated pack with the fully defined suffix so test configs don't overlap!
    save_path = base_dir / f"optimal_thresholds_{split}_{args.output_format}_{logic_str}.json"
    with open(save_path, 'w') as f:
        json.dump(optimal_thresholds_pack, f, indent=4)
    print(f"\n✅ All optimal thresholds saved to: {save_path.relative_to(ROOT_DIR)}")

    print(f"\n{'='*60}")
    print(f"✅ Joint calibration complete.")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()