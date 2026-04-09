import copy
from datetime import datetime
import os
import json
import shutil
import subprocess
import sys
import inquirer

def run_batch_experiments(experiment_queue, retriever_type="vector"):
    try:
        for i, config in enumerate(experiment_queue):
            print(f"\n{'='*70}")
            print(f"🚀 Launching Batch Job {i+1}/{len(experiment_queue)}")
            print(f"Mode: {config['mode']} | Dataset: {config['dataset']} | Retriever: {retriever_type.upper()}")
            print(f"{'='*70}\n")
            
            env = os.environ.copy()
            env["AUTO_CONFIG"] = json.dumps(config)
            
            # Hydra command-line override
            hydra_args = [f"retriever.type={retriever_type}"]
            
            try:
                # 1. Run the experiment
                print("⏳ Running experiment pipeline...")
                exp_result = subprocess.run(["python", "rq1.py"] + hydra_args, env=env)
                
                if exp_result.returncode == 0:
                    
                    # 2. Handle UQ Calibration → Evaluation Pipeline
                    if "calibration" in config and config["calibration"] == "Yes":
                        # Run calibrate.py ONCE — it computes both naive and threshold_sweep thresholds
                        print(f"\n📐 Running calibration (naive + threshold_sweep)...")
                        
                        cal_config = copy.deepcopy(config)
                        cal_env = os.environ.copy()
                        cal_env["AUTO_CONFIG"] = json.dumps(cal_config)
                        
                        calibrate_result = subprocess.run(["python", "calibrate.py"] + hydra_args, env=cal_env)

                        if calibrate_result.returncode == 0:
                            print(f"✅ Calibration completed (both methods).")

                            # Evaluate each calibration method × each eval mode
                            calibration_methods = config.get("calibration_methods", ["naive", "threshold_sweep"])
                            eval_modes = config.get("eval_modes", ["uq_aware"])

                            for cal_method in calibration_methods:
                                for eval_mode in eval_modes:
                                    print(f"\n🔄 Evaluating [{eval_mode.upper()} | {cal_method.upper()}]...")
                                    
                                    eval_config = copy.deepcopy(config)
                                    eval_config["mode"] = eval_mode
                                    eval_config["calibration"] = "No" 
                                    eval_config["calibrated_split"] = config["calibration_split"]
                                    eval_config["calibration_method_used"] = cal_method
                                    eval_env = os.environ.copy()
                                    eval_env["AUTO_CONFIG"] = json.dumps(eval_config)

                                    eval_result = subprocess.run(["python", "rq1.py"] + hydra_args, env=eval_env)

                                    if eval_result.returncode == 0:
                                        print(f"📊 [{eval_mode.upper()} | {cal_method.upper()}] Running analysis...")
                                        subprocess.run(["python", "analyze_rq1.py"] + hydra_args, env=eval_env)
                                    else:
                                        print(f"⚠️ [{eval_mode.upper()} | {cal_method.upper()}] Evaluation failed with return code {eval_result.returncode}.")
                        else:
                            print(f"⚠️ Calibration failed with return code {calibrate_result.returncode}")
                        
                        continue

                    # 3. Run Analysis (for non-calibration modes)
                    print("\n📊 Experiment finished successfully. Running analysis...")
                    subprocess.run(["python", "analyze_rq1.py"] + hydra_args, env=env)
                    
                else:
                    print(f"\n⚠️ Experiment {i+1} failed with return code {exp_result.returncode}. Skipping analysis.")
                    
            except Exception as e:
                print(f"\n❌ Unexpected error running job {i+1}: {e}")
                continue

        print(f"\n✅ All batch jobs completed for retriever: {retriever_type.upper()}!")

    except KeyboardInterrupt:
        print("\n\n🛑 Batch execution terminated. Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    import glob
    import hydra
    from omegaconf import DictConfig

    # Load model name from config for the default folder name
    from hydra import compose, initialize_config_dir
    initialize_config_dir(config_dir=os.path.abspath("config"), version_base=None)
    _cfg = compose(config_name="config")
    model_short = _cfg.llm.model_name.split("/")[-1]

    # ========================
    # 1. Prompt user for run folder name
    # ========================
    retriever_types = ["vector"]
    default_name = f"{model_short}_run"

    setup_questions = [
        inquirer.Text('run_name',
                      message="Enter a name for this experiment run",
                      default=default_name),
    ]
    setup = inquirer.prompt(setup_questions)
    if not setup:
        print("\nSetup cancelled. Exiting...")
        sys.exit(0)

    run_name = setup['run_name'].strip() or default_name
    today_str = datetime.now().strftime("%Y-%m-%d")
    run_dir = os.path.join("results", "runs", today_str, run_name)

    print(f"\n📁 Results for this run will be saved to: {run_dir}")

    # ========================
    # 2. Archive existing results if present
    # ========================
    source_dir = "results/RQ1"

    if os.path.exists(source_dir):
        print(f"\n⚠️ Found existing results in '{source_dir}'. Archiving before starting...")
        archive_dir = os.path.join(run_dir, "archived_previous", "RQ1")
        os.makedirs(os.path.dirname(archive_dir), exist_ok=True)
        if os.path.exists(archive_dir):
            shutil.rmtree(archive_dir)
        shutil.move(source_dir, archive_dir)
        print(f"✅ Archived to {archive_dir}\n")

    # ========================
    # 3. Build the job queue 
    # ========================
    uq_methods = [
        "Perplexity",
        "MaximumSequenceProbability",
        "MeanTokenEntropy",
        "MeanPointwiseMutualInformation",
        "MeanConditionalPointwiseMutualInformation",
    ]

    jobs_queue = [
        # # SCIFACT — Baselines
        {"dataset": "scifact", "mode": "never_retrieve", "test_split": "train"},
        {"dataset": "scifact", "mode": "always_retrieve", "test_split": "train"},
        {"dataset": "scifact", "mode": "factscore", "test_split": "train"},

        # # QUANTEMP — Baselines
        {"dataset": "quantemp", "mode": "never_retrieve", "test_split": "test_mini"},
        {"dataset": "quantemp", "mode": "always_retrieve", "test_split": "test_mini"},
        {"dataset": "quantemp", "mode": "factscore", "test_split": "test_mini"},
    ]

    # UQ jobs: calibrate once per method, then evaluate both uq_aware & uq_decompose
    for method in uq_methods:
        jobs_queue.append({
            "dataset": "scifact",
            "mode": "uq_aware",
            "uq_method": method,
            "calibration": "Yes",
            "calibration_split": "val",
            "test_split": "train",
            "eval_modes": ["uq_decompose"],
            "calibration_methods": ["threshold_sweep"],
        })
        jobs_queue.append({
            "dataset": "quantemp",
            "mode": "uq_aware",
            "uq_method": method,
            "calibration": "Yes",
            "calibration_split": "val_mini",
            "test_split": "test_mini",
            "eval_modes": ["uq_decompose"],
            "calibration_methods": ["threshold_sweep"],
        })

    # ========================
    # 4. Run all experiments
    # ========================
    try:
        for r_type in retriever_types:
            print(f"\n\n{'*'*80}")
            print(f"🌟 STARTING FULL BATCH RUN FOR RETRIEVER TYPE: {r_type.upper()}")
            print(f"{'*'*80}\n")
            
            current_queue = copy.deepcopy(jobs_queue)
            run_batch_experiments(current_queue, retriever_type=r_type)
            
            # Copy results into the run directory
            if os.path.exists(source_dir):
                dest = os.path.join(run_dir, "RQ1")
                print(f"\n📦 Copying results into {dest}...")
                os.makedirs(dest, exist_ok=True)
                shutil.copytree(source_dir, dest, dirs_exist_ok=True)
                shutil.rmtree(source_dir)
                print("✅ Results saved!")

        # ========================================
        # 5. Collect all summaries into one folder
        # ========================================
        summaries_dir = os.path.join(run_dir, "summaries")
        rq1_results = os.path.join(run_dir, "RQ1")

        if os.path.exists(rq1_results):
            summary_files = glob.glob(os.path.join(rq1_results, "**", "*_summary.json"), recursive=True)

            if summary_files:
                os.makedirs(summaries_dir, exist_ok=True)
                for src_path in summary_files:
                    # Create a descriptive filename from the relative path
                    # e.g. scifact/Qwen3-4B/uq_aware/threshold_sweep/Perplexity/results_train_summary.json
                    #    → scifact__uq_aware__threshold_sweep__Perplexity__results_train_summary.json
                    rel = os.path.relpath(src_path, rq1_results)
                    flat_name = rel.replace(os.sep, "__")
                    shutil.copy2(src_path, os.path.join(summaries_dir, flat_name))

                print(f"\n📋 Collected {len(summary_files)} summary files into: {summaries_dir}")
            else:
                print("\nℹ️ No summary files found to collect.")

        print(f"\n✅ All done! Full results are in: {run_dir}")

    except KeyboardInterrupt:
        print("\n\n🛑 Execution completely terminated by user.")
        sys.exit(0)