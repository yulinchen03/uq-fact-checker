import json
import numpy as np
from omegaconf import DictConfig
from sklearn.metrics import balanced_accuracy_score, confusion_matrix, classification_report, precision_recall_fscore_support
from pathlib import Path
import hydra

@hydra.main(version_base=None, config_path="config", config_name="config")
def analyze_results(cfg: DictConfig):
    file_path = f"results/RQ1/{cfg.data.dataset_name}/{cfg.mode}/results_{cfg.data.split}.jsonl"
    if not Path(file_path).exists():
        print(f"Error: File not found at {file_path}")
        return
    save_path = f"results/RQ1/{cfg.data.dataset_name}/{cfg.mode}/results_{cfg.data.split}_stats.json"
    print(f"Analyzing: {file_path}")
    
    y_true = []
    y_pred = []
    latencies = []
    total_tokens = []

    # --- READ DATA ---
    with open(file_path, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                
                # Metrics
                metrics = data.get("metrics", {})
                latencies.append(metrics.get("latency_seconds", 0.0))
                total_tokens.append(metrics.get("input_tokens", 0) + metrics.get("output_tokens", 0))
                
                # Labels
                gold = data.get("gold_label", "NOT ENOUGH INFO").upper()
                raw_pred = data.get("predicted_verdict", "NOT ENOUGH INFO")
                pred = raw_pred.upper().strip() if raw_pred else "NOT ENOUGH INFO"
                
                y_true.append(gold)
                y_pred.append(pred)
            except json.JSONDecodeError:
                continue

    if not y_true:
        print("No valid data found.")
        return

    # --- CALCULATIONS ---
    
    # 1. Basic Stats
    avg_latency = float(np.mean(latencies))
    avg_tokens = float(np.mean(total_tokens))
    total_claims = len(y_true)
    
    # 2. Scikit-Learn Metrics
    # Get unique labels sorted to ensure consistent matrix order
    labels = sorted(list(set(y_true) | set(y_pred)))
    
    bal_acc = balanced_accuracy_score(y_true, y_pred)
    
    # Detailed per-class metrics
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, zero_division=0
    )
    
    conf_matrix = confusion_matrix(y_true, y_pred, labels=labels)

    stats_output = {
        "experiment_mode": cfg.mode,  # e.g., 'always_retrieve'
        "dataset": cfg.data.dataset_name, # e.g., 'scifact'
        "total_claims": total_claims,
        "metrics": {
            "balanced_accuracy": bal_acc,
            "avg_latency_seconds": avg_latency,
            "avg_token_overhead": avg_tokens
        },
        "per_class_metrics": {},
        "confusion_matrix": {
            "labels": labels,
            "matrix": conf_matrix.tolist() # Convert numpy array to list for JSON
        }
    }

    # Populate per-class metrics
    for i, label in enumerate(labels):
        stats_output["per_class_metrics"][label] = {
            "precision": float(precision[i]),
            "recall": float(recall[i]),
            "f1-score": float(f1[i]),
            "support": int(support[i])
        }

    # --- SAVE TO FILE ---
    with open(save_path, 'w') as f:
        json.dump(stats_output, f, indent=4)

    # --- PRINT REPORT ---
    print("\n" + "="*40)
    print("       PERFORMANCE REPORT       ")
    print("="*40)
    print(f"1. Avg Inference Latency : {avg_latency:.4f} s/claim")
    print(f"2. Avg Token Overhead    : {avg_tokens:.1f} tokens/claim")
    print(f"3. Balanced Accuracy     : {bal_acc:.4f} ({(bal_acc*100):.2f}%)")
    print("-" * 40)
    print("\nDetailed Classification Report:")
    print(classification_report(y_true, y_pred, target_names=labels, zero_division=0))

if __name__ == "__main__":
    analyze_results()