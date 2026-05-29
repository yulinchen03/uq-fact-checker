"""
Post-Evaluation SHAP Analysis for Ensemble UQ Models.

Loads the saved ensemble model bundle (LogisticRegression + StandardScaler)
and evaluation results from uq_aware/Ensemble/ directories, then computes
SHAP values on the held-out evaluation data.

Produces per (dataset, model, config):
  1. SHAP bar plot (mean |SHAP|)
  2. SHAP beeswarm plot (per-sample feature impact)
  3. JSON summary of SHAP importance values

Auto-discovers all available Ensemble evaluation results.

Usage:
    python scripts/analysis/shap_eval_analysis.py
    python scripts/analysis/shap_eval_analysis.py --results_root results_dump/green_light
    python scripts/analysis/shap_eval_analysis.py --dataset scifact --model gemma-3-12b-it
"""

import json
import argparse
import sys
import pickle
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import shap
from pathlib import Path
from collections import defaultdict

matplotlib.use("Agg")

# --- Dynamic Path Resolution ---
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

# Short display names
SHORT_NAMES = {
    "MaximumSequenceProbability": "MSP",
    "Perplexity": "PPL",
    "MeanTokenEntropy": "MTE",
    "MeanPointwiseMutualInformation": "MPMI",
    "MeanConditionalPointwiseMutualInformation": "MCPMI",
    "LogicalContradiction": "LogicTrap",
    "SemanticEntropy": "SE",
    "Ensemble": "Ensemble",
}


def shorten(name: str) -> str:
    return SHORT_NAMES.get(name, name)


def clean_label(label: str) -> str:
    lbl = str(label).upper().replace(".", "").replace("_", " ")
    return " ".join(lbl.split())


def load_ensemble_bundle(bundle_path: Path) -> dict:
    """Load a saved ensemble model bundle (.pkl)."""
    with open(bundle_path, "rb") as f:
        return pickle.load(f)


def load_eval_data(jsonl_path: Path, features: list, max_finite_replacements: dict, dataset_name: str):
    """
    Load Ensemble evaluation JSONL, extract feature matrix and error labels.
    Mirrors the same data prep logic used in ensembler.py.
    Returns: (X_raw, y_errors, n_total, n_excluded)
    """
    allowed_labels = (
        ["TRUE", "FALSE", "CONFLICTING"]
        if dataset_name.lower() == "quantemp"
        else ["SUPPORT", "CONTRADICT", "NOT ENOUGH INFO"]
    )

    X_list, y_list = [], []
    n_total, n_excluded = 0, 0

    with open(jsonl_path, "r") as f:
        for line in f:
            n_total += 1
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                n_excluded += 1
                continue

            gold = clean_label(d.get("gold_label", "NOT ENOUGH INFO"))
            para = clean_label(d.get("parametric_verdict", "NOT ENOUGH INFO"))

            if para not in allowed_labels:
                n_excluded += 1
                continue

            uq_scores = d.get("uq_scores", {})
            feat = []
            for method in features:
                val = uq_scores.get(method)
                if val is None or not isinstance(val, (int, float)) or np.isnan(val):
                    feat.append(np.inf)
                else:
                    feat.append(float(val))
            X_list.append(feat)
            y_list.append(1 if gold != para else 0)

    if not X_list:
        return None, None, n_total, n_excluded

    X_raw = np.array(X_list)

    # Replace inf with max_finite_replacements (same logic as ensembler)
    for j, method in enumerate(features):
        col = X_raw[:, j]
        inf_mask = ~np.isfinite(col)
        replacement = max_finite_replacements.get(method, 0.0)
        X_raw[inf_mask, j] = replacement

    return X_raw, np.array(y_list), n_total, n_excluded


def compute_and_plot_shap(
    bundle: dict,
    X_raw: np.ndarray,
    y_errors: np.ndarray,
    features: list,
    title_prefix: str,
    output_dir: Path,
    filename_suffix: str,
):
    """
    Compute SHAP values for the ensemble model on evaluation data and generate plots.
    Mirrors the SHAP logic in ensembler.py train_final_model().
    """
    scaler = bundle["scaler"]
    model = bundle["model"]

    # Scale the eval data using the calibration-fitted scaler
    X_scaled = scaler.transform(X_raw)

    # Compute SHAP values
    explainer = shap.Explainer(model, X_scaled, feature_names=features)
    explanation = explainer(X_scaled)
    shap_values = explanation.values  # (n_samples, n_features)

    # Summary statistics
    mean_abs_shap = np.abs(shap_values).mean(axis=0)
    mean_signed_shap = shap_values.mean(axis=0)
    total_shap = float(mean_abs_shap.sum())
    shap_share = mean_abs_shap / total_shap if total_shap > 0 else np.zeros_like(mean_abs_shap)

    # Build JSON summary
    shap_summary = {}
    for j, feat in enumerate(features):
        shap_summary[feat] = {
            "shap_mean_abs": float(mean_abs_shap[j]),
            "shap_mean_signed": float(mean_signed_shap[j]),
            "shap_share": float(shap_share[j]),
        }

    # Save JSON
    json_path = output_dir / f"shap_eval_{filename_suffix}.json"
    with open(json_path, "w") as f:
        json.dump(shap_summary, f, indent=2)
    print(f"   📄 SHAP summary: {json_path.relative_to(ROOT_DIR)}")

    # Build display explanation with raw (unscaled) feature values for beeswarm
    display_explanation = shap.Explanation(
        values=explanation.values,
        base_values=explanation.base_values,
        data=X_raw,
        feature_names=features,
    )

    # --- Bar plot ---
    plt.figure()
    shap.plots.bar(display_explanation, max_display=len(features), show=False)
    plt.title(f"{title_prefix}\nMean |SHAP| (Eval Data)", fontsize=11, fontweight="bold")
    bar_path = output_dir / f"shap_bar_eval_{filename_suffix}.png"
    plt.savefig(bar_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"   📊 Bar plot: {bar_path.relative_to(ROOT_DIR)}")

    # --- Beeswarm plot ---
    plt.figure()
    shap.plots.beeswarm(display_explanation, max_display=len(features), show=False)
    plt.title(f"{title_prefix}\nSHAP Beeswarm (Eval Data)", fontsize=11, fontweight="bold")
    beeswarm_path = output_dir / f"shap_beeswarm_eval_{filename_suffix}.png"
    plt.savefig(beeswarm_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"   📊 Beeswarm: {beeswarm_path.relative_to(ROOT_DIR)}")

    return shap_summary


