import copy
from datetime import datetime
import os
import json
import shutil
import subprocess
import sys
import argparse
import inquirer
from pathlib import Path

project_root = Path(__file__).resolve().parent
sys.path.append(str(project_root))

RUN_SCRIPT = project_root / "run.py"
CALIBRATE_SCRIPT = project_root / "src" / "utils" / "calibrate.py"
ANALYZE_SCRIPT = project_root / "scripts" / "analysis" / "analyze_run.py"

def run_batch_experiments(experiment_queue, base_hydra_args):
    try:
        for i, config in enumerate(experiment_queue):
            print(f"\n{'='*70}")
            print(f"🚀 Launching Batch Job {i+1}/{len(experiment_queue)}")
            print(f"Mode: {config['mode']} | Dataset: {config['dataset']}")
            print(f"{'='*70}\n")
            
            env = os.environ.copy()
            env["AUTO_CONFIG"] = json.dumps(config)
            
            try:
                # 1. Run the experiment
                print("⏳ Running experiment pipeline...")
                exp_result = subprocess.run(["python", str(RUN_SCRIPT)] + base_hydra_args, env=env)
                
                if exp_result.returncode == 0:
                    
                    # 2. Handle UQ Calibration → Evaluation Pipeline
                    if "calibration" in config and config["calibration"] == "Yes":
                        print(f"\n📐 Running calibration (naive + threshold_sweep)...")
                        
                        cal_config = copy.deepcopy(config)
                        cal_env = os.environ.copy()
                        cal_env["AUTO_CONFIG"] = json.dumps(cal_config)
                        
                        calibrate_result = subprocess.run(["python", str(CALIBRATE_SCRIPT)] + base_hydra_args, env=cal_env)

                        if calibrate_result.returncode == 0:
                            print(f"✅ Calibration completed.")

                            calibration_methods = config.get("calibration_methods", ["naive", "threshold_sweep"])
                            eval_modes = config.get("eval_modes", ["uq_aware"])

                            for cal_method in calibration_methods:
                                for eval_mode in eval_modes: # if we are evaluating both uq_aware and uq_decompose
                                    print(f"\n🔄 Evaluating [{eval_mode.upper()} | {cal_method.upper()}]...")
                                    
                                    eval_config = copy.deepcopy(config)
                                    eval_config["mode"] = eval_mode
                                    eval_config["calibration"] = "No" 
                                    eval_config["calibrated_split"] = config["calibration_split"]
                                    eval_config["calibration_method_used"] = cal_method
                                    eval_env = os.environ.copy()
                                    eval_env["AUTO_CONFIG"] = json.dumps(eval_config)

                                    eval_result = subprocess.run(["python", str(RUN_SCRIPT)] + base_hydra_args, env=eval_env)

                                    if eval_result.returncode == 0:
                                        print(f"📊 [{eval_mode.upper()} | {cal_method.upper()}] Running analysis...")
                                        subprocess.run(["python", str(ANALYZE_SCRIPT)] + base_hydra_args, env=eval_env)
                                    else:
                                        print(f"⚠️ [{eval_mode.upper()} | {cal_method.upper()}] Evaluation failed.")
                        else:
                            print(f"⚠️ Calibration failed with return code {calibrate_result.returncode}")
                        
                        continue

                    # 3. Run Analysis (for non-calibration modes)
                    print("\n📊 Experiment finished successfully. Running analysis...")
                    subprocess.run(["python", str(ANALYZE_SCRIPT)] + base_hydra_args, env=env)
                    
                else:
                    print(f"\n⚠️ Experiment {i+1} failed with return code {exp_result.returncode}. Skipping analysis.")
                    
            except Exception as e:
                print(f"\n❌ Unexpected error running job {i+1}: {e}")
                continue

        print(f"\n✅ All batch jobs in queue completed!")

    except KeyboardInterrupt:
        print("\n\n🛑 Batch execution terminated. Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    from hydra import compose, initialize_config_dir
    
    # 1. Parse CLI Arguments (Allows headless mode & pass-through Hydra args)
    parser = argparse.ArgumentParser(description="Orchestrate experiment batch runs.")
    parser.add_argument("--run-name", type=str, default=None, help="Custom name for the output folder.")
    args, unknown_hydra_args = parser.parse_known_args()

    # Initialize Hydra to grab default model name for fallback
    initialize_config_dir(config_dir=str(project_root / "config"), version_base=None)
    _cfg = compose(config_name="config", overrides=unknown_hydra_args)
    model_short = _cfg.llm.model_name.split("/")[-1]

    default_name = f"{model_short}_run"
    run_name = args.run_name

    # Interactive prompt if no name was provided and we are in a terminal
    if not run_name:
        if sys.stdout.isatty():
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
        else:
            print("🤖 Headless mode detected without --run-name. Using default name.")
            run_name = default_name

    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # Define Source and Final Destinations
    source_dir = project_root / "results" / "active_run"
    final_dir = project_root / "results" / today_str / run_name

    print(f"\n📁 Active run data will be staged in: {source_dir.relative_to(project_root)}")
    print(f"📦 Final full results will be saved to: {final_dir.relative_to(project_root)}")

    # 2. Archive existing lingering results to prevent contamination
    if source_dir.exists() and any(source_dir.iterdir()):
        print(f"\n⚠️ Found lingering results in '{source_dir.relative_to(project_root)}'.")
        backup_name = f"active_run_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        archive_dir = project_root / "results" / "archived" / backup_name
        archive_dir.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source_dir), str(archive_dir))
        print(f"✅ Lingering files safely archived to {archive_dir.relative_to(project_root)}\n")

    # 3. Build the job queue 
    uq_methods = [
        "Perplexity",
        "MaximumSequenceProbability",
        "MeanTokenEntropy",
        "MeanPointwiseMutualInformation",
        "MeanConditionalPointwiseMutualInformation",
    ]

    jobs_queue = [
        # SCIFACT — Baselines
        {"dataset": "scifact", "mode": "never_retrieve", "test_split": "train"},
        {"dataset": "scifact", "mode": "always_retrieve", "test_split": "train"},
        {"dataset": "scifact", "mode": "factscore", "test_split": "train"},

        # QUANTEMP — Baselines
        {"dataset": "quantemp", "mode": "never_retrieve", "test_split": "test_mini"},
        {"dataset": "quantemp", "mode": "always_retrieve", "test_split": "test_mini"},
        {"dataset": "quantemp", "mode": "factscore", "test_split": "test_mini"},
    ]

    # UQ jobs
    for method in uq_methods:
        jobs_queue.append({
            "dataset": "scifact",
            "mode": "uq_decompose",
            "uq_method": method,
            "calibration": "Yes",
            "calibration_split": "val",
            "test_split": "train",
            "eval_modes": ["uq_decompose"],
            "calibration_methods": ["threshold_sweep"],
        })
        jobs_queue.append({
            "dataset": "quantemp",
            "mode": "uq_decompose",
            "uq_method": method,
            "calibration": "Yes",
            "calibration_split": "val",
            "test_split": "test_mini",
            "eval_modes": ["uq_decompose"],
            "calibration_methods": ["threshold_sweep"],
        })

    # 4. Run all experiments
    try:
        retriever_type = "hybrid"

        print(f"\n\n{'*'*80}")
        print(f"🌟 STARTING FULL BATCH RUN FOR RETRIEVER TYPE: {retriever_type.upper()}")
        print(f"{'*'*80}\n")
        
        # Append retriever type to any other hydra arguments the user passed in via CLI
        active_hydra_args = unknown_hydra_args + [f"retriever.type={retriever_type}"]
        
        current_queue = copy.deepcopy(jobs_queue)
        run_batch_experiments(current_queue, base_hydra_args=active_hydra_args)
        
        # 5. Safely Transfer active_run to the Final Destination
        if source_dir.exists():
            dest_run = final_dir / "run"
            print(f"\n📦 Moving results from active staging into {dest_run.relative_to(project_root)}...")
            dest_run.mkdir(parents=True, exist_ok=True)
            shutil.copytree(str(source_dir), str(dest_run), dirs_exist_ok=True)
            
            # Clean up active_run to leave a clean slate for the next run
            shutil.rmtree(str(source_dir))
            print("✅ Transfer successful!")

        # 6. Collect all summaries into a consolidated folder for easy access
        summaries_dir = final_dir / "summaries"
        run_results = final_dir / "run"

        if run_results.exists():
            summary_files = list(run_results.rglob("*_summary.json"))

            if summary_files:
                summaries_dir.mkdir(parents=True, exist_ok=True)
                for src_path in summary_files:
                    # Flatten the path to prevent naming collisions
                    rel = src_path.relative_to(run_results)
                    flat_name = str(rel).replace(os.sep, "__")
                    shutil.copy2(str(src_path), str(summaries_dir / flat_name))

                print(f"\n📋 Collected {len(summary_files)} summary files into: {summaries_dir.relative_to(project_root)}")
            else:
                print("\nℹ️ No summary files found to collect.")

        print(f"\n🎉 All done! Full results are bundled in: {final_dir.relative_to(project_root)}")

    except KeyboardInterrupt:
        print("\n\n🛑 Execution completely terminated by user.")
        sys.exit(0)