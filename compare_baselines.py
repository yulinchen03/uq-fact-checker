#!/usr/bin/env python3
"""
compare_baselines.py
====================
Compares baselines (never_retrieve, always_retrieve, factscore) and UQ-aware
methods across base (vector) and gold evidence retrieval for RQ1 experiments.

Generates 7 plots:
  1. Accuracy comparison for SciFact   (Base vs Gold, baselines only)
  2. Accuracy comparison for QuanTemp  (Base vs Gold, baselines only)
  3. Token breakdown    for SciFact   (stacked bars, all methods incl. UQ)
  4. Token breakdown    for QuanTemp  (stacked bars, all methods incl. UQ)
  5. Calls comparison   for SciFact   (base only, all methods, grouped bars)
  6. Calls comparison   for QuanTemp  (base only, all methods, grouped bars)
  7. Atomic facts       (both datasets in one plot, baselines only)
"""

import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path


# ── Constants ────────────────────────────────────────────────────────────────

BASELINES = ["never_retrieve", "always_retrieve", "factscore"]

DISPLAY_NAMES = {
    "never_retrieve":  "Parametric\n(No RAG)",
    "always_retrieve": "Always\nRetrieve",
    "factscore":       "FActScore",
    # UQ methods are shortened dynamically via shorten_name()
}

UQ_SHORT = {
    "MaximumSequenceProbability":                   "MaxSeqProb",
    "MeanTokenEntropy":                             "MeanTokEnt",
    "MeanPointwiseMutualInformation":               "MeanPMI",
    "MeanConditionalPointwiseMutualInformation":    "MeanCPMI",
    "Perplexity":                                   "Perplexity",
}

UQ_VARIANTS = ["naive", "threshold_sweep"]
VARIANT_SUFFIX = {"naive": "(naive)", "threshold_sweep": "(sweep)"}

DATASETS = {
    "scifact":  {"subdir": "scifact",  "pattern": "results_train_summary.json",     "title": "SciFact"},
    "quantemp": {"subdir": "quantemp", "pattern": "results_test_mini_summary.json", "title": "QuanTemp"},
}

MODEL = "Qwen3-4B-Instruct-2507"


# ── Helpers ──────────────────────────────────────────────────────────────────

def load_json(filepath: Path):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠  Could not load {filepath}: {e}")
        return None


def display_name(method_raw: str) -> str:
    if method_raw in DISPLAY_NAMES:
        return DISPLAY_NAMES[method_raw]
    # Handle suffixed UQ keys like "MaximumSequenceProbability__baseline"
    if "__" in method_raw:
        base_method, variant = method_raw.rsplit("__", 1)
        short = UQ_SHORT.get(base_method, base_method)
        suffix = VARIANT_SUFFIX.get(variant, variant)
        return f"{short}\n{suffix}"
    return UQ_SHORT.get(method_raw, method_raw)


def resolve_summary(archive_root: Path, dataset_key: str, baseline: str) -> Path:
    ds = DATASETS[dataset_key]
    return archive_root / "RQ1" / ds["subdir"] / MODEL / baseline / ds["pattern"]


def collect_all(archive_root: Path, dataset_key: str) -> dict:
    """Return {method_key: data_dict} for baselines AND both UQ-aware variants.

    UQ keys are suffixed: 'MethodName__naive' and 'MethodName__threshold_sweep'.
    """
    ds = DATASETS[dataset_key]
    out = {}

    # 1) Baselines
    for bl in BASELINES:
        p = resolve_summary(archive_root, dataset_key, bl)
        data = load_json(p)
        if data:
            out[bl] = data

    # 2) UQ-aware runs (both variants)
    for variant in UQ_VARIANTS:
        uq_dir = archive_root / "RQ1" / ds["subdir"] / MODEL / "uq_aware" / variant
        if not uq_dir.exists():
            continue
        for method_dir in sorted(uq_dir.iterdir()):
            summary = method_dir / ds["pattern"]
            data = load_json(summary)
            if data:
                method_name = data.get("uq_settings", {}).get("method", method_dir.name)
                key = f"{method_name}__{variant}"
                out[key] = data

    return out


