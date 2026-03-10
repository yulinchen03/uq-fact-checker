import os
import json
import inspect
import inquirer
import numpy as np
from pathlib import Path
from omegaconf import DictConfig
from sklearn.metrics import balanced_accuracy_score, confusion_matrix, classification_report, precision_recall_fscore_support, recall_score
import hydra
import lm_polygraph.estimators as estimators

def validate_float(answers, current):
    """Validates that the user input can be safely cast to a float."""
    try:
        float(current)
        return True
    except ValueError:
        return False

def get_experiment_config():
    """Interactive menu for selecting which results to analyze."""
    if "AUTO_CONFIG" in os.environ:
        return json.loads(os.environ["AUTO_CONFIG"])

    available_estimators = [
        name for name, obj in inspect.getmembers(estimators, inspect.isclass)
    ]

    questions = [
        inquirer.List('dataset',
                      message="Select the dataset to evaluate",
                      choices=['scifact', 'quantemp']),

        inquirer.List('mode',
                      message="Select the experimental mode",
                      choices=['never_retrieve', 'always_retrieve', 'uq_aware']),
        
        inquirer.List('uq_method',
                      message="Select the UQ Method for this run",
                      choices=available_estimators,
                      ignore=lambda answers: answers.get('mode') != 'uq_aware'),
                      
        # Ask if we are analyzing the Calibration run or the Evaluation run
        inquirer.List('calibration',
                      message="Which run are you analyzing?",
                      choices=['Calibration (val)', 'Evaluation'],
                      ignore=lambda answers: answers.get('mode') != 'uq_aware'),

        inquirer.List('calibration_split',
                      message="Select the data split for calibration",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini'],
                      ignore=lambda answers: answers.get('calibration') != 'Calibration (val)'),

        inquirer.List('test_split',
                      message="Select the data split",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini','test_mini'],
                      ignore=lambda answers: answers.get('mode') == 'uq_aware' or answers.get('calibration') == 'Calibration (val)'),
    ]

    return inquirer.prompt(questions)


def normalize_label(label, dataset_name):
    """Cleans punctuation, underscores, and enforces strict academic evaluation."""
    lbl = str(label).upper().replace(".", "").replace("_", " ")
    lbl = " ".join(lbl.split())
    
    if dataset_name.lower() == 'scifact':
        mapping = {
            "SUPPORTED": "SUPPORT", 
            # (Thought) Partial support means the claim as a whole cannot be verified with given evidence/knowledge.
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
            # (Thought) A political/economic half-truth should be FALSE.
            "PARTIAL SUPPORT": "FALSE", 
            "PARTIALLY TRUE": "FALSE",
            "CONTRADICT": "FALSE", 
            "REFUTED": "FALSE", 
        }
        return mapping.get(lbl, lbl)
        
    return lbl


