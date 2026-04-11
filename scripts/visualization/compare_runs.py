import os
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path
from collections import defaultdict

def load_json(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def shorten_name(name):
    """Shortens long estimator names for cleaner X-axis labels."""
    mapping = {
        "MaximumSequenceProbability": "MaxSeqProb",
        "MeanTokenEntropy": "MeanTokenEnt",
        "MeanPointwiseMutualInformation": "MeanPMI",
        "MeanConditionalPointwiseMutualInformation": "MeanCPMI",
        "never_retrieve": "Parametric\n(0% RAG)",
        "always_retrieve": "100% RAG"
    }
    return mapping.get(name, name)

def get_fine_tokens(metrics):
    """Safely extracts fine-grained token metrics with fallbacks for older runs."""
    uq_in = metrics.get('avg_uq_input_tokens', 0)
    uq_out = metrics.get('avg_uq_output_tokens', 0)
    gen_in = metrics.get('avg_gen_input_tokens', metrics.get('avg_rag_input_tokens', 0))
    gen_out = metrics.get('avg_gen_output_tokens', metrics.get('avg_rag_output_tokens', 0))
    
    # Fallback to older aggregate keys if the fine-grained ones are completely missing
    if uq_in == 0 and uq_out == 0 and metrics.get('avg_uq_tokens', 0) > 0:
        uq_out = metrics.get('avg_uq_tokens', 0)
    if gen_in == 0 and gen_out == 0:
        gen_out = metrics.get('avg_gen_tokens', metrics.get('avg_rag_tokens', metrics.get('avg_total_tokens', 0)))
        
    return uq_in, uq_out, gen_in, gen_out

def generate_accuracy_plot(dataset, split, sorted_records, save_path):
    labels = [r['Display_Name'] for r in sorted_records]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(14, 7))
    
    max_acc = 0.0

    # Iterating to handle the single-bar Parametric vs split-bar RAG logic
    for i, r in enumerate(sorted_records):
        if r['Method_Raw'] == 'never_retrieve':
            # Parametric gets a single, centered, slightly wider bar
            val = r.get('Base_Acc', 0.0)
            rect = ax.bar(x[i], val, width * 1.5, color='#e74c3c', edgecolor='black')
            ax.bar_label(rect, fmt='%.3f', padding=3, fontsize=10, fontweight='bold')
            max_acc = max(max_acc, val)
        else:
            # Everything else gets the Base vs Gold split bars
            b_val = r.get('Base_Acc', 0.0)
            g_val = r.get('Gold_Acc', 0.0)
            rect1 = ax.bar(x[i] - width/2, b_val, width, color='#3498db', edgecolor='black')
            rect2 = ax.bar(x[i] + width/2, g_val, width, color='#f1c40f', edgecolor='black')
            ax.bar_label(rect1, fmt='%.3f', padding=3, fontsize=10, fontweight='bold')
            ax.bar_label(rect2, fmt='%.3f', padding=3, fontsize=10, fontweight='bold')
            max_acc = max(max_acc, b_val, g_val)

    ax.set_ylabel('Balanced Accuracy (0.0 - 1.0)', fontsize=12, fontweight='bold')
    ax.set_title(f'Base vs. Gold Accuracy Comparison | Dataset: {dataset.upper()} ({split.capitalize()})', fontsize=16, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=11)
    
    # Give 20% headroom for labels
    if max_acc > 0:
        ax.set_ylim(0, max_acc * 1.2)
        
    # Custom legend incorporating the Parametric distinct color
    legend_elements = [
        mpatches.Patch(facecolor='#e74c3c', edgecolor='black', label='Parametric (0% RAG)'),
        mpatches.Patch(facecolor='#3498db', edgecolor='black', label='Base (Vector Evidence)'),
        mpatches.Patch(facecolor='#f1c40f', edgecolor='black', label='Gold Evidence')
    ]
    ax.legend(handles=legend_elements, fontsize=11, loc="upper left")
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"✅ Accuracy plot saved: {save_path}")