def ordered_methods(data: dict) -> list:
    """Return method keys in a logical order:
    Parametric → UQ baseline (alpha) → UQ sweep (alpha) → Always Retrieve → FActScore."""
    order = []
    if "never_retrieve" in data:
        order.append("never_retrieve")
    uq_base = sorted(k for k in data if k not in BASELINES and k.endswith("__naive"))
    uq_sweep = sorted(k for k in data if k not in BASELINES and k.endswith("__threshold_sweep"))
    order.extend(uq_base)
    order.extend(uq_sweep)
    if "always_retrieve" in data:
        order.append("always_retrieve")
    if "factscore" in data:
        order.append("factscore")
    return order


# ── Token helpers ────────────────────────────────────────────────────────────

def _get_tokens(metrics: dict):
    uq_in  = metrics.get("avg_uq_input_tokens", 0)
    uq_out = metrics.get("avg_uq_output_tokens", 0)
    gen_in  = metrics.get("avg_gen_input_tokens", metrics.get("avg_rag_input_tokens", 0))
    gen_out = metrics.get("avg_gen_output_tokens", metrics.get("avg_rag_output_tokens", 0))

    if uq_in == 0 and uq_out == 0 and metrics.get("avg_uq_tokens", 0) > 0:
        uq_out = metrics.get("avg_uq_tokens", 0)
    if gen_in == 0 and gen_out == 0:
        gen_out = metrics.get("avg_gen_tokens",
                    metrics.get("avg_rag_tokens",
                        metrics.get("avg_total_tokens", 0)))
    return uq_in, uq_out, gen_in, gen_out


# ── Plot 1 & 2: Accuracy (all methods, Base vs Gold) ────────────────────────

def plot_accuracy(dataset_key: str, base_data: dict, gold_data: dict, save_path: Path):
    ds_title = DATASETS[dataset_key]["title"]
    methods = ordered_methods(base_data)
    labels, base_vals, gold_vals = [], [], []

    for m in methods:
        labels.append(display_name(m))
        base_vals.append(base_data[m]["metrics"]["balanced_accuracy"])
        gold_vals.append(
            gold_data[m]["metrics"]["balanced_accuracy"] if m in gold_data else 0.0
        )

    x = np.arange(len(labels))
    width = 0.32
    fig, ax = plt.subplots(figsize=(max(12, len(labels) * 1.5), 7))

    for i, m in enumerate(methods):
        if m == "never_retrieve":
            # Parametric: single centered bar (no retrieval difference)
            rect = ax.bar(x[i], base_vals[i], width * 1.5, color="#e74c3c", edgecolor="black")
            ax.bar_label(rect, fmt="%.3f", padding=3, fontsize=9, fontweight="bold")
        else:
            r1 = ax.bar(x[i] - width / 2, base_vals[i], width, color="#3498db", edgecolor="black")
            r2 = ax.bar(x[i] + width / 2, gold_vals[i], width, color="#f1c40f", edgecolor="black")
            ax.bar_label(r1, fmt="%.3f", padding=3, fontsize=9, fontweight="bold")
            ax.bar_label(r2, fmt="%.3f", padding=3, fontsize=9, fontweight="bold")

    max_val = max(max(base_vals), max(gold_vals)) if gold_vals else max(base_vals)
    ax.set_ylim(0, max_val * 1.25)
    ax.set_ylabel("Balanced Accuracy", fontsize=12, fontweight="bold")
    ax.set_title(f"Accuracy Comparison — {ds_title}  (Base vs Gold Evidence)", fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=10)
    ax.grid(axis="y", linestyle="--", alpha=0.6)

    legend_elements = [
        mpatches.Patch(facecolor="#e74c3c", edgecolor="black", label="Parametric (No RAG)"),
        mpatches.Patch(facecolor="#3498db", edgecolor="black", label="Base (Vector Evidence)"),
        mpatches.Patch(facecolor="#f1c40f", edgecolor="black", label="Gold Evidence"),
    ]
    ax.legend(handles=legend_elements, fontsize=10, loc="upper left")

    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"✅  Accuracy plot saved: {save_path}")


# ── Plot 3 & 4: Token breakdown (all methods) ───────────────────────────────

