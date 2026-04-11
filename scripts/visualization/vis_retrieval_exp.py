import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
from pathlib import Path
import argparse
import sys

# Force non-interactive backend
matplotlib.use("Agg")

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

def parse_args():
    parser = argparse.ArgumentParser(description="Visualize retrieval experiment results")
    
    # Optional K override. If omitted, the script grabs the max K from the JSON
    parser.add_argument("--top-k", "-k", type=int, default=None,
                        help="Number of final documents returned to plot (e.g., 1, 2, or 3)")
    
    # Matches the benchmark script's routing
    parser.add_argument("--save-results-folder", type=str, default="default",
                        help="Folder inside results/benchmarks/ where the JSON is located")
    
    return parser.parse_args()

# ── 1. Clean, Paired Tech Palette (With Baseline) ──
CATEGORY_COLORS = {
    "Baseline (BGE-M3)": "#95A5A6",    # Slate Gray (Control Group)
    "Dense": "#5DADE2",                # Light Blue
    "Dense + Reranking": "#2874A6",    # Dark Blue
    "Sparse": "#F5B041",               # Light Orange
    "Sparse + Reranking": "#B9770E",   # Dark Orange
    "Hybrid": "#58D68D",               # Light Green
    "Hybrid + Reranking": "#1D8348"    # Dark Green
}

def get_category(method_name: str) -> str:
    """Categorize the method based on its name."""
    name = method_name.lower()
    
    if "gold" in name:
        return "Gold"
        
    has_reranker = "reranker" in name

    # Intercept the exact BGE-M3 dense model to act as our isolated baseline
    if "dense" in name and "bge-m3" in name and not has_reranker:
        return "Baseline (BGE-M3)"
    
    if "dense" in name:
        return "Dense + Reranking" if has_reranker else "Dense"
    elif "sparse" in name:
        return "Sparse + Reranking" if has_reranker else "Sparse"
    elif "hybrid" in name:
        return "Hybrid + Reranking" if has_reranker else "Hybrid"
    
    return "Other"

def clean_model_name(name: str) -> str:
    """Removes the numeric prefixes (e.g., '14. ') for a cleaner legend."""
    return name.split(". ", 1)[-1] if ". " in name else name

