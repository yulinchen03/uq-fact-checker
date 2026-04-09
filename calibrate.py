import inspect
import json
import os
import hydra
import numpy as np
import inquirer
import matplotlib.pyplot as plt
import scipy.stats as stats
import lm_polygraph.estimators as estimators
from omegaconf import DictConfig
from sklearn.metrics import balanced_accuracy_score
import torch
import random
from transformers import set_seed

# ==========================================
# SETUP & UTILITIES
# ==========================================

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

def validate_float(answers, current):
    try:
        float(current)
        return True
    except ValueError:
        return False

def get_config():
    if "AUTO_CONFIG" in os.environ:
        return json.loads(os.environ["AUTO_CONFIG"])

    available_estimators = [
        name for name, obj in inspect.getmembers(estimators, inspect.isclass)
    ]

    questions = [
        inquirer.List('dataset',
                      message="Select the dataset to calibrate on",
                      choices=['scifact', 'quantemp']),
        
        inquirer.List('uq_method',
                      message="Select the UQ Method for this run",
                      choices=available_estimators),

        inquirer.List('calibration_split',
                      message="Select the data split",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini']),
    ]

    return inquirer.prompt(questions)

def clean_label(label: str) -> str:
    """
    Standardizes verdict labels to ensure strict matching during evaluation.
    
    Strips formatting artifacts, punctuation, and casing discrepancies from 
    model outputs to prevent false negative matches during accuracy calculations 
    (e.g., mapping "NOT_ENOUGH_INFO." to "NOT ENOUGH INFO").

    Args:
        label (str): The raw output string from the LLM or dataset.

    Returns:
        str: The normalized, uppercase label string.
    """
    lbl = str(label).upper().replace(".", "").replace("_", " ")
    return " ".join(lbl.split())

def calc_balanced_accuracy(y_true, y_pred, dataset_name=None):
    """Calculates balanced accuracy natively."""
    return balanced_accuracy_score(y_true, y_pred)


# ==========================================
# CORE CALIBRATION MODULES
# ==========================================

def load_and_clean_calibration_data(file_path, dataset_name):
    """Parses JSONL logs, strictly filters invalid labels, and extracts arrays."""
    print(f"Loading calibration data from: {file_path}")
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
        score = d.get('uncertainty_score')
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
    """
    Calculates the theoretical risk bound for the Selection with Guaranteed Risk (SGR) 
    algorithm (Geifman & El-Yaniv, 2017).
    
    To solve the Binomial sum defined in Lemma 3.1 of the SGR algorithm, we utilize the 
    Clopper-Pearson exact method. By passing our empirical errors and accepted sample sizes 
    through the Beta distribution's Percent Point Function (PPF) in SciPy, we mathematically 
    invert the Binomial CDF. This outputs the strict upper bound of our true risk, ensuring 
    with high statistical confidence (e.g., 99%) that our pipeline's real-world hallucination 
    rate on parametric queries will not exceed this value.

    Args:
        m_accepted (int): The total number of claims the model handled parametrically.
        k_errors (int): The absolute number of incorrect predictions made within the `m_accepted` set.
        delta_confidence (float, optional): The allowed probability of the bound failing. 
            Defaults to 0.01, representing a 99% statistical confidence guarantee.

    Returns:
        float: The guaranteed maximum real-world error rate ($b^*$) for the specified confidence level.
    """
    if m_accepted == 0:
        return 1.0
    # Solves Lemma 3.1 mathematically using the Beta Distribution PPF ()
    return float(stats.beta.ppf(1 - delta_confidence, k_errors + 1, m_accepted - k_errors))


def plot_calibration_curves(fpr, tpr, auroc, best_fpr, best_tpr,
                            coverages, risks, best_coverage, best_risk,
                            optimal_threshold, dataset_name, uq_method, save_dir):
    """
    Generates a side-by-side visualization of the ROC curve and Risk-Coverage curve.

    Panel 1 (ROC): Plots the Receiver Operating Characteristic with the
    Youden's J optimal operating point marked in red.
    Panel 2 (Risk-Coverage): Plots the parametric error rate as a function
    of coverage, with the operating point at the chosen threshold.

    Args:
        fpr, tpr (np.ndarray): False/True positive rate arrays from roc_curve.
        auroc (float): Area Under the ROC Curve.
        best_fpr, best_tpr (float): FPR/TPR at the Youden's J point.
        coverages, risks (np.ndarray): Coverage and risk arrays from threshold sweep.
        best_coverage, best_risk (float): Coverage/risk at the chosen threshold.
        optimal_threshold (float): The selected threshold value.
        dataset_name, uq_method, save_dir (str): Metadata for titling and saving.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # ---- Panel 1: ROC Curve ----
    ax1.plot(fpr, tpr, color='#2563eb', linewidth=2, label=f'{uq_method} (AUROC: {auroc:.4f})')
    ax1.plot([0, 1], [0, 1], 'k--', alpha=0.4, label='Random Chance')
    ax1.scatter([best_fpr], [best_tpr], color='red', s=80, zorder=5,
               label=f"Youden's J (t={optimal_threshold:.3f})")
    ax1.set_title(f'ROC Curve: {dataset_name.capitalize()}')
    ax1.set_xlabel('False Positive Rate (1 - Specificity)')
    ax1.set_ylabel('True Positive Rate (Sensitivity)')
    ax1.legend(loc='lower right')
    ax1.grid(True, linestyle='--', alpha=0.4)
    ax1.set_xlim([-0.02, 1.02])
    ax1.set_ylim([-0.02, 1.02])

    # ---- Panel 2: Risk-Coverage Curve ----
    sorted_idx = np.argsort(coverages)
    sorted_cov = coverages[sorted_idx]
    sorted_risk = risks[sorted_idx]

    ax2.plot(sorted_cov, sorted_risk, color='#2563eb', linewidth=2, label=f'{uq_method}')
    ax2.fill_between(sorted_cov, sorted_risk, color='#2563eb', alpha=0.08)
    ax2.scatter([best_coverage], [best_risk], color='red', s=80, zorder=5,
               label=f'Operating Point (C={best_coverage:.2f}, R={best_risk:.3f})')
    ax2.set_title(f'Risk-Coverage Curve: {dataset_name.capitalize()}')
    ax2.set_xlabel('Coverage (Fraction handled parametrically)')
    ax2.set_ylabel('Risk (Error rate on covered claims)')
    ax2.legend(loc='upper left')
    ax2.grid(True, linestyle='--', alpha=0.4)

    plt.tight_layout()
    plot_path = os.path.join(save_dir, 'calibration_curves.png')
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"\n📈 Calibration curves saved to: {plot_path}")


# ==========================================
# NAIVE CALIBRATION
# ==========================================

def naive_threshold(file_path, dataset_name):
    """
    Naive calibration method that takes the median of uncertainty scores as the threshold.

    This serves as a naive baseline to compare against the AUROC-optimal threshold sweep.
    By using the median, roughly half of all claims are routed parametrically and half 
    are flagged as uncertain, providing a simple split without any accuracy-driven optimization.

    Args:
        file_path (str): The JSONL calibration file path.
        dataset_name (str): Target dataset name.

    Returns:
        tuple: (threshold, sensitivity, specificity, auroc, coverage, risk)
    """
    from sklearn.metrics import roc_curve, roc_auc_score

    scores, y_true, y_para, excluded_count = load_and_clean_calibration_data(file_path, dataset_name)
    if scores is None:
        print("Error: No data found in file.")
        return None, None, None, None, None, None

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
        return None, None, None, None, None, None

    # Binary error labels: 1 = parametric was wrong, 0 = parametric was correct
    errors = (finite_para != finite_true).astype(int)

    # Compute median as threshold
    median_threshold = float(np.median(finite_scores))

    # Coverage and risk at the median threshold
    covered_mask = finite_scores < median_threshold
    coverage = float(np.mean(covered_mask))
    risk = float(np.mean(errors[covered_mask])) if coverage > 0 else 0.0

    # Guaranteed risk bound (Lemma 3.1)
    m_accepted = int(np.sum(covered_mask))
    k_errors = int(np.sum(errors[covered_mask])) if m_accepted > 0 else 0
    guaranteed_risk = calculate_guaranteed_risk_bound(m_accepted, k_errors)

    # Compute AUROC and sensitivity/specificity at the median threshold
    auroc = None
    sensitivity = None
    specificity = None
    if len(set(errors)) >= 2:
        fpr, tpr, thresholds = roc_curve(errors, finite_scores)
        auroc = float(roc_auc_score(errors, finite_scores))

        # Find the closest threshold in the ROC curve to our median
        closest_idx = np.argmin(np.abs(thresholds - median_threshold))
        sensitivity = float(tpr[closest_idx])
        specificity = float(1 - fpr[closest_idx])

    print(f"\n--- Naive Calibration (Median) ---")
    print(f"Median Threshold:    {median_threshold:.4f}")
    if auroc is not None:
        print(f"AUROC:              {auroc:.4f}")
        print(f"Sensitivity (TPR):  {sensitivity:.4f} (Error detection rate)")
        print(f"Specificity (TNR):  {specificity:.4f} (Correct preservation rate)")
    print(f"Coverage:           {coverage:.2%} (Claims handled parametrically)")
    print(f"Empirical Risk:     {risk:.4f} (Error rate on parametric claims)")
    print(f"Guaranteed Max Risk:{guaranteed_risk:.4f} (99% confidence)")
    print("-" * 30)

    return median_threshold, sensitivity, specificity, auroc, coverage, risk, guaranteed_risk


# ==========================================
# THRESHOLD SWEEP CALIBRATION
# ==========================================

def sweep_threshold(file_path, dataset_name, save_dir=None):
    """
    Mode-agnostic calibration using the AUROC-optimal operating point (Youden's J statistic).

    Finds the threshold that best separates correct from incorrect parametric
    predictions by maximizing sensitivity + specificity - 1.
    This is the point on the ROC curve furthest from the diagonal.

    Optionally generates ROC and Risk-Coverage curve plots when save_dir is provided.

    Args:
        file_path (str): The JSONL calibration file path.
        dataset_name (str): Target dataset name.
        save_dir (str, optional): Directory to save calibration curve plots.

    Returns:
        tuple: (threshold, sensitivity, specificity, j_score, auroc, coverage, risk)
    """
    from sklearn.metrics import roc_curve, roc_auc_score

    scores, y_true, y_para, excluded_count = load_and_clean_calibration_data(file_path, dataset_name)
    if scores is None:
        print("Error: No data found in file.")
        return None, None, None, None, None, None, None

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
        return None, None, None, None, None, None, None

    # Binary error labels: 1 = parametric was wrong, 0 = parametric was correct
    errors = (finite_para != finite_true).astype(int)

    # Need both classes present for AUROC
    if len(set(errors)) < 2:
        print("Error: All predictions are either correct or incorrect. Cannot compute AUROC-optimal threshold.")
        return None, None, None, None, None, None, None

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

    print(f"\n--- Threshold Sweep Calibration ---")
    print(f"AUROC:              {auroc:.4f}")
    print(f"Optimal Threshold:  {optimal_threshold:.4f}")
    print(f"Sensitivity (TPR):  {best_sensitivity:.4f} (Error detection rate)")
    print(f"Specificity (TNR):  {best_specificity:.4f} (Correct preservation rate)")
    print(f"Coverage:           {coverage:.2%} (Claims handled parametrically)")
    print(f"Empirical Risk:     {risk:.4f} (Error rate on parametric claims)")
    print(f"Guaranteed Max Risk:{guaranteed_risk:.4f} (99% confidence)")
    print("-" * 30)

    # Generate calibration curve plots if save_dir is provided
    if save_dir is not None:
        # Build risk-coverage arrays by sweeping across all ROC thresholds
        rc_coverages, rc_risks = [], []
        for t in thresholds:
            t_covered = finite_scores < t
            t_cov = float(np.mean(t_covered))
            t_risk = float(np.mean(errors[t_covered])) if t_cov > 0 else 0.0
            rc_coverages.append(t_cov)
            rc_risks.append(t_risk)

        uq_method = os.path.basename(os.path.dirname(save_dir))  # infer from path
        plot_calibration_curves(
            fpr, tpr, auroc,
            best_fpr=float(fpr[best_idx]), best_tpr=float(tpr[best_idx]),
            coverages=np.array(rc_coverages), risks=np.array(rc_risks),
            best_coverage=coverage, best_risk=risk,
            optimal_threshold=optimal_threshold,
            dataset_name=dataset_name, uq_method=uq_method, save_dir=save_dir
        )

    return optimal_threshold, best_sensitivity, best_specificity, best_j, auroc, coverage, risk, guaranteed_risk

# ==========================================
# MAIN EXECUTION
# ==========================================

@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg: DictConfig):
    lock_random_seeds(42)

    config = get_config()
    if not config:
        print("Calibration aborted...")
        return
    
    model_name = cfg.llm.model_name.split("/")[-1]
    
    # The calibration JSONL lives in the UQ method folder, independent of calibration method
    path = f"results/RQ1/{config['dataset']}/{model_name}/calibration/{config['uq_method']}/results_{config['calibration_split']}.jsonl"
    
    print(f"\n{'='*60}")
    print(f"Running all calibration methods on: {path}")
    print(f"{'='*60}")

    # ===== 1. BASELINE (Median) =====
    print(f"\n{'─'*40}")
    print(f"📐 Method 1: NAIVE (Median)")
    print(f"{'─'*40}")

    base_dir = f"results/RQ1/{config['dataset']}/{model_name}/calibration/naive/{config['uq_method']}"
    save_path = f"{base_dir}/optimal_threshold_{config['calibration_split']}.json"
    os.makedirs(base_dir, exist_ok=True)

    median_thresh, n_sensitivity, n_specificity, n_auroc, coverage, risk, n_guaranteed = naive_threshold(path, config['dataset'])

    if median_thresh is not None:
        naive_result = {
            "dataset": config['dataset'],
            "uq_method": config['uq_method'],
            "calibration_method": "naive",
            "optimal_threshold": float(median_thresh),
            "coverage": float(coverage),
            "empirical_risk": float(risk),
            "guaranteed_max_risk": float(n_guaranteed),
        }
        if n_auroc is not None:
            naive_result["auroc"] = float(n_auroc)
            naive_result["sensitivity"] = float(n_sensitivity)
            naive_result["specificity"] = float(n_specificity)
        with open(save_path, 'w') as f:
            json.dump(naive_result, f, indent=4)
        print(f"✅ Naive threshold saved to: {save_path}")

    # ===== 2. AUROC-OPTIMAL =====
    print(f"\n{'─'*40}")
    print(f"📐 Method 2: THRESHOLD SWEEP")
    print(f"{'─'*40}")

    base_dir = f"results/RQ1/{config['dataset']}/{model_name}/calibration/threshold_sweep/{config['uq_method']}"
    save_path = f"{base_dir}/optimal_threshold_{config['calibration_split']}.json"
    os.makedirs(base_dir, exist_ok=True)

    result = sweep_threshold(path, config['dataset'], save_dir=base_dir)
    optimal_thresh, sensitivity, specificity, j_score, auroc, ao_coverage, ao_risk, ao_guaranteed = result

    if optimal_thresh is not None:
        with open(save_path, 'w') as f:
            json.dump({
                "dataset": config['dataset'],
                "uq_method": config['uq_method'],
                "calibration_method": "threshold_sweep",
                "optimal_threshold": float(optimal_thresh),
                "auroc": float(auroc),
                "sensitivity": float(sensitivity),
                "specificity": float(specificity),
                "coverage": float(ao_coverage),
                "empirical_risk": float(ao_risk),
                "guaranteed_max_risk": float(ao_guaranteed),
            }, f, indent=4)
        print(f"✅ Threshold sweep saved to: {save_path}")
    else:
        print("❌ Threshold sweep calibration failed. No threshold saved.")

    print(f"\n{'='*60}")
    print(f"✅ All calibration methods complete.")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()