def plot_tokens(dataset_key: str, all_data: dict, save_path: Path):
    ds_title = DATASETS[dataset_key]["title"]
    methods = ordered_methods(all_data)

    labels = [display_name(m) for m in methods]
    uq_in_vals, uq_out_vals, gen_in_vals, gen_out_vals = [], [], [], []

    for m in methods:
        uq_in, uq_out, gen_in, gen_out = _get_tokens(all_data[m]["metrics"])
        uq_in_vals.append(uq_in);   uq_out_vals.append(uq_out)
        gen_in_vals.append(gen_in);  gen_out_vals.append(gen_out)

    uq_in_arr  = np.array(uq_in_vals)
    uq_out_arr = np.array(uq_out_vals)
    gen_in_arr  = np.array(gen_in_vals)
    gen_out_arr = np.array(gen_out_vals)

    x = np.arange(len(labels))
    width = 0.55
    fig, ax = plt.subplots(figsize=(max(12, len(labels) * 1.6), 7))

    c1, c2, c3, c4 = "#FFC300", "#FF5733", "#00C9A7", "#2C73D2"

    p1 = ax.bar(x, uq_in_arr,  width, color=c1, edgecolor="black")
    p2 = ax.bar(x, uq_out_arr, width, bottom=uq_in_arr, color=c2, edgecolor="black")
    p3 = ax.bar(x, gen_in_arr,  width, bottom=uq_in_arr + uq_out_arr, color=c3, edgecolor="black")
    p4 = ax.bar(x, gen_out_arr, width, bottom=uq_in_arr + uq_out_arr + gen_in_arr, color=c4, edgecolor="black")

    fmt = lambda v: f"{int(v)}" if v > 0 else ""
    ax.bar_label(p1, label_type="center", fmt=fmt, fontsize=9, fontweight="bold", color="black")
    ax.bar_label(p2, label_type="center", fmt=fmt, fontsize=9, fontweight="bold", color="black")
    ax.bar_label(p3, label_type="center", fmt=fmt, fontsize=9, fontweight="bold", color="black")
    ax.bar_label(p4, label_type="center", fmt=fmt, fontsize=9, fontweight="bold", color="white")

    totals = uq_in_arr + uq_out_arr + gen_in_arr + gen_out_arr
    max_tok = max(totals) if len(totals) else 10
    ax.set_ylim(0, max_tok * 1.3)

    for i, t in enumerate(totals):
        ax.text(i, t + max_tok * 0.02, f"{int(t)}", ha="center", fontsize=11, fontweight="bold")

    ax.set_ylabel("Avg Tokens per Claim", fontsize=12, fontweight="bold")
    ax.set_title(f"Token Consumption Breakdown — {ds_title}", fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=10)
    ax.grid(axis="y", linestyle="--", alpha=0.6)

    legend_els = [
        mpatches.Patch(facecolor=c1, edgecolor="black", label="UQ Input (Prompt)"),
        mpatches.Patch(facecolor=c2, edgecolor="black", label="UQ Output (Thinking)"),
        mpatches.Patch(facecolor=c3, edgecolor="black", label="Gen Input (RAG Evidence)"),
        mpatches.Patch(facecolor=c4, edgecolor="black", label="Gen Output (RAG Answer)"),
    ]
    ax.legend(handles=legend_els, loc="upper left", fontsize=10)

    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"✅  Token plot saved: {save_path}")


# ── Plot 5 & 6: Calls comparison (base only, all methods, per dataset) ──────

