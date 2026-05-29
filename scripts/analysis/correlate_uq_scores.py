import json
import argparse
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from pathlib import Path
from collections import defaultdict
from scipy.stats import spearmanr

matplotlib.use("Agg")

# --- Dynamic Path Resolution ---
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

# Short display names for readability in plots
SHORT_NAMES = {
    "MaximumSequenceProbability": "MSP",
    "Perplexity": "PPL",
    "MeanTokenEntropy": "MTE",
    "MeanPointwiseMutualInformation": "MPMI",
    "MeanConditionalPointwiseMutualInformation": "MCPMI",
    "LogicalContradiction": "LogicTrap",
    "SemanticEntropy": "SE",
    "RenyiNeg": "RenyiNeg",
    "Ensemble": "Ensemble",
}


def shorten(name: str) -> str:
    return SHORT_NAMES.get(name, name)


def load_method_scores(jsonl_path: Path, method_name: str) -> dict:
    """
    Load an evaluation JSONL and return {sample_id: uncertainty_score}.
    Each eval file has one UQ method's score per sample.
    """
    scores = {}
    with open(jsonl_path, "r") as f:
        for line in f:
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            sample_id = d.get("id")
            if sample_id is None:
                continue
            uq = d.get("uq_scores", {})
            val = uq.get(method_name, d.get("uncertainty_score"))
            if val is not None:
                scores[str(sample_id)] = float(val)
    return scores


def merge_eval_scores(
    uq_aware_dir: Path, result_filename: str, exclude_set: set
) -> pd.DataFrame:
    """
    Walk uq_aware/{method}/ subdirectories, find matching JSONL files by filename,
    and merge scores into a single DataFrame (samples × methods) by ID.
    """
    method_scores = {}

    for method_dir in sorted(uq_aware_dir.iterdir()):
        if not method_dir.is_dir():
            continue
        method_name = method_dir.name
        if method_name in exclude_set:
            continue

        jsonl_path = method_dir / result_filename
        if not jsonl_path.exists():
            continue

        scores = load_method_scores(jsonl_path, method_name)
        if scores:
            method_scores[method_name] = scores

    if len(method_scores) < 2:
        return pd.DataFrame()

    # Merge by sample ID
    df = pd.DataFrame(method_scores)
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    return df


def compute_spearman_matrix(df: pd.DataFrame):
    """Compute pairwise Spearman rank correlations, returning (rho_matrix, p_matrix) as DataFrames."""
    methods = df.columns.tolist()
    n = len(methods)
    rho_mat = np.ones((n, n))
    p_mat = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            pair = df[[methods[i], methods[j]]].dropna()
            if len(pair) < 3:
                rho_mat[i, j] = rho_mat[j, i] = np.nan
                p_mat[i, j] = p_mat[j, i] = np.nan
            else:
                rho, p = spearmanr(pair[methods[i]], pair[methods[j]])
                rho_mat[i, j] = rho_mat[j, i] = rho
                p_mat[i, j] = p_mat[j, i] = p

    return (
        pd.DataFrame(rho_mat, index=methods, columns=methods),
        pd.DataFrame(p_mat, index=methods, columns=methods),
    )


def plot_correlation_heatmap(
    rho_df: pd.DataFrame,
    p_df: pd.DataFrame,
    title: str,
    save_path: Path,
    figsize=(9, 7.5),
):
    """
    Render a publication-quality Spearman correlation heatmap.
    Cells with p >= 0.05 are marked with 'ns' (not significant).
    """
    display_names = [shorten(c) for c in rho_df.columns]
    plot_rho = rho_df.copy()
    plot_rho.index = display_names
    plot_rho.columns = display_names

    fig, ax = plt.subplots(figsize=figsize)

    annot = rho_df.copy()
    annot_labels = annot.map(lambda x: f"{x:.2f}")
    for i in range(len(rho_df)):
        for j in range(len(rho_df)):
            if i != j and p_df.iloc[i, j] >= 0.05:
                annot_labels.iloc[i, j] += "\n(ns)"

    annot_labels.index = display_names
    annot_labels.columns = display_names

    sns.heatmap(
        plot_rho,
        annot=annot_labels,
        fmt="",
        cmap="RdBu_r",
        center=0,
        vmin=-1,
        vmax=1,
        linewidths=0.8,
        linecolor="white",
        square=True,
        cbar_kws={"shrink": 0.75, "label": "Spearman ρ"},
        ax=ax,
        annot_kws={"fontsize": 9},
    )

    ax.set_title(title, fontsize=13, fontweight="bold", pad=14)
    ax.tick_params(axis="both", labelsize=10)
    plt.tight_layout()
    save_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  📊 Saved: {save_path.relative_to(ROOT_DIR)}")


