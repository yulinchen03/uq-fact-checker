import os
import json
import inspect
import inquirer
import numpy as np
from pathlib import Path
from omegaconf import DictConfig
from sklearn.metrics import f1_score, balanced_accuracy_score, confusion_matrix, classification_report, precision_recall_fscore_support, roc_auc_score
import hydra
import lm_polygraph.estimators as estimators

ROOT_DIR = Path(__file__).resolve().parents[2]

def validate_float(answers, current):
    try:
        float(current)
        return True
    except ValueError:
        return False

def get_experiment_config():
    """Interactive menu for selecting which results to analyze."""
    if "AUTO_CONFIG" in os.environ:
        return json.loads(os.environ["AUTO_CONFIG"])

    available_estimators = [name for name, obj in inspect.getmembers(estimators, inspect.isclass)]

    questions = [
        inquirer.List('dataset', message="Select the dataset to evaluate", choices=['scifact', 'quantemp']),
        inquirer.List('mode', message="Select the experimental mode", choices=['never_retrieve', 'always_retrieve', 'uq_aware', 'granular', 'uq_decompose', 'openai_never_retrieve', 'openai_always_retrieve']),
        inquirer.List('output_format', message="Select the output format", choices=['label_only', 'full_response']),
        inquirer.List('uq_method', message="Select the UQ Method for this run", choices=available_estimators, ignore=lambda answers: answers.get('mode') not in ('uq_aware', 'uq_decompose')),
        inquirer.List('calibrated_split', message="Which split was originally used for calibration?", choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini'], ignore=lambda answers: answers.get('mode') not in ('uq_aware', 'uq_decompose')),
        inquirer.List('check_logic', message="Was the Logic check enabled for this run?", choices=['Yes', 'No']),
        inquirer.List('logic_eval_method', message="Select the Logic evaluation method", choices=['discrete', 'probabilistic'], ignore=lambda answers: answers.get('check_logic') == 'No'),
        inquirer.List('test_split', message="Select the test data split", choices=['train', 'val', 'test', 'train_mini', 'val_mini','test_mini']),
    ]
    return inquirer.prompt(questions)


def clean_label(label):
    """Cleans punctuation, underscores, and enforces strict casing."""
    lbl = str(label).upper().replace(".", "").replace("_", " ")
    return " ".join(lbl.split())


def resolve_paths(cfg, config, model_name, output_format):
    """Constructs and validates all file paths needed for analysis."""
    seed = cfg.get("seed", 42)
    base_dir = ROOT_DIR / "run_results" / f"seed_{seed}" / cfg.data.dataset_name / model_name
    logic_suffix = f"logic_{config.get('logic_eval_method', 'discrete')}" if config.get('check_logic') == 'Yes' else "logic_OFF"
    
    if cfg.mode in ('uq_aware', 'uq_decompose'):
        file_path = base_dir / cfg.mode / cfg.uncertainty.method / f"results_{cfg.data.split}_{output_format}_{logic_suffix}.jsonl"
    else:
        file_path = base_dir / cfg.mode / f"results_{cfg.data.split}_{output_format}_{logic_suffix}.jsonl"

    save_path = file_path.with_name(f"results_{cfg.data.split}_{output_format}_{logic_suffix}_summary.json")
    
    thresh_path = None
    if cfg.mode in ('uq_aware', 'uq_decompose'):
        calib_split = config.get('calibrated_split', 'val')
        thresh_path = ROOT_DIR / "run_results" / f"seed_{seed}" / cfg.data.dataset_name / model_name / "calibration" / f"optimal_thresholds_{calib_split}_{output_format}_{logic_suffix}.json"

    return file_path, save_path, thresh_path, logic_suffix


def parse_results_file(file_path, allowed_labels, cfg):
    """Reads the JSONL file and extracts all metrics into a structured dictionary."""
    data_store = {
        "y_true": [], "y_pred": [], "y_parametric": [], "latencies": [], "uncertainty_scores": [],
        "all_input_tokens": [], "all_output_tokens": [], "total_tokens": [],
        "uq_input_tokens": [], "uq_output_tokens": [], "gen_input_tokens": [], "gen_output_tokens": [],
        "decomp_input_tokens": [], "decomp_output_tokens": [], "num_retrieval_calls": [], 
        "num_llm_calls": [], "num_atomic_facts": [], "uq_flagged_list": [], "atom_rag_triggered": [],
        "excluded_count": 0
    }

    with open(file_path, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                
                gold = clean_label(data.get("gold_label", "N/A"))
                pred = clean_label(data.get("predicted_verdict", data.get("parametric_verdict", "N/A")))
                param = clean_label(data.get("parametric_verdict", "N/A"))

                if gold not in allowed_labels or pred not in allowed_labels:
                    data_store["excluded_count"] += 1
                    continue

                data_store["y_true"].append(gold)
                data_store["y_pred"].append(pred)
                data_store["y_parametric"].append(param)
                
                # UQ Scores
                uq_score = data["uq_scores"].get(cfg.uncertainty.method) if "uq_scores" in data else data.get("uncertainty_score")
                data_store["uncertainty_scores"].append(float(uq_score) if uq_score is not None else None)

                # Metrics Extraction
                metrics = data.get("metrics", {})
                data_store["latencies"].append(metrics.get("latency_seconds", 0.0))
                
                in_toks = metrics.get("input_tokens", 0)
                out_toks = metrics.get("output_tokens", 0)
                data_store["all_input_tokens"].append(in_toks)
                data_store["all_output_tokens"].append(out_toks)
                data_store["total_tokens"].append(in_toks + out_toks)
                
                for key in ["uq_input_tokens", "uq_output_tokens", "decomp_input_tokens", "decomp_output_tokens", "gen_input_tokens", "gen_output_tokens", "num_retrieval_calls", "num_llm_calls"]:
                    data_store[key].append(metrics.get(key, 0))

                data_store["uq_flagged_list"].append(data.get("uq_flagged", False))

                for av in data.get("atomic_verdicts", []):
                    data_store["atom_rag_triggered"].append(av.get("rag_triggered", False))
                    
                if "atomic_facts" in data and isinstance(data["atomic_facts"], list):
                    if cfg.mode == "granular" or data.get("uq_flagged", False):
                        data_store["num_atomic_facts"].append(len(data["atomic_facts"]))

            except json.JSONDecodeError:
                continue

    return data_store


def compute_metrics(ds, allowed_labels, cfg):
    """Calculates all statistical metrics from the parsed data arrays."""
    def safe_mean(arr): return float(np.mean(arr)) if arr else 0.0

    if cfg.mode in ('uq_aware', 'uq_decompose'):
        uq_flag_rate = safe_mean(ds["uq_flagged_list"])
        retrieval_rate = safe_mean(ds["atom_rag_triggered"])
    elif cfg.mode in ['always_retrieve', 'openai_always_retrieve', 'granular']:
        uq_flag_rate, retrieval_rate = 0.0, 1.0
    else:
        uq_flag_rate, retrieval_rate = 0.0, 0.0

    avg_atomic_facts = safe_mean(ds["num_atomic_facts"]) if cfg.mode in ('granular', 'uq_decompose') else 1.0

    # Sklearn Metrics
    macro_f1 = f1_score(ds["y_true"], ds["y_pred"], labels=allowed_labels, average='macro', zero_division=0)
    bal_acc = balanced_accuracy_score(ds["y_true"], ds["y_pred"])
    precision, recall, f1, support = precision_recall_fscore_support(ds["y_true"], ds["y_pred"], labels=allowed_labels, zero_division=0)
    conf_matrix = confusion_matrix(ds["y_true"], ds["y_pred"], labels=allowed_labels)

    # AUROC Calculation
    auroc = None
    if any(s is not None for s in ds["uncertainty_scores"]):
        valid_pairs = [(t, p, u) for t, p, u in zip(ds["y_true"], ds["y_parametric"], ds["uncertainty_scores"]) if u is not None]
        if valid_pairs:
            errors = [1 if t != p else 0 for t, p, _ in valid_pairs]
            if len(set(errors)) > 1:
                auroc = roc_auc_score(errors, [u for _, _, u in valid_pairs])

    computed = {
        "balanced_accuracy": float(bal_acc),
        "macro_f1": float(macro_f1),
        "error_detection_auroc": float(f"{auroc:.4f}") if auroc is not None else None,
        "avg_latency_seconds": float(f"{safe_mean(ds['latencies']):.3f}"),
        "avg_total_tokens": int(safe_mean(ds["total_tokens"])),
        "avg_input_tokens": int(safe_mean(ds["all_input_tokens"])),
        "avg_output_tokens": int(safe_mean(ds["all_output_tokens"])),
        "avg_uq_input_tokens": int(safe_mean(ds["uq_input_tokens"])),
        "avg_uq_output_tokens": int(safe_mean(ds["uq_output_tokens"])),
        "avg_gen_input_tokens": int(safe_mean(ds["gen_input_tokens"])),
        "avg_gen_output_tokens": int(safe_mean(ds["gen_output_tokens"])),
        "avg_decomp_input_tokens": int(safe_mean(ds["decomp_input_tokens"])),
        "avg_decomp_output_tokens": int(safe_mean(ds["decomp_output_tokens"])),
        "avg_retrieval_calls": float(f"{safe_mean(ds['num_retrieval_calls']):.2f}"),
        "avg_llm_calls": float(f"{safe_mean(ds['num_llm_calls']):.2f}"),
        "avg_atomic_facts": float(f"{avg_atomic_facts:.2f}"),
        "uq_flag_rate": float(f"{uq_flag_rate*100:.2f}"),
        "retrieval_trigger_rate": float(f"{retrieval_rate*100:.2f}")
    }
    return computed, conf_matrix, precision, recall, f1, support, auroc


def print_performance_report(ds, computed, auroc, allowed_labels, save_path):
    """Formats and prints the console summary report."""
    print("\n" + "="*40)
    print("       PERFORMANCE REPORT       ")
    print("="*40)
    print(f"Total Evaluated Claims : {len(ds['y_true'])}")
    print(f"Excluded Claims        : {ds['excluded_count']} (Invalid label output)")
    print("-" * 40)
    print(f"1. Avg Inference Latency : {computed['avg_latency_seconds']} s/claim")
    print(f"2. Avg Total Tokens      : {computed['avg_total_tokens']} tokens/claim")
    print(f"   ├─ Avg Input Tokens     : {computed['avg_input_tokens']} tokens/claim")
    print(f"   ├─ Avg Output Tokens    : {computed['avg_output_tokens']} tokens/claim")
    print(f"   ├─ Avg UQ Input/Output  : {computed['avg_uq_input_tokens']} / {computed['avg_uq_output_tokens']} tokens")
    print(f"   ├─ Avg Gen Input/Output : {computed['avg_gen_input_tokens']} / {computed['avg_gen_output_tokens']} tokens")
    print(f"   └─ Avg Decomp In/Out    : {computed['avg_decomp_input_tokens']} / {computed['avg_decomp_output_tokens']} tokens")
    print(f"3. Avg LLM Calls         : {computed['avg_llm_calls']} calls/claim")
    print(f"4. Avg Retrieval Calls   : {computed['avg_retrieval_calls']} calls/claim")
    print(f"5. Avg Atomic Facts      : {computed['avg_atomic_facts']} facts/claim (decomposed only)")
    print(f"6. UQ Flag Rate   : {computed['uq_flag_rate']}%")
    print(f"7. Retrieval Trigger Rate : {computed['retrieval_trigger_rate']}% (of atomic claims)")
    print("=" * 40)
    print(f"★★★ BALANCED ACCURACY: {computed['balanced_accuracy']:.4f} ({(computed['balanced_accuracy']*100):.2f}%) ★★★")
    print(f"★★★ MACRO F1: {computed['macro_f1']:.4f} ({(computed['macro_f1']*100):.2f}%) ★★★")
    print(f"★★★ ERROR DETECT AUROC : {f'{auroc:.4f}' if auroc is not None else 'N/A'} ★★★")
    print("=" * 40)
    print("\nDetailed Classification Report:")
    print(classification_report(ds["y_true"], ds["y_pred"], target_names=allowed_labels, zero_division=0))
    print(f"\nStats successfully saved to: {save_path.relative_to(ROOT_DIR)}")


@hydra.main(version_base=None, config_path="../../config", config_name="config")
def analyze_results(cfg: DictConfig):
    config = get_experiment_config()
    if not config: return

    # 1. Configuration Setup
    cfg.data.dataset_name = config['dataset']
    cfg.mode = config['mode']
    cfg.data.split = config['test_split']
    output_format = config.get('output_format', 'label_only')
    model_name = cfg.llm.model_name.split("/")[-1]
    
    if cfg.mode in ('uq_aware', 'uq_decompose'):
        cfg.uncertainty.method = config['uq_method']

    # 2. Path Resolution
    file_path, save_path, thresh_path, logic_suffix = resolve_paths(cfg, config, model_name, output_format)

    if not file_path.exists():
        print(f"\n❌ Error: Results file not found at {file_path.relative_to(ROOT_DIR)}")
        return
    else:
        print(f"\n✅ Found run at: {file_path.relative_to(ROOT_DIR)}")

    allowed_labels = ["TRUE", "FALSE", "CONFLICTING"] if cfg.data.dataset_name == "quantemp" else ["SUPPORT", "CONTRADICT", "NOT ENOUGH INFO"]

    # 3. Parse Data
    ds = parse_results_file(file_path, allowed_labels, cfg)
    if not ds["y_true"]:
        print("No valid data found after applying strict exclusion rules.")
        return

    # 4. Compute Metrics
    computed_metrics, conf_matrix, precision, recall, f1, support, auroc = compute_metrics(ds, allowed_labels, cfg)

    # 5. Build Output Dictionary
    stats_output = {
        "experiment_mode": cfg.mode,
        "output_format": output_format,
        "dataset": cfg.data.dataset_name,
        "split": cfg.data.split,
        "total_claims": len(ds["y_true"]),
        "excluded_claims": ds["excluded_count"],
        "metrics": computed_metrics,
        "per_class_metrics": {},
        "confusion_matrix": {"labels": allowed_labels, "matrix": conf_matrix.tolist()}
    }

    if cfg.mode in ('uq_aware', 'uq_decompose'):
        threshold_used = cfg.uncertainty.get('threshold', 0.0)
        if thresh_path and thresh_path.exists():
            with open(thresh_path, 'r') as tf:
                t_data = json.load(tf)
                threshold_used = t_data.get(cfg.uncertainty.method, {}).get('optimal_threshold', threshold_used)
        stats_output["uq_settings"] = {"method": config.get('uq_method'), "threshold": float(threshold_used)}

    for i, label in enumerate(allowed_labels):
        stats_output["per_class_metrics"][label] = {
            "precision": float(precision[i]), "recall": float(recall[i]), "f1-score": float(f1[i]), "support": int(support[i])
        }

    # 6. Save and Report
    save_path.parent.mkdir(parents=True, exist_ok=True)
    with open(save_path, 'w') as f:
        json.dump(stats_output, f, indent=4)

    print_performance_report(ds, computed_metrics, auroc, allowed_labels, save_path)


if __name__ == "__main__":
    try:
        analyze_results()
    except KeyboardInterrupt:
        import sys
        sys.exit(0)