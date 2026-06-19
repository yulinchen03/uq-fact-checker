"""
Qualitative analysis

For each dataset/model pair, across all UQ-aware configurations (excluding
LogicalContradiction), identifies claims that were:
  1. Wrong in ALL configurations across ALL models (predicted_verdict != gold_label)

Output:
  - Always Wrong (claims wrong everywhere)
  - Wrong Label Distribution (summary of gold labels for these claims)
"""

import json
from pathlib import Path

import pandas as pd


# ── Configuration ──────────────────────────────────────────────────────────
BASE_DIR = Path("results_dump/temp0.3")
SEED = "seed_42"
DATASETS = ["quantemp", "scifact"]
MODELS = {
    "Qwen3-4B-Instruct-2507": "Qwen",
    "Mistral-7B-Instruct-v0.3": "Mistral",
    "Llama-3.1-8B-Instruct": "Llama",
}
# UQ-aware configurations to compare (excluding LogicalContradiction)
# Each entry: (display_name, folder_name, file_suffix)
# file_suffix is "logic_discrete" or "logic_OFF"
UQ_CONFIGS = [
    ("Ensemble+ACE", "Ensemble", "logic_discrete"),
    ("Ensemble", "Ensemble", "logic_OFF"),
    ("MSP", "MaximumSequenceProbability", "logic_discrete"),
    ("MTE", "MeanTokenEntropy", "logic_discrete"),
    ("Perplexity", "Perplexity", "logic_discrete"),
]
# Dataset → split mapping
DATASET_SPLIT = {
    "quantemp": "test",
    "scifact": "val",
}
OUTPUT_DIR = Path("results_dump/temp0.3/qualitative_analysis")


def get_result_filename(dataset: str, suffix: str) -> str:
    """Return the result filename for a given dataset and logic variant."""
    split = DATASET_SPLIT[dataset]
    return f"results_{split}_label_only_{suffix}.jsonl"


def load_jsonl(path: Path) -> list[dict]:
    """Load a JSONL file and return a list of records."""
    records = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def load_config_data(
    base_dir: Path,
    dataset: str,
    model: str,
    folder: str,
    result_file: str,
) -> dict[str, dict]:
    """
    Load results for a given dataset/model/config from seed_42.

    Returns a dict keyed by claim ID with relevant fields.
    """
    path = base_dir / SEED / dataset / model / "uq_aware" / folder / result_file
    if not path.exists():
        print(f"  WARNING: Missing {path}")
        return {}

    records = load_jsonl(path)
    return {
        r["id"]: {
            "id": r["id"],
            "claim": r["claim"],
            "gold_label": r["gold_label"],
            "predicted_verdict": r["predicted_verdict"],
        }
        for r in records
    }


def is_wrong(predicted_verdict: str, gold_label: str) -> bool:
    """Check if the prediction is wrong (does not match the gold label)."""
    return predicted_verdict != gold_label


def build_dataset_tables(
    base_dir: Path,
    dataset: str,
    models: list[str],
    configs: list[tuple[str, str, str]],
) -> pd.DataFrame:
    """
    Build the qualitative analysis table for a dataset, aggregating across all models and configs.

    Returns:
      - df_always_wrong: claims wrong in all configurations across all models
    """
    # Load results for each model and config
    config_data = {}  # "model_displayname" -> {id -> record}
    for model in models.keys():
        for display_name, folder, suffix in configs:
            result_file = get_result_filename(dataset, suffix)
            key = f"{models[model]}_{display_name}"
            print(f"  Loading {key}...")
            config_data[key] = load_config_data(
                base_dir, dataset, model, folder, result_file
            )

    # Get claim IDs present in all configs
    config_keys = list(config_data.keys())
    id_sets = [set(config_data[k].keys()) for k in config_keys if config_data[k]]
    if not id_sets:
        return pd.DataFrame()
    common_ids = set.intersection(*id_sets)
    print(f"  Common claims across all models/configs: {len(common_ids)}")

    # Categorise claims
    always_wrong_rows = []

    for claim_id in sorted(common_ids):
        # Check if wrong across all models and configs
        all_wrong = all(
            is_wrong(
                config_data[k][claim_id]["predicted_verdict"],
                config_data[k][claim_id]["gold_label"],
            )
            for k in config_keys
        )

        if all_wrong:
            # Build a row with per-config details
            base_info = {
                "id": claim_id,
                "claim": config_data[config_keys[0]][claim_id]["claim"],
                "gold_label": config_data[config_keys[0]][claim_id]["gold_label"],
            }

            # Add per-model-config columns
            for k in config_keys:
                rec = config_data[k][claim_id]
                base_info[f"{k}_verdict"] = rec["predicted_verdict"]

            always_wrong_rows.append(base_info)

    return pd.DataFrame(always_wrong_rows)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for dataset in DATASETS:
        print(f"\n{'='*60}")
        print(f"Processing: {dataset}")
        print(f"{'='*60}")

        df_wrong = build_dataset_tables(
            BASE_DIR, dataset, MODELS, UQ_CONFIGS
        )

        # Save to Excel
        out_file = OUTPUT_DIR / f"{dataset}_all_models_qualitative.xlsx"
        with pd.ExcelWriter(out_file, engine="openpyxl") as writer:
            df_wrong.to_excel(
                writer, sheet_name="Always Wrong", index=False
            )

            # Build distribution summary for always-wrong claims
            if not df_wrong.empty:
                summary_rows = []

                # Gold label distribution
                gold_counts = df_wrong["gold_label"].value_counts()
                for label, count in gold_counts.items():
                    summary_rows.append({
                        "Label": label,
                        "Count": count,
                        "Percentage": round(100 * count / len(df_wrong), 1),
                    })

                df_summary = pd.DataFrame(summary_rows)
                df_summary.to_excel(
                    writer,
                    sheet_name="Wrong Label Distribution",
                    index=False,
                )

        print(f"\n  Saved: {out_file}")
        print(f"  Always wrong (across all models & configs): {len(df_wrong)} claims")


if __name__ == "__main__":
    main()