def discover_ensemble_eval_configs(
    results_root: Path,
    dataset_filter: str = None,
    model_filter: str = None,
):
    """
    Auto-discover (dataset, model, eval_file, bundle_path) combinations where
    Ensemble eval results exist alongside a trained model bundle.
    """
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

            ensemble_dir = model_dir / "uq_aware" / "Ensemble"
            calib_dir = model_dir / "calibration"
            if not ensemble_dir.exists() or not calib_dir.exists():
                continue

            # Find all Ensemble eval JSONL files
            for jsonl in sorted(ensemble_dir.glob("results_*.jsonl")):
                if "_summary" in jsonl.name:
                    continue

                # Derive the config suffix to find the matching bundle
                # e.g. results_train_label_only_logic_OFF.jsonl ->
                #   split=train, config=label_only_logic_OFF
                stem = jsonl.stem.replace("results_", "")  # train_label_only_logic_OFF
                parts = stem.split("_", 1)  # ['train', 'label_only_logic_OFF']
                if len(parts) < 2:
                    continue

                eval_split = parts[0]
                config_suffix = parts[1]  # label_only_logic_OFF

                # The bundle was trained on 'val' split during calibration
                # Bundle naming: ensemble_model_bundle_val_{config_suffix}.pkl
                bundle_path = calib_dir / f"ensemble_model_bundle_val_{config_suffix}.pkl"
                if not bundle_path.exists():
                    # Try the exact split name as fallback
                    bundle_path = calib_dir / f"ensemble_model_bundle_{eval_split}_{config_suffix}.pkl"
                    if not bundle_path.exists():
                        continue

                configs.append({
                    "dataset": dataset_dir.name,
                    "model": model_dir.name,
                    "eval_split": eval_split,
                    "config_suffix": config_suffix,
                    "eval_path": jsonl,
                    "bundle_path": bundle_path,
                })
    return configs


def main():
    parser = argparse.ArgumentParser(
        description="Post-evaluation SHAP analysis for ensemble UQ models"
    )
    parser.add_argument(
        "--results_root",
        type=str,
        default="results_dump/green_light",
        help="Root directory containing dataset/model results",
    )
    parser.add_argument("--dataset", type=str, default=None, help="Filter by dataset")
    parser.add_argument("--model", type=str, default=None, help="Filter by model")
    parser.add_argument(
        "--output_dir",
        type=str,
        default="visualizations/shap_eval",
        help="Output directory for SHAP plots and JSON summaries",
    )
    args = parser.parse_args()

    results_root = ROOT_DIR / args.results_root
    output_dir = ROOT_DIR / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    if not results_root.exists():
        print(f"❌ Results root not found: {results_root}")
        sys.exit(1)

    configs = discover_ensemble_eval_configs(results_root, args.dataset, args.model)
    if not configs:
        print("❌ No Ensemble evaluation results with matching model bundles found.")
        sys.exit(1)

    print(f"🔍 Discovered {len(configs)} Ensemble eval configuration(s).\n")

    for entry in configs:
        dataset = entry["dataset"]
        model = entry["model"]
        eval_split = entry["eval_split"]
        config_suffix = entry["config_suffix"]
        eval_path = entry["eval_path"]
        bundle_path = entry["bundle_path"]

        config_label = f"{eval_split}_{config_suffix}"
        print(f"{'='*60}")
        print(f"📂 {dataset} / {model} / {config_label}")
        print(f"   Bundle: {bundle_path.relative_to(ROOT_DIR)}")
        print(f"   Eval:   {eval_path.relative_to(ROOT_DIR)}")

        # Load model bundle
        bundle = load_ensemble_bundle(bundle_path)
        features = bundle["features"]
        max_finite_replacements = bundle["max_finite_replacements"]

        # Load eval data
        X_raw, y_errors, n_total, n_excluded = load_eval_data(
            eval_path, features, max_finite_replacements, dataset
        )

        if X_raw is None or len(X_raw) == 0:
            print("   ⚠️  No valid evaluation data, skipping.")
            continue

        print(f"   ✅ {len(X_raw)} valid samples ({n_excluded} excluded)")
        print(f"   📊 Error rate: {y_errors.mean():.2%} ({y_errors.sum()}/{len(y_errors)})")
        print(f"   🔧 Features: {[shorten(f) for f in features]}")

        # Compute SHAP and generate plots
        plot_dir = output_dir / dataset / model
        plot_dir.mkdir(parents=True, exist_ok=True)

        title_prefix = f"{dataset} · {model}\n{config_label}"
        compute_and_plot_shap(
            bundle=bundle,
            X_raw=X_raw,
            y_errors=y_errors,
            features=features,
            title_prefix=title_prefix,
            output_dir=plot_dir,
            filename_suffix=config_label,
        )

        print()

    print(f"{'='*60}")
    print(f"✅ Post-evaluation SHAP analysis complete. Outputs in: {output_dir.relative_to(ROOT_DIR)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
