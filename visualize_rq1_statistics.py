import inspect
import os
import string
import sys
import hydra
import inquirer
from omegaconf import DictConfig
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import balanced_accuracy_score
import lm_polygraph.estimators as estimators

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

def load_calibration_data(filepath: str, dataset_name: str) -> pd.DataFrame:
    """
    Parses your specific JSONL format into a flat pandas DataFrame and sanitizes labels.
    """
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            row = json.loads(line)
            
            # Extract nested metrics
            metrics = row.get("metrics", {})
            input_tokens = metrics.get("input_tokens", 0)
            output_tokens = metrics.get("output_tokens", 0)
            
            clean_gold = normalize_label(row.get("gold_label", ""), dataset_name)
            clean_param = normalize_label(row.get("parametric_verdict", ""), dataset_name)
            clean_rag = normalize_label(row.get("rag_prediction", ""), dataset_name)
            
            data.append({
                "id": row["id"],
                "gold_label": clean_gold,
                "parametric_verdict": clean_param,
                "rag_prediction": clean_rag,
                "uncertainty_score": row["uncertainty_score"],
                # We assume bypassing RAG saves ~85% of input tokens (no evidence in prompt)
                "parametric_tokens_estimated": (input_tokens * 0.15) + output_tokens,
                "rag_tokens_total": input_tokens + output_tokens
            })
    
    return pd.DataFrame(data)

def generate_all_plots(df: pd.DataFrame, save_path: string):
    # Sort the dataframe by UQ score (lowest uncertainty first)
    df_sorted = df.sort_values(by="uncertainty_score", ascending=True).reset_index(drop=True)
    total_claims = len(df_sorted)
    
    # ---------------------------------------------------------
    # PLOT 1: Trade-off: Parametric Coverage vs. Accuracy
    # ---------------------------------------------------------
    percentages, accuracies, avg_tokens_list = [], [], []
    
    for pct in range(0, 101, 5):
        n_param = int((pct / 100.0) * total_claims)
        
        # Split predictions based on threshold
        param_subset = df_sorted.iloc[:n_param]
        rag_subset = df_sorted.iloc[n_param:]
        
        combined_preds = pd.concat([param_subset['parametric_verdict'], rag_subset['rag_prediction']])
        acc = balanced_accuracy_score(df_sorted['gold_label'], combined_preds)
        
        # Calculate tokens
        total_tokens = param_subset['parametric_tokens_estimated'].sum() + rag_subset['rag_tokens_total'].sum()
        
        percentages.append(pct)
        accuracies.append(acc)
        avg_tokens_list.append(total_tokens / total_claims)

    plt.figure(figsize=(9, 5))
    plt.plot(percentages, accuracies, marker='o', linewidth=2, color='#1E3046')
    plt.title('Trade-off: Parametric Coverage vs. Balanced Accuracy', fontsize=14, fontweight='bold')
    plt.xlabel('% of Claims Handled Parametrically (Bypassing RAG)', fontsize=12)
    plt.ylabel('Overall Balanced Accuracy', fontsize=12)
    plt.axhline(y=accuracies[0], color='green', linestyle=':', label=f'100% RAG ({accuracies[0]:.2f})')
    plt.axhline(y=accuracies[-1], color='red', linestyle=':', label=f'100% Parametric ({accuracies[-1]:.2f})')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path + '/1_coverage_vs_accuracy.png', dpi=150)
    plt.close()

    # ---------------------------------------------------------
    # PLOT 2: UQ Score Distribution (Violin Plot)
    # ---------------------------------------------------------
    df['parametric_is_correct'] = df['parametric_verdict'] == df['gold_label']
    
    plt.figure(figsize=(8, 5))
    sns.violinplot(
        x='parametric_is_correct', 
        y='uncertainty_score', 
        data=df, 
        inner='quartile',
        palette=['#e74c3c', '#2ecc71'],
    )
    plt.title('Uncertainty Distribution: Correct vs. Incorrect Predictions', fontsize=14, fontweight='bold')
    plt.xticks([0, 1], ['Incorrect (Needs RAG)', 'Correct (Bypass RAG)'], fontsize=12)
    plt.ylabel('Calculated Uncertainty Score', fontsize=12)
    plt.xlabel('')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(save_path + '/2_uq_distribution.png', dpi=150)
    plt.close()

    # ---------------------------------------------------------
    # PLOT 3: The "Harm vs. Help" Matrix
    # ---------------------------------------------------------
    param_correct = df['parametric_verdict'] == df['gold_label']
    rag_correct = df['rag_prediction'] == df['gold_label']
    
    conditions = [
        (~param_correct) & rag_correct,   # RAG Fixed it
        param_correct & (~rag_correct),   # RAG Broke it
        param_correct & rag_correct,      # Both Right
        (~param_correct) & (~rag_correct) # Both Wrong
    ]
    choices = ['RAG Helped\n(Fixed Error)', 'RAG Harmed\n(Induced Error)', 'Both Correct\n(Redundant)', 'Both Incorrect\n(Unsolved)']
    
    df['transition_state'] = np.select(conditions, choices)
    counts = df['transition_state'].value_counts().reindex(choices)
    
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(x=counts.index, y=counts.values, palette=['#2ecc71', '#e74c3c', '#3498db', '#95a5a6'])
    plt.title('The Behavioral Impact of RAG on Parametric Knowledge', fontsize=14, fontweight='bold')
    plt.ylabel('Number of Claims', fontsize=12)
    
    for i, v in enumerate(counts.values):
        ax.text(i, v + (max(counts.values) * 0.02), str(v), ha='center', fontsize=12, fontweight='bold')
        
    plt.tight_layout()
    plt.savefig(save_path + '/3_harm_help_matrix.png', dpi=150)
    plt.close()

    # ---------------------------------------------------------
    # PLOT 4: Efficiency Trade-off (Tokens vs Accuracy)
    # ---------------------------------------------------------
    plt.figure(figsize=(9, 5))
    plt.plot(avg_tokens_list, accuracies, marker='o', linestyle='-', color='#8e44ad', linewidth=2)
    plt.title('Efficiency Trade-off: Estimated Token Cost vs. Balanced Accuracy', fontsize=14, fontweight='bold')
    plt.xlabel('Estimated Average Tokens Consumed Per Claim', fontsize=12)
    plt.ylabel('Overall Balanced Accuracy', fontsize=12)
    
    best_idx = np.argmax(accuracies)
    plt.plot(avg_tokens_list[best_idx], accuracies[best_idx], marker='*', markersize=18, color='gold', markeredgecolor='black', label="Optimal Threshold")
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path + '/4_token_pareto_frontier.png', dpi=150)
    plt.close()
    
    print("✅ All 4 plots successfully generated and saved to your directory.")

