import os
import json
import subprocess
import sys


def run_batch_experiments(experiment_queue):
    try:
        for i, config in enumerate(experiment_queue):
            print(f"\n{'='*60}")
            print(f"🚀 Launching Batch Job {i+1}/{len(experiment_queue)}: {config['mode']} on {config['dataset']}")
            print(f"{'='*60}\n")
            
            env = os.environ.copy()
            env["AUTO_CONFIG"] = json.dumps(config)
            
            try:
                # 1. Run the experiment (For UQ, this is Calibration on 'val')
                print("⏳ Running experiment pipeline...")
                exp_result = subprocess.run(["python", "rq1.py"], env=env)
                
                if exp_result.returncode == 0:
                    
                    # 2. Handle UQ-Aware 2-Step Process
                    if "calibration" in config and config["calibration"] == "Yes":
                        print("\n📐 Running calibration step...")
                        calibrate_result = subprocess.run(["python", "calibrate.py"], env=env)

                        if calibrate_result.returncode == 0:
                            print("✅ Calibration completed successfully. Rerunning pipeline for final evaluation...")
                            
                            config["calibration"] = "No" 
                            config["calibrated_split"] = config["calibration_split"]
                            env["AUTO_CONFIG"] = json.dumps(config) 

                            print('Visualizing calibration results...')
                            plot_result = subprocess.run(["python", "visualize_rq1_statistics.py"], env=env)
                            
                            exp_result = subprocess.run(["python", "rq1.py"], env=env)

                            if exp_result.returncode != 0:
                                print(f"⚠️ Re-run after calibration failed with return code {exp_result.returncode}. Skipping analysis.")
                                continue
                        else:
                            print(f"⚠️ Calibration failed with return code {calibrate_result.returncode}")
                            continue

                    # 3. Run Analysis
                    print("\n📊 Experiment finished successfully. Running analysis...")
                    subprocess.run(["python", "analyze_rq1.py"], env=env)
                    
                else:
                    print(f"\n⚠️ Experiment {i+1} failed with return code {exp_result.returncode}. Skipping analysis.")
                    
            except Exception as e:
                print(f"\n❌ Unexpected error running job {i+1}: {e}")
                continue

        print("\n✅ All batch jobs completed!")

    except KeyboardInterrupt:
        print("\n\n🛑 Batch execution terminated. Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    jobs_queue = [
        # --- SCIFACT ---
        # {
        #     "dataset": "scifact",
        #     "mode": "never_retrieve",
        #     "test_split": "train" 
        # },
        # {
        #     "dataset": "scifact",
        #     "mode": "always_retrieve",
        #     "test_split": "train" 
        # },
        # {
        #     "dataset": "scifact",
        #     "mode": "uq_aware",
        #     "uq_method": "Perplexity",
        #     "calibration": "Yes",
        #     "tolerance": "0.05",
        #     "calibration_split": "val",
        #     # "calibrated_split": "val",
        #     "test_split": "train" 
        # },
        # {
        #     "dataset": "scifact",
        #     "mode": "uq_aware",
        #     "uq_method": "MaximumSequenceProbability",
        #     "calibration": "Yes",
        #     "tolerance": "0.05",
        #     "calibration_split": "val",
        #     # "calibrated_split": "val",
        #     "test_split": "train" 
        # },
        # {
        #     "dataset": "scifact",
        #     "mode": "uq_aware",
        #     "uq_method": "MeanTokenEntropy",
        #     "calibration": "Yes",
        #     "tolerance": "0.05",
        #     "calibration_split": "val",
        #     # "calibrated_split": "val",
        #     "test_split": "train" 
        # },
        # # --- QUANTEMP ---
        # {
        #     "dataset": "quantemp",
        #     "test_split": "test",
        #     "mode": "never_retrieve"
        # },
        # {
        #     "dataset": "quantemp",
        #     "test_split": "test",
        #     "mode": "always_retrieve"
        # },
        # {
        #     "dataset": "quantemp",
        #     "mode": "uq_aware",
        #     "uq_method": "Perplexity",
        #     "calibration": "Yes",
        #     "tolerance": "0.05",
        #     "calibration_split": "val",
        #     # "calibrated_split": "val",
        #     "test_split": "test" 
        # },
        # {
        #     "dataset": "quantemp",
        #     "mode": "uq_aware",
        #     "uq_method": "MaximumSequenceProbability",
        #     "calibration": "Yes",
        #     "tolerance": "0.05",
        #     "calibration_split": "val",
        #     # "calibrated_split": "val",
        #     "test_split": "test" 
        # },
        {
            "dataset": "quantemp",
            "mode": "uq_aware",
            "uq_method": "MeanTokenEntropy",
            "calibration": "Yes",
            "tolerance": "0.05",
            "calibration_split": "val",
            # "calibrated_split": "val",
            "test_split": "test" 
        },
    ]

    try:
        run_batch_experiments(jobs_queue)
    except KeyboardInterrupt:
        sys.exit(0)