@hydra.main(version_base=None, config_path="config", config_name="config")
def analyze_results(cfg: DictConfig):
    # 1. Get the user configuration interactively or via batch
    config = get_experiment_config()
    if not config:
        print("Analysis cancelled.")
        return

    # 2. Set strict Hydra config overrides
    cfg.data.dataset_name = config['dataset']
    cfg.mode = config['mode']

    # Explicitly set the split and calibration mode
    if cfg.mode == 'uq_aware':
        cfg.uncertainty.method = config['uq_method']
        if config.get('calibration') == 'Calibration (val)':
            cfg.data.split = config['calibration_split']
            cfg.uncertainty.calibration_mode = True
        else:
            cfg.data.split = config['test_split']
            cfg.uncertainty.calibration_mode = False
    else:
        cfg.data.split = config['test_split']
        cfg.uncertainty.calibration_mode = False

    # 3. Define Paths
    if cfg.mode == 'uq_aware':
        if cfg.uncertainty.calibration_mode:
            file_path = f"results/RQ1/{cfg.data.dataset_name}/calibration/{cfg.uncertainty.method}/results.jsonl"
            save_path = f"results/RQ1/{cfg.data.dataset_name}/calibration/{cfg.uncertainty.method}/results_summary.json"
        else:
            file_path = f"results/RQ1/{cfg.data.dataset_name}/uq_aware/{cfg.uncertainty.method}/results_{cfg.data.split}.jsonl"
            save_path = f"results/RQ1/{cfg.data.dataset_name}/{cfg.mode}/{cfg.uncertainty.method}/results_{cfg.data.split}_summary.json"
    else:
        file_path = f"results/RQ1/{cfg.data.dataset_name}/{cfg.mode}/results_{cfg.data.split}.jsonl"
        save_path = f"results/RQ1/{cfg.data.dataset_name}/{cfg.mode}/results_{cfg.data.split}_summary.json"

    if not Path(file_path).exists():
        print(f"Error: Results file not found at {file_path}")
        print("Make sure you have run the experiment for this configuration first.")
        return
    
    print(f"Analyzing: {file_path}")
    
    y_true = []
    y_pred = []
    latencies = []
    total_tokens = []
    retrievals_triggered = np.array([])

    # 4. Parse Results
    with open(file_path, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                
                metrics = data.get("metrics", {})
                latencies.append(metrics.get("latency_seconds", 0.0))
                total_tokens.append(metrics.get("input_tokens", 0) + metrics.get("output_tokens", 0))
                
                gold_raw = data.get("gold_label", "NOT ENOUGH INFO")
                pred_raw = data.get("predicted_verdict", "NOT ENOUGH INFO")

                gold = normalize_label(gold_raw, cfg.data.dataset_name)
                pred = normalize_label(pred_raw, cfg.data.dataset_name)

                y_true.append(gold)
                y_pred.append(pred)

                retrieval = data.get("retrieval_triggered", False)
                retrievals_triggered = np.append(retrievals_triggered, retrieval)        

            except json.JSONDecodeError:
                continue

    if not y_true:
        print("No valid data found in the file.")
        return

    # --- CALCULATIONS ---
    if cfg.mode == 'uq_aware':
        retrieval_rate = retrievals_triggered.mean() if len(retrievals_triggered) > 0 else 0.0
    elif cfg.mode == 'always_retrieve':
        retrieval_rate = 1.0
    else:
        retrieval_rate = 0.0

    avg_latency = float(np.mean(latencies)) if latencies else 0.0
    avg_tokens = float(np.mean(total_tokens)) if total_tokens else 0.0
    total_claims = len(y_true)
    
    # 1. Define strict dataset labels
    if cfg.data.dataset_name == "quantemp":
        labels = ["TRUE", "FALSE", "CONFLICTING"]
    else:
        labels = ["SUPPORT", "CONTRADICT", "NOT ENOUGH INFO"]

    # 2. Native Sklearn Balanced Accuracy (Macro-Averaged Recall)
    # This natively penalizes NEI predictions
    bal_acc = recall_score(y_true, y_pred, labels=labels, average='macro', zero_division=0)
    
    # 3. Standard Sklearn Reporting
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, zero_division=0
    )
    conf_matrix = confusion_matrix(y_true, y_pred, labels=labels)

    stats_output = {
        "experiment_mode": cfg.mode,
        "dataset": cfg.data.dataset_name,
        "split": cfg.data.split,
        "total_claims": total_claims,
        "metrics": {
            "balanced_accuracy": bal_acc,
            "avg_latency_seconds": float(f"{avg_latency:.3f}"),
            "avg_token_overhead": int(avg_tokens),
            "retrieval_trigger_rate": float(f"{retrieval_rate*100:.2f}")
        }
    }

    if cfg.mode == 'uq_aware':
        stats_output["uq_settings"] = {
            "method": config.get('uq_method'),
            "calibration": config.get('calibration'),
            "threshold": cfg.uncertainty.threshold
        }

    stats_output["per_class_metrics"] = {}
    stats_output["confusion_matrix"] = {
        "labels": labels,
        "matrix": conf_matrix.tolist() 
    }

    for i, label in enumerate(labels):
        stats_output["per_class_metrics"][label] = {
            "precision": float(precision[i]),
            "recall": float(recall[i]),
            "f1-score": float(f1[i]),
            "support": int(support[i])
        }

    # --- SAVE TO FILE ---
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, 'w') as f:
        json.dump(stats_output, f, indent=4)

    # --- PRINT REPORT ---
    print("\n" + "="*40)
    print("       PERFORMANCE REPORT       ")
    print("="*40)
    print(f"1. Avg Inference Latency : {avg_latency:.3f} s/claim")
    print(f"2. Avg Token Overhead    : {avg_tokens:.0f} tokens/claim")
    print(f"3. Balanced Accuracy     : {bal_acc:.4f} ({(bal_acc*100):.2f}%)")
    print(f"4. Retrieval Ratio       : {retrieval_rate*100:.2f}%")
    print("-" * 40)
    print("\nDetailed Classification Report:")
    print(classification_report(y_true, y_pred, target_names=labels, zero_division=0))
    print(f"\nStats successfully saved to: {save_path}")

if __name__ == "__main__":
    try:
        analyze_results()
    except KeyboardInterrupt:
        import sys
        sys.exit(0)