def get_experiment_config():
    if "AUTO_CONFIG" in os.environ:
        return json.loads(os.environ["AUTO_CONFIG"])
    
    available_estimators = [
        name for name, obj in inspect.getmembers(estimators, inspect.isclass)
    ]

    questions = [
        inquirer.List('dataset',
                      message="Select the dataset to visualize results",
                      choices=['scifact', 'quantemp']),
        
        inquirer.List('uq_method',
                      message="Select the UQ Method for this run",
                      choices=available_estimators),

        inquirer.List('calibrated_split',
                      message="Select the data split which was used for calibration",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini']),
    ]

    return inquirer.prompt(questions)

@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg: DictConfig):
    config = get_experiment_config()
        
    if not config:
        print("Experiment cancelled.")
        sys.exit(0)

    dataset = config['dataset']
    uq_method = config['uq_method']
    calibrated_split = config['calibrated_split']
    model_name = cfg.llm.model_name.split("/")[1]

    # Replace with your actual filepath
    path = f"results/RQ1/{dataset}/{model_name}/calibration/{uq_method}/results_{calibrated_split}.jsonl"
    save_path = f"vis/RQ1/{dataset}/{model_name}/calibration/{uq_method}/{calibrated_split}"

    os.makedirs(save_path, exist_ok=True)

    df_calibration = load_calibration_data(path, dataset)
    generate_all_plots(df_calibration, save_path)

# --- Execution ---
if __name__ == "__main__":
    main()