def main():
    args = parse_args()

    # --- FIXED: Use dynamic pathing to locate the results folder ---
    json_path = project_root / "results" / "benchmarks" / args.save_results_folder / "retrieval_exp.json"
    
    if not json_path.exists():
        print(f"❌ Error: Could not find {json_path.relative_to(project_root)}")
        return

    with open(json_path, "r") as f:
        data = json.load(f)

    methods_data = data.get("methods", {})
    if not methods_data:
        print("❌ Error: No methods found in JSON.")
        return

    # --- FIXED: Handle multiple K values dynamically ---
    available_ks = data.get("top_k", [3])
    if not isinstance(available_ks, list):
        available_ks = [available_ks]
        
    # User override, otherwise plot the max K available
    PLOT_K = args.top_k if args.top_k is not None else max(available_ks)
    
    if PLOT_K not in available_ks:
        print(f"⚠️ Warning: top-k {PLOT_K} not found in the JSON. Falling back to {max(available_ks)}")
        PLOT_K = max(available_ks)

    metrics = {
        f"hit@{PLOT_K}": f"Hit Rate@{PLOT_K}",
        f"recall@{PLOT_K}": f"Recall@{PLOT_K}",
        f"precision@{PLOT_K}": f"Precision@{PLOT_K}",
        f"mrr@{PLOT_K}": f"MRR@{PLOT_K}",
    }

    out_dir = json_path.parent
    base_name = f"retrieval_exp_dashboard_k{PLOT_K}.png"

    print(f"📊 Building Best-in-Category dashboard (K={PLOT_K}) for {args.save_results_folder}...")

    # Set consistent ordering for the X-axis (Baseline pinned to the far left)
    cat_order = list(CATEGORY_COLORS.keys())

    # Map to track WHICH model actually won each category
    best_models_map = {}

    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(24, 14))
    axes = axes.flatten()

    # ── 2. Generate Quality Plots (Axes 0 to 3) ──
    for idx, (metric_key, metric_title) in enumerate(metrics.items()):
        ax = axes[idx]
        
        # Group methods
        categorized_scores = {k: [] for k in CATEGORY_COLORS.keys()}
        
        for method_name, metrics_dict in methods_data.items():
            category = get_category(method_name)
            if category in categorized_scores:
                score = metrics_dict.get(metric_key, 0.0)
                categorized_scores[category].append((method_name, score))

        # Extract only the #1 Best per category
        top_methods = []
        for category, items in categorized_scores.items():
            if not items:
                continue 
            
            items.sort(key=lambda x: x[1], reverse=True)
            top_method_name, top_score = items[0]
            top_methods.append((category, top_score))
            
            # Save the winning method name
            if metric_key == f"hit@{PLOT_K}":
                best_models_map[category] = top_method_name

        # Sort strictly by the predefined category order
        top_methods.sort(key=lambda x: cat_order.index(x[0]))
        
        plot_categories = [m[0] for m in top_methods]
        plot_scores = [m[1] for m in top_methods]
        colors = [CATEGORY_COLORS[cat] for cat in plot_categories]

        if not plot_categories:
            continue

        bars = ax.bar(plot_categories, plot_scores, color=colors, edgecolor="black", alpha=0.9)

        # Add value labels
        for bar, val in zip(bars, plot_scores):
            ax.text(bar.get_x() + bar.get_width()/2, val + 0.01, 
                    f"{val:.3f}", ha='center', va='bottom', fontsize=11)

        ax.set_ylabel("Score", fontsize=12)
        ax.set_title(f"Best in Category: {metric_title}", fontsize=15, pad=12, fontweight='bold')
        
        max_score = max(plot_scores) if plot_scores else 1.0
        ax.set_ylim(0, max_score * 1.25) 
        
        ax.grid(axis="y", linestyle="--", alpha=0.7)
        ax.spines[['top', 'right']].set_visible(False)
        
        ax.set_xticks(range(len(plot_categories)))
        ax.set_xticklabels(plot_categories, rotation=35, ha="right", fontsize=11)

    # ── 3. Generate Latency Plot (Axis 4) ──
    ax_lat = axes[4]
    latency_data = []
    
    for cat in cat_order:
        if cat in best_models_map:
            method_name = best_models_map[cat]
            lat = methods_data[method_name].get("avg_latency_seconds", 0)
            if lat > 0:
                latency_data.append((cat, lat))

    if latency_data:
        plot_categories = [d[0] for d in latency_data]
        plot_lats = [d[1] for d in latency_data]
        lat_colors = [CATEGORY_COLORS[cat] for cat in plot_categories]

        bars = ax_lat.bar(plot_categories, plot_lats, color=lat_colors, edgecolor="black", alpha=0.9)

        max_lat = max(plot_lats) if plot_lats else 1.0
        ax_lat.set_ylim(0, max_lat * 1.25)

        for bar, val in zip(bars, plot_lats):
            ax_lat.text(bar.get_x() + bar.get_width()/2, val + (max_lat * 0.01), 
                        f"{val:.2f}s", ha='center', va='bottom', fontsize=11)

        ax_lat.set_ylabel("Average Latency (Seconds)", fontsize=12)
        ax_lat.set_title("Average Latency of Category Winners", fontsize=15, pad=12, fontweight='bold')
        ax_lat.grid(axis="y", linestyle="--", alpha=0.7)
        ax_lat.spines[['top', 'right']].set_visible(False)
        ax_lat.set_xticks(range(len(plot_categories)))
        ax_lat.set_xticklabels(plot_categories, rotation=35, ha="right", fontsize=11)

    # ── 4. Add the Smart Legend (Axis 5) ──
    ax_leg = axes[5]
    ax_leg.axis('off') 
    
    legend_patches = []
    for cat in cat_order:
        if cat in best_models_map:
            winning_config = clean_model_name(best_models_map[cat])
            # For the baseline, we don't need it to redundantly say "Winner:"
            if cat == "Baseline (BGE-M3)":
                label_text = f"Baseline\nPipeline: {winning_config}"
            else:
                label_text = f"{cat}\nWinner: {winning_config}"
                
            legend_patches.append(mpatches.Patch(color=CATEGORY_COLORS[cat], label=label_text, ec="black"))
    
    ax_leg.legend(
        handles=legend_patches, 
        loc="center", 
        title="Evaluated Configurations",
        title_fontsize=18,
        fontsize=12,
        frameon=False,
        labelspacing=1.8
    )

    # ── 5. Save the Master Figure ──
    plt.tight_layout()
    plt.subplots_adjust(top=0.92, hspace=0.35, wspace=0.2) 
    
    out_file = out_dir / base_name
    plt.savefig(out_file, dpi=300, bbox_inches="tight")
    print(f"  ✅ Saved clean dashboard with baseline: {out_file.relative_to(project_root)}")
    plt.close(fig)

if __name__ == "__main__":
    main()