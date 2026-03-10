import inspect
import json
import os
import numpy as np
import inquirer
import matplotlib.pyplot as plt
import lm_polygraph.estimators as estimators
from sklearn.metrics import auc, recall_score
import torch
import random
from transformers import set_seed

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
                      
        inquirer.Text('tolerance',
                      message="Enter the acceptable absolute accuracy drop from full RAG (delta, e.g., 0.05 for 5%)",
                      validate=validate_float,
                      default="0.05")
    ]

    return inquirer.prompt(questions)

def normalize_label(label, dataset_name):
    """Strict academic normalization mapping (penalizes partial/hedged answers)."""
    lbl = str(label).upper().replace(".", "").replace("_", " ")
    lbl = " ".join(lbl.split())
    
    if dataset_name.lower() == 'scifact':
        mapping = {
            "SUPPORTED": "SUPPORT", 
            "PARTIAL SUPPORT": "NOT ENOUGH INFO", 
            "REFUTED": "CONTRADICT", 
            "NEI": "NOT ENOUGH INFO", 
            "NOT": "NOT ENOUGH INFO"
        }
        return mapping.get(lbl, lbl)
        
    elif dataset_name.lower() == 'quantemp':
        mapping = {
            "SUPPORT": "TRUE", 
            "SUPPORTED": "TRUE", 
            "PARTIAL SUPPORT": "FALSE", 
            "CONTRADICT": "FALSE", 
            "REFUTED": "FALSE", 
            "NEI": "CONFLICTING", 
            "NOT ENOUGH INFO": "CONFLICTING"
        }
        return mapping.get(lbl, lbl)
        
    return lbl

def calc_balanced_accuracy(y_true, y_pred, dataset_name):
    """Matches the exact macro-recall math used in analyze_rq1.py."""
    if dataset_name.lower() == "quantemp":
        labels = ["TRUE", "FALSE", "CONFLICTING"]
    else:
        labels = ["SUPPORT", "CONTRADICT", "NOT ENOUGH INFO"]
        
    return recall_score(y_true, y_pred, labels=labels, average='macro', zero_division=0)

