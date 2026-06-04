import json
import os
import sys
import argparse
from pathlib import Path

# --- Dynamic Path Resolution ---
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

def generate_markdown_summary(dataset_name: str, model_name: str, seed: int = 42):
    clean_model_name = model_name.split("/")[-1]
    calib_dir = ROOT_DIR / "run_results" / f"seed_{seed}" / dataset_name / clean_model_name / "calibration"
    
    if not calib_dir.exists():
        print(f"❌ Directory not found: {calib_dir}")
        sys.exit(1)

    # 1. Gather all optimal_threshold files
    summary_files = list(calib_dir.glob("optimal_thresholds_*.json"))
    if not summary_files:
        print(f"⚠️ No optimal_thresholds_*.json files found in {calib_dir}")
        sys.exit(0)

    print(f"🔍 Found {len(summary_files)} configuration files to summarize.")

    # 2. Extract and flatten data
    all_records = []
    for filepath in summary_files:
        # Extract the configuration name from the filename
        # e.g., "optimal_thresholds_val_mini_strict_labels.json" -> "val_mini_strict_labels"
        config_name = filepath.stem.replace("optimal_thresholds_", "")
        
        with open(filepath, "r") as f:
            try:
                data = json.load(f)
                for uq_method, metrics in data.items():
                    record = {
                        "config": config_name,
                        "uq_method": uq_method,
                        "auroc": metrics.get("auroc", 0.0),
                        "threshold": metrics.get("optimal_threshold", 0.0),
                        "coverage": metrics.get("coverage", 0.0),
                        "risk": metrics.get("empirical_risk", 0.0),
                        "tpr": metrics.get("sensitivity", 0.0),
                        "tnr": metrics.get("specificity", 0.0)
                    }
                    all_records.append(record)
            except json.JSONDecodeError:
                print(f"⚠️ Could not parse {filepath.name}")

    # Sort records primarily by AUROC (Highest first) to immediately see the winner
    all_records.sort(key=lambda x: x["auroc"], reverse=True)

    # 3. Build the Markdown Content
    md_lines = []
    md_lines.append(f"# 📊 UQ Calibration Summary")
    md_lines.append(f"**Dataset:** `{dataset_name}`  ")
    md_lines.append(f"**Model:** `{clean_model_name}`  ")
    md_lines.append(f"**Generated:** Auto-compiled from {len(summary_files)} configuration(s).\n")

    md_lines.append("## 🏆 Configuration Leaderboard")
    md_lines.append("Sorted by highest Area Under the ROC Curve (AUROC). Higher is better.\n")

    # Table Header
    md_lines.append("| AUROC | Configuration (Split + Format) | UQ Method | Opt. Threshold | Coverage | Risk | TPR (Sens) | TNR (Spec) |")
    md_lines.append("|:---:|---|---|:---:|:---:|:---:|:---:|:---:|")

    # Table Rows
    for r in all_records:
        # Format the numbers for readability
        auroc_str = f"**{r['auroc']:.4f}**" if r['auroc'] > 0.7 else f"{r['auroc']:.4f}"
        cov_str = f"{r['coverage']:.1%}"
        risk_str = f"{r['risk']:.3f}"
        tpr_str = f"{r['tpr']:.3f}"
        tnr_str = f"{r['tnr']:.3f}"
        thresh_str = f"{r['threshold']:.3f}"
        
        row = f"| {auroc_str} | `{r['config']}` | {r['uq_method']} | {thresh_str} | {cov_str} | {risk_str} | {tpr_str} | {tnr_str} |"
        md_lines.append(row)

    md_lines.append("\n---\n")
    md_lines.append("### 💡 Metric Glossary:")
    md_lines.append("* **Coverage:** The percentage of claims the model felt confident enough to answer parametrically (without external retrieval).")
    md_lines.append("* **Risk:** The actual error rate on those covered claims.")
    md_lines.append("* **TPR (Sensitivity):** Ability to correctly flag *hallucinations/errors*.")
    md_lines.append("* **TNR (Specificity):** Ability to correctly preserve *accurate* statements.")

    # 4. Save the Markdown File
    output_path = calib_dir / "CALIBRATION_SUMMARY.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"✅ Markdown summary successfully generated at: {output_path.relative_to(ROOT_DIR)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Markdown summary of calibration experiments.")
    parser.add_argument("--dataset", type=str, required=True, help="Dataset name (e.g., quantemp)")
    parser.add_argument("--model", type=str, required=True, help="Model name or path")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    
    args = parser.parse_args()
    generate_markdown_summary(args.dataset, args.model, args.seed)