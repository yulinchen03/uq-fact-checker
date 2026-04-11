import os
import json
import inspect
import inquirer
import numpy as np
from pathlib import Path
from omegaconf import DictConfig
from sklearn.metrics import balanced_accuracy_score, confusion_matrix, classification_report, precision_recall_fscore_support, roc_auc_score
import hydra
import lm_polygraph.estimators as estimators

# --- NEW: Dynamic Path Resolution ---
# __file__ is scripts/analysis/analyze_run.py
ROOT_DIR = Path(__file__).resolve().parents[2]

def validate_float(answers, current):
    """Validates that the user input can be safely cast to a float."""
    try:
        float(current)
        return True
    except ValueError:
        return False

def get_experiment_config():
    """Interactive menu for selecting which results to analyze."""
    if "AUTO_CONFIG" in os.environ:
        return json.loads(os.environ["AUTO_CONFIG"])

    available_estimators = [
        name for name, obj in inspect.getmembers(estimators, inspect.isclass)
    ]

    questions = [
        inquirer.List('dataset',
                      message="Select the dataset to evaluate",
                      choices=['scifact', 'quantemp']),

        inquirer.List('mode',
                      message="Select the experimental mode",
                      choices=['never_retrieve', 'always_retrieve', 'uq_aware', 'factscore', 'uq_decompose']),
        
        inquirer.List('uq_method',
                      message="Select the UQ Method for this run",
                      choices=available_estimators,
                      ignore=lambda answers: answers.get('mode') not in ('uq_aware', 'uq_decompose')),
                      
        # Ask if we are analyzing the Calibration run or the Evaluation run
        inquirer.List('calibration',
                      message="Which run are you analyzing?",
                      choices=['Calibration (val)', 'Evaluation'],
                      ignore=lambda answers: answers.get('mode') not in ('uq_aware', 'uq_decompose')),

        inquirer.List('calibration_method_used',
                      message="Select the calibration method that was used",
                      choices=['naive', 'threshold_sweep'],
                      ignore=lambda answers: answers.get('calibration') != 'Evaluation'),

        inquirer.List('calibrated_split',
                      message="Which split was originally used for calibration?",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini'],
                      ignore=lambda answers: answers.get('calibration') != 'Evaluation'),

        inquirer.List('calibration_split',
                      message="Select the data split for calibration",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini'],
                      ignore=lambda answers: answers.get('calibration') != 'Calibration (val)'),

        inquirer.List('test_split',
                      message="Select the data split",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini','test_mini'],
                      ignore=lambda answers: answers.get('calibration') == 'Calibration (val)'),
    ]

    return inquirer.prompt(questions)


def clean_label(label):
    """Cleans punctuation, underscores, and enforces strict casing without semantic mapping."""
    lbl = str(label).upper().replace(".", "").replace("_", " ")
    return " ".join(lbl.split())