def optimize_threshold_and_plot(file_path, save_dir, dataset_name, uq_method, delta):
    print(f"Loading calibration data from: {file_path}")
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    if not data:
        print("Error: No data found in file.")
        return None, None, None

    # 1. Extract and Clean Data
    raw_scores = []
    for d in data:
        score = d.get('uncertainty_score')
        if score is None or np.isnan(score):
            raw_scores.append(np.inf) # Force failed estimations to infinity (always trigger RAG)
        else:
            raw_scores.append(score)
            
    scores = np.array(raw_scores)
    y_true = np.array([normalize_label(d['gold_label'], dataset_name) for d in data])
    y_para = np.array([normalize_label(d.get('parametric_verdict', 'NOT ENOUGH INFO'), dataset_name) for d in data])
    y_rag = np.array([normalize_label(d.get('rag_prediction', 'NOT ENOUGH INFO'), dataset_name) for d in data])

    # 2. Isolate Finite Scores for the Search Space
    finite_scores = scores[np.isfinite(scores)]
    if len(finite_scores) == 0:
        print("Error: No valid uncertainty scores found. All evaluated to infinity.")
        return 0.0, 0.0, 0.0

    print(f"\n--- Score Distribution Statistics (Excluding Inf) ---")
    print(f"Min Score: {finite_scores.min():.4f}")
    print(f"Max Score: {finite_scores.max():.4f}")
    print(f"Mean Score: {finite_scores.mean():.4f}")
    print(f"Failed Estimates (Inf): {len(scores) - len(finite_scores)}")
    print("-" * 30)

    # 3. Establish Baselines
    acc_para = calc_balanced_accuracy(y_true, y_para, dataset_name)
    acc_rag = calc_balanced_accuracy(y_true, y_rag, dataset_name)
    
    # 3. Establish Baselines
    acc_para = calc_balanced_accuracy(y_true, y_para, dataset_name)
    acc_rag = calc_balanced_accuracy(y_true, y_rag, dataset_name)
    gap = 1 - (acc_para / acc_rag) # relative performance gap % between rag and parametric (positive: rag better, negative: parametric better)

    print(f"\n--- Baselines (Strict Balanced Accuracy) ---")
    print(f"Parametric Only (0% RAG):   {acc_para:.4f}")
    print(f"RAG Only (100% RAG):        {acc_rag:.4f}")
    print(f"Relative Gap:            {gap * 100:.4f}%")
    
    # Adaptive Risk Tolerance Logic
    if gap <= 0:  # parametric is better
        target_acc = acc_para 
        print(f"Target Hybrid Accuracy:     >= {target_acc:.4f}")
    elif gap <= delta:  # e.g max tolerable loss: 5%, parametric performs at 97% relative to rag, then target acc is (0.97+(1-0.97)/2)*rag score
        target_acc = acc_para + ((acc_rag - acc_para) / 2) # midway accuracy between parametric and rag
        print(f"Target Hybrid Accuracy:     >= {target_acc:.4f} (Midpoint accuracy applied)")
    else:  # if target is still greater than parametric performance
        target_acc = acc_rag * (1 - delta) # maximum tolerable loss
        print(f"Target Hybrid Accuracy:     >= {target_acc:.4f} (Applying Delta: {delta*100}%)")
        
    print("-" * 30)
    
    print(f"\n--- Baselines (Strict Balanced Accuracy) ---")
    print(f"Parametric Only (0% RAG):   {acc_para:.4f}")
    print(f"RAG Only (100% RAG):        {acc_rag:.4f}")
    print(f"Target Hybrid Accuracy:     >= {target_acc:.4f} (Applying Delta: {delta*100}%)")
    print("-" * 30)

    # 4. Dynamic Threshold Search
    search_space = np.linspace(finite_scores.min() - 1e-5, finite_scores.max() + 1e-5, num=1000)
    
    best_thresh = None
    best_coverage = -1.0
    best_acc = 0.0

    coverages = []
    risks = []

    for t in search_space:
        # If score is inf, it's always >= t, so it safely routes to RAG
        y_hybrid = np.where(scores < t, y_para, y_rag) 
        acc = calc_balanced_accuracy(y_true, y_hybrid, dataset_name)
        
        covered_indices = (scores < t)
        coverage = np.mean(covered_indices)
        
        if coverage > 0:
            covered_true = y_true[covered_indices]
            covered_para = y_para[covered_indices]
            risk = np.mean(covered_true != covered_para) 
        else:
            risk = 0.0
            
        coverages.append(coverage)
        risks.append(risk)
        
        if acc >= target_acc:
            if coverage > best_coverage:
                best_coverage = coverage
                best_acc = acc
                best_thresh = t
            elif coverage == best_coverage and acc > best_acc:
                best_acc = acc
                best_thresh = t

    # 5. Calculate AURC
    sorted_indices = np.argsort(coverages)
    sorted_coverages = np.array(coverages)[sorted_indices]
    sorted_risks = np.array(risks)[sorted_indices]
    
    calculated_aurc = auc(sorted_coverages, sorted_risks)

    # 6. Plot Risk-Coverage Curve
    plt.figure(figsize=(8, 6))
    plt.plot(sorted_coverages, sorted_risks, color='blue', linewidth=2, label=f'{uq_method} (AURC: {calculated_aurc:.4f})')
    plt.fill_between(sorted_coverages, sorted_risks, color='blue', alpha=0.1)
    
    if best_thresh is not None:
        best_risk_idx = np.abs(sorted_coverages - best_coverage).argmin()
        best_risk = sorted_risks[best_risk_idx]
        plt.scatter([best_coverage], [best_risk], color='red', zorder=5, label=f'Chosen Threshold (C={best_coverage:.2f}, R={best_risk:.2f})')

    plt.title(f'Risk-Coverage Curve: {dataset_name.capitalize()}')
    plt.xlabel('Coverage (Fraction of claims handled parametrically)')
    plt.ylabel('Risk (Parametric Error Rate on Covered Claims)')
    plt.legend(loc="upper left")
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plot_path = os.path.join(save_dir, 'aurc_plot.png')
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\n📈 Risk-Coverage curve saved to: {plot_path}")
    print(f"📊 Calculated AURC: {calculated_aurc:.4f} (Lower is better)")

    # 7. Print Optimization Results
    if best_thresh is not None:
        retrieval_rate = 1.0 - best_coverage
        print(f"\n--- Optimization Results ---")
        print(f"Optimal Threshold: {best_thresh:.4f}")
        print(f"Hybrid Accuracy:   {best_acc:.4f} (Target was {target_acc:.4f})")
        print(f"Compute Saved:     {best_coverage:.2%} (Queries handled parametrically)")
        print(f"Retrieval Rate:    {retrieval_rate:.2%} (Queries sent to RAG)")
    else:
        print("\n❌ Warning: Could not find a threshold that satisfies the tolerance constraint.")
        print("Falling back to Always Retrieve (Threshold = 0.0)")
        best_thresh = 0.0

    return best_thresh, best_acc, calculated_aurc

def main():
    lock_random_seeds(42)

    config = get_config()
    if not config:
        print("Calibration aborted...")
        return
        
    delta = float(config['tolerance'])
    
    base_dir = f"results/RQ1/{config['dataset']}/calibration/{config['uq_method']}"
    path = f"{base_dir}/results_{config['calibration_split']}.jsonl"
    save_path = f"{base_dir}/optimal_threshold_{config['calibration_split']}.json"
    
    os.makedirs(base_dir, exist_ok=True)
    
    best_thresh, achieved_acc, aurc_score = optimize_threshold_and_plot(
        path, base_dir, config['dataset'], config['uq_method'], delta
    )

    if best_thresh is not None:
        with open(save_path, 'w') as f:
            json.dump({
                "dataset": config['dataset'],
                "uq_method": config['uq_method'],
                "optimal_threshold": float(best_thresh),
                "tolerance_delta": delta,
                "calibrated_accuracy": float(achieved_acc),
                "aurc": float(aurc_score)
            }, f, indent=4)
        print(f"\n✅ Threshold metadata saved to: {save_path}")

if __name__ == "__main__":
    main()