def discover_eval_configs(
    results_root: Path,
    dataset_filter: str = None,
    model_filter: str = None,
    exclude_set: set = None,
):
    """
    Auto-discover all (dataset, model, result_filename) combinations from
    results_root/{dataset}/{model}/uq_aware/{method}/results_*.jsonl.
    Groups by result filename so that methods sharing the same file are merged.
    """
    if exclude_set is None:
        exclude_set = set()

    configs = []
    for dataset_dir in sorted(results_root.iterdir()):
        if not dataset_dir.is_dir():
            continue
        if dataset_filter and dataset_dir.name != dataset_filter:
            continue

        for model_dir in sorted(dataset_dir.iterdir()):
            if not model_dir.is_dir():
                continue
            if model_filter and model_dir.name != model_filter:
                continue

            uq_aware_dir = model_dir / "uq_aware"
            if not uq_aware_dir.exists():
                continue

            # Collect all unique result filenames across non-excluded method dirs
            result_files = set()
            for method_dir in uq_aware_dir.iterdir():
                if not method_dir.is_dir() or method_dir.name in exclude_set:
                    continue
                for jsonl in method_dir.glob("results_*.jsonl"):
                    # Skip summary files
                    if "_summary" in jsonl.name:
                        continue
                    result_files.add(jsonl.name)

            for result_filename in sorted(result_files):
                configs.append(
                    {
                        "dataset": dataset_dir.name,
                        "model": model_dir.name,
                        "result_filename": result_filename,
                        "uq_aware_dir": uq_aware_dir,
                    }
                )
    return configs


