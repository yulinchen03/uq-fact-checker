import json
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter

# Force non-interactive backend for headless cluster environments
matplotlib.use("Agg")

def load_claims(file_path):
    """Smart loader that handles JSON Arrays and JSONL automatically."""
    print(f"Reading {os.path.basename(file_path)}...")
    
    if not os.path.exists(file_path):
        print(f"  ❌ File not found: {file_path}")
        return []

    data = []
    # Attempt 1: Standard JSON Array
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            parsed = json.load(f)
            if isinstance(parsed, list):
                print("  ✅ Detected standard JSON array format.")
                return parsed
    except json.JSONDecodeError:
        pass # Fall through to Attempt 2
        
    # Attempt 2: JSONL (JSON Lines)
    print("  ✅ Detected JSONL (JSON Lines) format.")
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    return data

def extract_gold_counts(dataset):
    """
    Robustly extracts the number of gold documents per claim.
    Handles SciFact's nested dictionary format, standard lists, and QuanTemp monolithic docs.
    """
    counts = []
    for item in dataset:
        gold_len = 0
        
        # Method 1: 'evidence' key (SciFact format: dict of doc_ids, or standard list)
        if "evidence" in item and item["evidence"]:
            ev = item["evidence"]
            if isinstance(ev, dict):
                gold_len = len(ev.keys())
            elif isinstance(ev, list):
                gold_len = len(ev)
                
        # Method 2: 'cited_doc_ids' key
        elif "cited_doc_ids" in item and item["cited_doc_ids"]:
            gold_len = len(item["cited_doc_ids"])
            
        # Method 3: 'doc_ids' key
        elif "doc_ids" in item and item["doc_ids"]:
            gold_len = len(item["doc_ids"])
            
        # Method 4: 'doc' key (QuanTemp format: single monolithic text block attached to claim)
        elif "doc" in item and item["doc"]:
            gold_len = 1
            
        counts.append(gold_len)
        
    return np.array(counts)

def print_statistics(dataset_name, counts):
    """Prints a clean statistical breakdown to the console."""
    if len(counts) == 0:
        return

    # Filter out claims with 0 evidence (if any exist) as they are usually skipped in eval
    valid_counts = counts[counts > 0]
    zero_count = len(counts) - len(valid_counts)
    
    print(f"\n" + "="*50)
    print(f"📊 Statistics for {dataset_name.upper()}")
    print("="*50)
    print(f"Total Claims Analyzed: {len(counts)}")
    if zero_count > 0:
        print(f"⚠️ Claims with ZERO gold evidence: {zero_count} (Ignored in stats below)")
        
    if len(valid_counts) == 0:
        print("❌ No valid gold evidence found to calculate statistics. Skipping.")
        print("="*50 + "\n")
        return
        
    if "quantemp" in dataset_name.lower():
        print("ℹ️ Note: QuanTemp uses monolithic documents. Each claim maps to 1 parent doc,")
        print("   but these may be split into multiple chunks in your vector database.")
    
    print(f"\n--- Metrics ---")
    print(f"Mean gold docs per claim:   {np.mean(valid_counts):.2f}")
    print(f"Median gold docs per claim: {np.median(valid_counts):.1f}")
    print(f"Max gold docs for a claim:  {np.max(valid_counts)}")
    print(f"95th Percentile:            {np.percentile(valid_counts, 95):.0f}")
    print(f"99th Percentile:            {np.percentile(valid_counts, 99):.0f}")
    
    print(f"\n--- Frequency Breakdown ---")
    freq = Counter(valid_counts)
    for num_docs in sorted(freq.keys()):
        count = freq[num_docs]
        percentage = (count / len(valid_counts)) * 100
        print(f"Claims with exactly {num_docs} gold doc(s): {count:<4} ({percentage:.1f}%)")
    print("="*50 + "\n")

def plot_distributions(all_counts, save_path="data/gold_evidence_distribution.png"):
    """Creates a comparative bar chart showing the distribution of gold docs."""
    datasets = list(all_counts.keys())
    if not datasets:
        return
        
    # Find the maximum number of gold documents across all datasets to set the X-axis
    max_val = max([np.max(counts) for counts in all_counts.values() if len(counts[counts > 0]) > 0], default=0)
    
    if max_val == 0:
        print("⚠️ Not enough valid data to generate a plot.")
        return
        
    x_labels = np.arange(1, max_val + 1)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bar_width = 0.35
    colors = ["#1F77B4", "#FF7F0E"] # Blue and Orange
    
    for idx, (name, counts) in enumerate(all_counts.items()):
        if len(counts) == 0:
            continue
            
        valid_counts = counts[counts > 0]
        if len(valid_counts) == 0:
            continue
            
        freq = Counter(valid_counts)
        
        # Calculate percentages for the Y-axis instead of raw counts for fair comparison
        percentages = [(freq.get(i, 0) / len(valid_counts)) * 100 for i in x_labels]
        
        # Offset bars so they sit side-by-side
        x_positions = x_labels + (idx * bar_width) - (bar_width / 2 if len(all_counts) > 1 else 0)
        
        bars = ax.bar(x_positions, percentages, bar_width, label=name.capitalize(), 
                      color=colors[idx % len(colors)], edgecolor="black", alpha=0.85)
        
        # Add the percentage labels on top of the bars
        for bar, pct in zip(bars, percentages):
            if pct > 0:
                ax.text(bar.get_x() + bar.get_width()/2, pct + 1, 
                        f"{pct:.1f}%", ha='center', va='bottom', fontsize=9)

    ax.set_xlabel('Number of Gold Documents Required (Parent IDs)', fontsize=12)
    ax.set_ylabel('Percentage of Claims (%)', fontsize=12)
    ax.set_title('Gold Evidence Density: SciFact vs QuanTemp', fontsize=14, pad=15, fontweight='bold')
    
    ax.set_xticks(x_labels + (bar_width / 2 if len(all_counts) > 1 else 0))
    ax.set_xticklabels([str(int(x)) for x in x_labels])
    
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.legend(fontsize=12, frameon=False)
    
    plt.tight_layout()
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    print(f"📈 Comparative plot saved to: {save_path}")
    plt.close()

def main():
    # Define your dataset paths here
    dataset_paths = {
        "scifact": "data/scifact/claims_val.jsonl",
        "quantemp": "data/quantemp/claims_val.json" # Adjust this path if needed
    }
    
    all_counts = {}
    
    for name, path in dataset_paths.items():
        data = load_claims(path)
        if data:
            counts = extract_gold_counts(data)
            all_counts[name] = counts
            print_statistics(name, counts)
            
    if all_counts:
        plot_distributions(all_counts)

if __name__ == "__main__":
    main()