@hydra.main(version_base=None, config_path="../../config", config_name="config")
def analyze_results(cfg: DictConfig):
    # 1. Get the user configuration interactively or via batch
    config = get_experiment_config()
    if not config:
        print("Analysis cancelled.")
        return

    # 2. Set strict Hydra config overrides
    cfg.data.dataset_name = config['dataset']
    cfg.mode = config['mode']
    model_name = cfg.llm.model_name.split("/")[-1]

    # Explicitly set the split and calibration mode
    if cfg.mode in ('uq_aware', 'uq_decompose'):
        cfg.uncertainty.method = config['uq_method']
        if config.get('calibration') == 'Calibration (val)':
            cfg.data.split = config['calibration_split']
            cfg.uncertainty.calibration_mode = True
        else:
            cfg.data.split = config['test_split']
            cfg.uncertainty.calibration_mode = False
    else:
        cfg.data.split = config['test_split']
        cfg.uncertainty.calibration_mode = False

    # 3. Define Smart Paths (Directly targeting active_run)
    base_dir = ROOT_DIR / "results" / "active_run" / cfg.data.dataset_name / model_name
    
    if cfg.mode in ('uq_aware', 'uq_decompose'):
        if cfg.uncertainty.calibration_mode:
            file_dir = base_dir / "calibration" / cfg.uncertainty.method
        else:
            calib_method_used = config.get('calibration_method_used', 'threshold_sweep')
            file_dir = base_dir / cfg.mode / calib_method_used / cfg.uncertainty.method
    else:
        file_dir = base_dir / cfg.mode

    filename = f"results_{cfg.data.split}.jsonl"
    file_path = file_dir / filename

    if file_path.exists():
        print(f"\n✅ Found run at: {file_path.relative_to(ROOT_DIR)}")
    else:
        print(f"\n❌ Error: Results file not found.")
        print(f"Checked path: {file_path.relative_to(ROOT_DIR)}")
        print("Make sure you have run the experiment for this configuration first.")
        return
    
    # Save the summary in the exact same folder the JSONL was found in
    save_path = file_path.with_name(f"results_{cfg.data.split}_summary.json")

    # 4. Define strict dataset labels for exclusion validation
    if cfg.data.dataset_name == "quantemp":
        allowed_labels = ["TRUE", "FALSE", "CONFLICTING"]
    else:
        allowed_labels = ["SUPPORT", "CONTRADICT", "NOT ENOUGH INFO"]
    
    y_true = []
    y_pred = []
    latencies = []
    uncertainty_scores = []
    
    # Setup token tracking arrays
    all_input_tokens = []
    all_output_tokens = []
    total_tokens = []
    
    uq_input_tokens = []
    uq_output_tokens = []
    gen_input_tokens = []
    gen_output_tokens = []
    decomp_input_tokens = []
    decomp_output_tokens = []
    num_retrieval_calls = []
    num_llm_calls = []
    num_atomic_facts = []
    uq_flagged_list = []
    atom_rag_triggered = []
    excluded_count = 0

    # 5. Parse Results
    with open(file_path, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)

                gold_raw = data.get("gold_label", "NOT ENOUGH INFO")
                pred_raw = data.get("predicted_verdict", "NOT ENOUGH INFO")

                gold = clean_label(gold_raw)
                pred = clean_label(pred_raw)

                # checks both gold AND pred, if the label does not match one of the available options, exclude from our results
                if gold not in allowed_labels or pred not in allowed_labels:
                    excluded_count += 1
                    continue

                y_true.append(gold)
                y_pred.append(pred)
                
                # Capture UQ score if it exists
                uq_score = data.get("uncertainty_score")
                if uq_score is not None:
                    uncertainty_scores.append(float(uq_score))
                else:
                    uncertainty_scores.append(None)

                metrics = data.get("metrics", {})
                latencies.append(metrics.get("latency_seconds", 0.0))
                
                # Capture standard input/output tokens
                in_toks = metrics.get("input_tokens", 0)
                out_toks = metrics.get("output_tokens", 0)
                all_input_tokens.append(in_toks)
                all_output_tokens.append(out_toks)
                total_tokens.append(in_toks + out_toks)
                
                # Split tokens natively 
                uq_input_tokens.append(metrics.get("uq_input_tokens", 0))
                uq_output_tokens.append(metrics.get("uq_output_tokens", 0))
                decomp_input_tokens.append(metrics.get("decomp_input_tokens", 0))
                decomp_output_tokens.append(metrics.get("decomp_output_tokens", 0))
                gen_input_tokens.append(metrics.get("gen_input_tokens", 0))
                gen_output_tokens.append(metrics.get("gen_output_tokens", 0))
                
                num_retrieval_calls.append(metrics.get("num_retrieval_calls", 0))
                num_llm_calls.append(metrics.get("num_llm_calls", 0))

                # Track uq flags (uq_aware and uq_decompose mode)
                uq_flagged_list.append(data.get("uq_flagged", False))

                # Track per-atom retrieval: count how many atoms triggered RAG
                atom_verdicts = data.get("atomic_verdicts", [])
                for av in atom_verdicts:
                    atom_rag_triggered.append(av.get("rag_triggered", False))

                # Count atomic facts: for factscore (always decomposes), count all;
                # for uq_decompose, only count when decomposition was triggered
                if "atomic_facts" in data and isinstance(data["atomic_facts"], list):
                    is_decomposed = data.get("uq_flagged", False)
                    if cfg.mode == "factscore" or is_decomposed:
                        num_atomic_facts.append(len(data["atomic_facts"]))

            except json.JSONDecodeError:
                continue

    if not y_true:
        print("No valid data found in the file after applying strict exclusion rules.")
        return

    # --- CALCULATIONS ---
    if cfg.mode in ('uq_aware', 'uq_decompose'):
        uq_flag_rate = np.mean(uq_flagged_list) if uq_flagged_list else 0.0
        retrieval_rate = np.mean(atom_rag_triggered) if atom_rag_triggered else 0.0
    elif cfg.mode in ['always_retrieve', 'factscore']:
        uq_flag_rate = 0.0
        retrieval_rate = 1.0
    else:
        uq_flag_rate = 0.0
        retrieval_rate = 0.0

    avg_latency = float(np.mean(latencies)) if latencies else 0.0
    
    # Calculate Token Averages
    avg_input_tokens = float(np.mean(all_input_tokens)) if all_input_tokens else 0.0
    avg_output_tokens = float(np.mean(all_output_tokens)) if all_output_tokens else 0.0
    avg_tokens = float(np.mean(total_tokens)) if total_tokens else 0.0
    
    # Calculate separate averages
    avg_uq_input_tokens = float(np.mean(uq_input_tokens)) if uq_input_tokens else 0.0
    avg_uq_output_tokens = float(np.mean(uq_output_tokens)) if uq_output_tokens else 0.0
    avg_gen_input_tokens = float(np.mean(gen_input_tokens)) if gen_input_tokens else 0.0
    avg_gen_output_tokens = float(np.mean(gen_output_tokens)) if gen_output_tokens else 0.0
    avg_decomp_input_tokens = float(np.mean(decomp_input_tokens)) if decomp_input_tokens else 0.0
    avg_decomp_output_tokens = float(np.mean(decomp_output_tokens)) if decomp_output_tokens else 0.0
    
    avg_retrieval_calls = float(np.mean(num_retrieval_calls)) if num_retrieval_calls else 0.0
    avg_llm_calls = float(np.mean(num_llm_calls)) if num_llm_calls else 0.0
    
    if cfg.mode in ('factscore', 'uq_decompose'):
        avg_atomic_facts = float(np.mean(num_atomic_facts)) if num_atomic_facts else 0.0
    else:
        avg_atomic_facts = 1.0
    
    total_claims = len(y_true)

    bal_acc = balanced_accuracy_score(y_true, y_pred)
    
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true, y_pred, labels=allowed_labels, zero_division=0
    )
    conf_matrix = confusion_matrix(y_true, y_pred, labels=allowed_labels)

    # Calculate Error Detection AUROC
    auroc = None
    if any(s is not None for s in uncertainty_scores):
        valid_pairs = [(t, p, u) for t, p, u in zip(y_true, y_pred, uncertainty_scores) if u is not None]
        if valid_pairs:
            y_t_valid = [x[0] for x in valid_pairs]
            y_p_valid = [x[1] for x in valid_pairs]
            u_valid = [x[2] for x in valid_pairs]
            
            # 1 = Incorrect (Error), 0 = Correct
            errors = [1 if t != p else 0 for t, p in zip(y_t_valid, y_p_valid)]
            
            if len(set(errors)) > 1:
                auroc = roc_auc_score(errors, u_valid)

    stats_output = {
        "experiment_mode": cfg.mode,
        "dataset": cfg.data.dataset_name,
        "split": cfg.data.split,
        "total_claims": total_claims,
        "excluded_claims": excluded_count,
        "metrics": {
            "balanced_accuracy": float(bal_acc),
            "error_detection_auroc": float(f"{auroc:.4f}") if auroc is not None else None,
            "avg_latency_seconds": float(f"{avg_latency:.3f}"),
            "avg_total_tokens": int(avg_tokens),
            "avg_input_tokens": int(avg_input_tokens),
            "avg_output_tokens": int(avg_output_tokens),
            "avg_uq_input_tokens": int(avg_uq_input_tokens),
            "avg_uq_output_tokens": int(avg_uq_output_tokens),
            "avg_gen_input_tokens": int(avg_gen_input_tokens),
            "avg_gen_output_tokens": int(avg_gen_output_tokens),
            "avg_decomp_input_tokens": int(avg_decomp_input_tokens),
            "avg_decomp_output_tokens": int(avg_decomp_output_tokens),
            "avg_retrieval_calls": float(f"{avg_retrieval_calls:.2f}"),
            "avg_llm_calls": float(f"{avg_llm_calls:.2f}"),
            "avg_atomic_facts": float(f"{avg_atomic_facts:.2f}"),
            "uq_flag_rate": float(f"{uq_flag_rate*100:.2f}"),
            "retrieval_trigger_rate": float(f"{retrieval_rate*100:.2f}")
        }
    }

    if cfg.mode in ('uq_aware', 'uq_decompose'):
        # --- FIXED: Calibration path correctly points to active_run ---
        threshold_used = cfg.uncertainty.get('threshold', 0.0)
        if not cfg.uncertainty.calibration_mode and config.get('calibration_method_used'):
            calib_method_used = config['calibration_method_used']
            calib_split = config.get('calibrated_split', config.get('calibration_split', 'val'))
            thresh_path = ROOT_DIR / "results" / "active_run" / cfg.data.dataset_name / model_name / "calibration" / calib_method_used / cfg.uncertainty.method / f"optimal_threshold_{calib_split}.json"
            
            if thresh_path.exists():
                with open(thresh_path, 'r') as tf:
                    threshold_used = json.load(tf).get('optimal_threshold', threshold_used)
            else:
                print(f"⚠️ Warning: Calibration threshold file not found at {thresh_path.relative_to(ROOT_DIR)}")
        
        stats_output["uq_settings"] = {
            "method": config.get('uq_method'),
            "calibration": config.get('calibration'),
            "threshold": float(threshold_used)
        }

    stats_output["per_class_metrics"] = {}
    stats_output["confusion_matrix"] = {
        "labels": allowed_labels,
        "matrix": conf_matrix.tolist() 
    }

    for i, label in enumerate(allowed_labels):
        stats_output["per_class_metrics"][label] = {
            "precision": float(precision[i]),
            "recall": float(recall[i]),
            "f1-score": float(f1[i]),
            "support": int(support[i])
        }

    # --- SAVE TO FILE ---
    save_path.parent.mkdir(parents=True, exist_ok=True)
    with open(save_path, 'w') as f:
        json.dump(stats_output, f, indent=4)

    # --- PRINT REPORT ---
    print("\n" + "="*40)
    print("       PERFORMANCE REPORT       ")
    print("="*40)
    print(f"Total Evaluated Claims : {total_claims}")
    print(f"Excluded Claims        : {excluded_count} (Invalid label output)")
    print("-" * 40)
    print(f"1. Avg Inference Latency : {avg_latency:.3f} s/claim")
    print(f"2. Avg Total Tokens      : {avg_tokens:.0f} tokens/claim")
    print(f"   ├─ Avg Input Tokens     : {avg_input_tokens:.0f} tokens/claim")
    print(f"   ├─ Avg Output Tokens    : {avg_output_tokens:.0f} tokens/claim")
    print(f"   ├─ Avg UQ Input Tokens  : {avg_uq_input_tokens:.0f} tokens/claim")
    print(f"   ├─ Avg UQ Output Tokens : {avg_uq_output_tokens:.0f} tokens/claim")
    print(f"   ├─ Avg Gen Input Tokens : {avg_gen_input_tokens:.0f} tokens/claim")
    print(f"   ├─ Avg Gen Output Tokens: {avg_gen_output_tokens:.0f} tokens/claim")
    print(f"   ├─ Avg Decomp Input Tokens: {avg_decomp_input_tokens:.0f} tokens/claim")
    print(f"   └─ Avg Decomp Output Tokens: {avg_decomp_output_tokens:.0f} tokens/claim")
    print(f"3. Avg LLM Calls         : {avg_llm_calls:.2f} calls/claim")
    print(f"4. Avg Retrieval Calls   : {avg_retrieval_calls:.2f} calls/claim")
    print(f"5. Avg Atomic Facts      : {avg_atomic_facts:.2f} facts/claim (decomposed claims only)")
    print(f"6. UQ Flag Rate   : {uq_flag_rate*100:.2f}%")
    print(f"7. Retrieval Trigger Rate : {retrieval_rate*100:.2f}% (of all atomic claims)")
    print("=" * 40)
    print(f"★★★ BALANCED ACCURACY: {bal_acc:.4f} ({(bal_acc*100):.2f}%) ★★★")
    if auroc is not None:
        print(f"★★★ ERROR DETECT AUROC : {auroc:.4f} ★★★")
    else:
        print("★★★ ERROR DETECT AUROC : N/A (No UQ scores or unified class) ★★★")
    print("=" * 40)
    print("\nDetailed Classification Report:")
    print(classification_report(y_true, y_pred, target_names=allowed_labels, zero_division=0))
    print(f"\nStats successfully saved to: {save_path.relative_to(ROOT_DIR)}")

if __name__ == "__main__":
    try:
        analyze_results()
    except KeyboardInterrupt:
        import sys
        sys.exit(0)