def main():
    parser = argparse.ArgumentParser(
        description="Pairwise Spearman correlation analysis of UQ method scores from evaluation results"
    )
    parser.add_argument(
        "--results_root",
        type=str,
        default="results_dump/final",
        help="Root directory containing dataset/model results",
    )
    parser.add_argument("--dataset", type=str, default=None, help="Filter by dataset")
    parser.add_argument("--model", type=str, default=None, help="Filter by model")
    parser.add_argument(
        "--output_dir",
        type=str,
        default="visualizations/uq_correlations",
        help="Output directory for plots and CSV",
    )
    parser.add_argument(
        "--exclude",
        type=str,
        nargs="*",
        default=["SemanticEntropy", "LogicalContradiction"],
        help="UQ methods to exclude (default: Ensemble, LogicalContradiction)",
    )
    args = parser.parse_args()

    results_root = ROOT_DIR / args.results_root
    output_dir = ROOT_DIR / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    if not results_root.exists():
        print(f"❌ Results root not found: {results_root}")
        sys.exit(1)

    exclude_set = set(args.exclude) if args.exclude else set()

    configs = discover_eval_configs(results_root, args.dataset, args.model, exclude_set)
    if not configs:
        print("❌ No evaluation results found.")
        sys.exit(1)

    print(f"🔍 Auto-discovered {len(configs)} (dataset, model, file) configuration(s).")
    print(f"🚫 Excluding: {exclude_set}\n")

    all_correlation_records = []
    # Key: (dataset, result_filename) -> list of per-model results
    aggregation_groups = defaultdict(list)

    # ========================================================================
    # PER-(DATASET, MODEL, FILE): Merge across methods and compute correlations
    # ========================================================================
    for entry in configs:
        dataset = entry["dataset"]
        model = entry["model"]
        result_filename = entry["result_filename"]
        uq_aware_dir = entry["uq_aware_dir"]

        # Derive a clean label from the filename (e.g. "train_label_only_logic_OFF")
        config_label = result_filename.replace("results_", "").replace(".jsonl", "")

        print(f"📂 {dataset} / {model} / {config_label}")

        df = merge_eval_scores(uq_aware_dir, result_filename, exclude_set)
        if df.empty:
            print("   ⚠️  Fewer than 2 UQ methods with matching results, skipping.")
            continue

        methods = df.columns.tolist()
        print(
            f"   ✅ {len(df)} samples × {len(methods)} methods: "
            f"{[shorten(m) for m in methods]}"
        )

        rho_df, p_df = compute_spearman_matrix(df)

        # Save individual heatmap
        title = (
            f"UQ Score Correlations (Spearman ρ)\n"
            f"{dataset} · {model} · {config_label}"
        )

        save_dir = Path("visualizations/uq_correlations")
        plot_path = (
            ROOT_DIR / save_dir / dataset / model / f"correlation_heatmap_{config_label}.png"
        )
        plot_correlation_heatmap(rho_df, p_df, title, plot_path)

        # Collect for cross-model aggregation
        aggregation_groups[(dataset, config_label)].append(
            {"model": model, "rho": rho_df, "p": p_df}
        )

        # Record to CSV
        for i, m1 in enumerate(rho_df.columns):
            for j, m2 in enumerate(rho_df.columns):
                if j <= i:
                    continue
                all_correlation_records.append(
                    {
                        "dataset": dataset,
                        "model": model,
                        "config": config_label,
                        "method_1": m1,
                        "method_2": m2,
                        "spearman_rho": rho_df.iloc[i, j],
                        "p_value": p_df.iloc[i, j],
                    }
                )

    # ========================================================================
    # AGGREGATED: Cross-model average correlation per (dataset, config)
    # ========================================================================
    print(f"\n{'='*60}")
    print("📊 Generating aggregated cross-model heatmaps...")
    print(f"{'='*60}")

    for (dataset, config_label), entries in aggregation_groups.items():
        if len(entries) < 1:
            continue

        # Find common methods across all models
        common_methods = None
        for e in entries:
            methods_set = set(e["rho"].columns)
            common_methods = (
                methods_set if common_methods is None else common_methods & methods_set
            )
        common_methods = sorted(common_methods)

        if len(common_methods) < 2:
            print(f"   ⚠️  {dataset}/{config_label}: Fewer than 2 common methods, skipping.")
            continue

        # Average rho across models
        stacked = np.stack(
            [e["rho"].loc[common_methods, common_methods].values for e in entries]
        )
        avg_rho = pd.DataFrame(
            np.nanmean(stacked, axis=0), index=common_methods, columns=common_methods
        )

        # Conservative: report max p-value across models
        stacked_p = np.stack(
            [e["p"].loc[common_methods, common_methods].values for e in entries]
        )
        max_p = pd.DataFrame(
            np.nanmax(stacked_p, axis=0), index=common_methods, columns=common_methods
        )

        title = (
            f"Avg. UQ Score Correlations (Spearman ρ)\n"
            f"{dataset} · {config_label}\n"
            f"Averaged across {len(entries)} model(s)"
        )
        plot_path = output_dir / dataset / f"correlation_heatmap_avg_{config_label}.png"
        plot_correlation_heatmap(avg_rho, max_p, title, plot_path, figsize=(9, 8))

    # ========================================================================
    # SAVE CSV
    # ========================================================================
    if all_correlation_records:
        csv_df = pd.DataFrame(all_correlation_records)
        csv_path = output_dir / "pairwise_correlations.csv"
        csv_df.to_csv(csv_path, index=False)
        print(
            f"\n📄 Full pairwise correlation data saved to: {csv_path.relative_to(ROOT_DIR)}"
        )

    print(f"\n{'='*60}")
    print(f"✅ Correlation analysis complete. Outputs in: {output_dir.relative_to(ROOT_DIR)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