def plot_calls(dataset_key: str, ds_data: dict, save_path: Path):
    ds_title = DATASETS[dataset_key]["title"]
    methods = ordered_methods(ds_data)
    labels, ret_vals, llm_vals = [], [], []

    for m in methods:
        met = ds_data[m]["metrics"]
        labels.append(display_name(m))
        ret_vals.append(met.get("avg_retrieval_calls", 0))
        llm_vals.append(met.get("avg_llm_calls", 0))

    x = np.arange(len(labels))
    width = 0.30
    fig, ax = plt.subplots(figsize=(max(12, len(labels) * 1.6), 7))

    r1 = ax.bar(x - width / 2, ret_vals, width, color="#8E44AD", edgecolor="black", label="Avg Retrieval Calls")
    r2 = ax.bar(x + width / 2, llm_vals, width, color="#16A085", edgecolor="black", label="Avg LLM Calls")

    ax.bar_label(r1, fmt="%.2f", padding=3, fontsize=9, fontweight="bold")
    ax.bar_label(r2, fmt="%.2f", padding=3, fontsize=9, fontweight="bold")

    max_v = max(max(ret_vals, default=0), max(llm_vals, default=0))
    ax.set_ylim(0, max_v * 1.3)

    ax.set_ylabel("Avg Calls per Claim", fontsize=12, fontweight="bold")
    ax.set_title(f"Retrieval & LLM Calls per Method — {ds_title} (Base Evidence)", fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=10)
    ax.grid(axis="y", linestyle="--", alpha=0.6)
    ax.legend(fontsize=11, loc="upper left")

    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"✅  Calls plot saved: {save_path}")


# ── Plot 6: Atomic facts (both datasets, baselines only) ────────────────────

def plot_atomic_facts(all_base: dict, save_path: Path):
    baselines_present = [bl for bl in BASELINES
                         if any(bl in all_base.get(ds, {}) for ds in ("scifact", "quantemp"))]

    labels = [display_name(bl) for bl in baselines_present]
    sci_vals, qt_vals = [], []

    for bl in baselines_present:
        sci_vals.append(
            all_base.get("scifact", {}).get(bl, {}).get("metrics", {}).get("avg_atomic_facts", 0)
        )
        qt_vals.append(
            all_base.get("quantemp", {}).get(bl, {}).get("metrics", {}).get("avg_atomic_facts", 0)
        )

    x = np.arange(len(labels))
    width = 0.30
    fig, ax = plt.subplots(figsize=(10, 6))

    r1 = ax.bar(x - width / 2, sci_vals, width, color="#2980B9", edgecolor="black", label="SciFact")
    r2 = ax.bar(x + width / 2, qt_vals, width, color="#E67E22", edgecolor="black", label="QuanTemp")

    ax.bar_label(r1, fmt="%.2f", padding=3, fontsize=10, fontweight="bold")
    ax.bar_label(r2, fmt="%.2f", padding=3, fontsize=10, fontweight="bold")

    max_v = max(max(sci_vals, default=0), max(qt_vals, default=0))
    ax.set_ylim(0, max_v * 1.4)

    ax.set_ylabel("Avg Atomic Facts per Claim", fontsize=12, fontweight="bold")
    ax.set_title("Average Atomic Facts Extracted per Baseline", fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=11)
    ax.grid(axis="y", linestyle="--", alpha=0.6)
    ax.legend(fontsize=11, loc="upper left")

    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"✅  Atomic facts plot saved: {save_path}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    base_root = Path("results/archives/base")
    gold_root = Path("results/archives/gold")

    out_dir = Path("vis/baselines")
    out_dir.mkdir(parents=True, exist_ok=True)

    all_base = {}   # {dataset_key: {method: data}}
    all_gold = {}

    for ds_key in ("scifact", "quantemp"):
        all_base[ds_key] = collect_all(base_root, ds_key)
        all_gold[ds_key] = collect_all(gold_root, ds_key)

        if not all_base[ds_key]:
            print(f"⚠  No base data for {ds_key}, skipping.")
            continue

        # ── Accuracy plot (baselines only, base vs gold) ─────────────────
        plot_accuracy(
            ds_key,
            all_base[ds_key],
            all_gold.get(ds_key, {}),
            out_dir / f"{ds_key}_accuracy.png",
        )

        # ── Token breakdown (all methods, base evidence) ─────────────────
        plot_tokens(
            ds_key,
            all_base[ds_key],
            out_dir / f"{ds_key}_tokens.png",
        )

        # ── Calls comparison (base only, per dataset) ────────────────────
        plot_calls(
            ds_key,
            all_base[ds_key],
            out_dir / f"{ds_key}_calls.png",
        )

    # ── Atomic facts (both datasets, baselines only) ─────────────────────
    plot_atomic_facts(all_base, out_dir / "atomic_facts.png")

    print("\n✅  All baseline comparison plots generated.")


if __name__ == "__main__":
    main()