def generate_token_plot(dataset, split, sorted_records, save_path):
    labels = [r['Display_Name'] for r in sorted_records]
    
    uq_in = np.array([r.get('UQ_Input_Tokens', 0) for r in sorted_records])
    uq_out = np.array([r.get('UQ_Output_Tokens', 0) for r in sorted_records])
    gen_in = np.array([r.get('Gen_Input_Tokens', 0) for r in sorted_records])
    gen_out = np.array([r.get('Gen_Output_Tokens', 0) for r in sorted_records])

    x = np.arange(len(labels))
    width = 0.55

    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Vibrant presentation-friendly colors
    color_uq_in = '#FFC300'   # Vibrant Yellow
    color_uq_out = '#FF5733'  # Bright Red/Orange
    color_gen_in = '#00C9A7'  # Vibrant Teal
    color_gen_out = '#2C73D2' # Deep Blue
    
    # 4-Part Stacked bars
    p1 = ax.bar(x, uq_in, width, color=color_uq_in, edgecolor='black', label='UQ Input (Prompt)')
    p2 = ax.bar(x, uq_out, width, bottom=uq_in, color=color_uq_out, edgecolor='black', label='UQ Output (Explanation)')
    p3 = ax.bar(x, gen_in, width, bottom=uq_in+uq_out, color=color_gen_in, edgecolor='black', label='Gen Input (Evidence)')
    p4 = ax.bar(x, gen_out, width, bottom=uq_in+uq_out+gen_in, color=color_gen_out, edgecolor='black', label='Gen Output (Answer)')

    # Add centered labels for each individual sector (hiding 0s automatically)
    def label_fmt(x): return f"{int(x)}" if x > 0 else ""
    
    ax.bar_label(p1, label_type='center', fmt=label_fmt, fontsize=10, fontweight='bold', color='black')
    ax.bar_label(p2, label_type='center', fmt=label_fmt, fontsize=10, fontweight='bold', color='black')
    ax.bar_label(p3, label_type='center', fmt=label_fmt, fontsize=10, fontweight='bold', color='black')
    # White text for the dark blue top bar for better contrast
    ax.bar_label(p4, label_type='center', fmt=label_fmt, fontsize=10, fontweight='bold', color='white')

    ax.set_ylabel('Average Total Tokens per Claim', fontsize=12, fontweight='bold')
    ax.set_title(f'Token Consumption Pipeline Cost | Dataset: {dataset.upper()} ({split.capitalize()})', fontsize=16, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=11)
    
    totals = uq_in + uq_out + gen_in + gen_out
    max_tokens = max(totals) if len(totals) > 0 else 10
    ax.set_ylim(0, max_tokens * 1.3) # 30% headroom to fit the larger legend
    
    # Clean custom legend
    legend_elements = [
        mpatches.Patch(facecolor=color_uq_in, edgecolor='black', label='UQ Input (Prompt)'),
        mpatches.Patch(facecolor=color_uq_out, edgecolor='black', label='UQ Output (Thinking)'),
        mpatches.Patch(facecolor=color_gen_in, edgecolor='black', label='Gen Input (RAG Evidence)'),
        mpatches.Patch(facecolor=color_gen_out, edgecolor='black', label='Gen Output (RAG Answer)')
    ]
    ax.legend(handles=legend_elements, loc="upper left", fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Label the total height on top of the stacked bars
    for i, total in enumerate(totals):
        ax.text(i, total + (max_tokens * 0.02), f"{int(total)}", ha='center', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"✅ Token plot saved: {save_path}")

def main():
    base_dir = Path("results/archives/base/RQ1")
    gold_dir = Path("results/archives/gold/RQ1")
    current_dir = Path("results/archives/gold/RQ1")
    
    out_dir_acc = Path("vis/comparisons/accuracy")
    out_dir_tok = Path("vis/comparisons/tokens")
    out_dir_acc.mkdir(parents=True, exist_ok=True)
    out_dir_tok.mkdir(parents=True, exist_ok=True)
    
    # Data structure: experiments[(dataset, split)][method_raw_name] = data_dict
    experiments = defaultdict(lambda: defaultdict(dict))
    
    # --- 1. Mine Accuracy Metrics from Archives ---
    if base_dir.exists() and gold_dir.exists():
        for base_filepath in base_dir.rglob("*_summary.json"):
            if "calibration" in base_filepath.parts:
                continue
                
            relative_path = base_filepath.relative_to(base_dir)
            gold_filepath = gold_dir / relative_path
            
            # Parametric run won't typically have a meaningful "Gold" counterpart but 
            # we just need its base accuracy extracted.
            base_data = load_json(base_filepath)
            gold_data = load_json(gold_filepath) if gold_filepath.exists() else None
            
            if base_data:
                dataset = base_data.get('dataset', 'unknown').lower()
                split = base_data.get('split', 'unknown').lower()
                mode = base_data.get('experiment_mode', 'unknown')
                
                if mode == 'uq_aware':
                    method_raw = base_data.get("uq_settings", {}).get("method", "Unknown_UQ")
                else:
                    method_raw = mode
                
                experiments[(dataset, split)][method_raw]['Method_Raw'] = method_raw
                experiments[(dataset, split)][method_raw]['Display_Name'] = shorten_name(method_raw)
                experiments[(dataset, split)][method_raw]['Base_Acc'] = base_data.get('metrics', {}).get('balanced_accuracy', 0.0)
                
                if gold_data:
                    experiments[(dataset, split)][method_raw]['Gold_Acc'] = gold_data.get('metrics', {}).get('balanced_accuracy', 0.0)

    # --- 2. Mine Token Metrics from Current Run ---
    if current_dir.exists():
        for curr_filepath in current_dir.rglob("*_summary.json"):
            if "calibration" in curr_filepath.parts:
                continue
                
            curr_data = load_json(curr_filepath)
            if curr_data:
                dataset = curr_data.get('dataset', 'unknown').lower()
                split = curr_data.get('split', 'unknown').lower()
                mode = curr_data.get('experiment_mode', 'unknown')
                
                if mode == 'uq_aware':
                    method_raw = curr_data.get("uq_settings", {}).get("method", "Unknown_UQ")
                else:
                    method_raw = mode
                
                metrics = curr_data.get('metrics', {})
                uq_in, uq_out, gen_in, gen_out = get_fine_tokens(metrics)
                
                # Ensure identifiers exist in case the method is missing from archives
                experiments[(dataset, split)][method_raw]['Method_Raw'] = method_raw
                experiments[(dataset, split)][method_raw]['Display_Name'] = shorten_name(method_raw)
                experiments[(dataset, split)][method_raw]['UQ_Input_Tokens'] = uq_in
                experiments[(dataset, split)][method_raw]['UQ_Output_Tokens'] = uq_out
                experiments[(dataset, split)][method_raw]['Gen_Input_Tokens'] = gen_in
                experiments[(dataset, split)][method_raw]['Gen_Output_Tokens'] = gen_out

    print(f"\n--- Processing Mined Data ---")
    
    # --- 3. Generate Aggregated Plots ---
    for (dataset, split), methods_dict in experiments.items():
        records = list(methods_dict.values())
        
        # Smart Sorting: Parametric (0% RAG) -> UQ Methods (sorted by Base Acc) -> 100% RAG
        parametric = next((r for r in records if r['Method_Raw'] == 'never_retrieve'), None)
        rag = next((r for r in records if r['Method_Raw'] == 'always_retrieve'), None)
        uq_records = [r for r in records if r['Method_Raw'] not in ['never_retrieve', 'always_retrieve']]
        
        # Sort UQ methods by Base Accuracy descending (defaults to 0 if not found in archives)
        uq_records.sort(key=lambda x: x.get('Base_Acc', 0.0), reverse=True)
        
        sorted_records = []
        if parametric: sorted_records.append(parametric)
        sorted_records.extend(uq_records)
        if rag: sorted_records.append(rag)
        
        if not sorted_records:
            continue
            
        acc_save_path = out_dir_acc / f"{dataset}_{split}_accuracy_aggregation.png"
        tok_save_path = out_dir_tok / f"{dataset}_{split}_token_aggregation.png"
        
        # Filter for completeness, deliberately keeping Parametric
        acc_records = []
        for r in sorted_records:
            if r['Method_Raw'] == 'never_retrieve' and 'Base_Acc' in r:
                acc_records.append(r)
            elif r['Method_Raw'] != 'never_retrieve' and 'Base_Acc' in r and 'Gold_Acc' in r:
                acc_records.append(r)
                
        if acc_records:
            generate_accuracy_plot(dataset, split, acc_records, acc_save_path)
        
        # Keep Parametric in token comparisons AND filter for completeness
        tok_records = [r for r in sorted_records if 'UQ_Input_Tokens' in r and 'Gen_Input_Tokens' in r]
        if tok_records:
            generate_token_plot(dataset, split, tok_records, tok_save_path)

    print(f"\n✅ All dataset aggregations completed successfully.")

if __name__ == "__main__":
    main()