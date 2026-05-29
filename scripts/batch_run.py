import os
import json
import subprocess
import sys
import argparse
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

RUN_SCRIPT = project_root / "scripts" / "run.py"
CALIBRATION_RUN_SCRIPT = project_root / "src" / "utils" / "calibration_run.py"
ENSEMBLER_SCRIPT = project_root / "src" / "utils" / "ensembler.py"
CALIBRATE_SCRIPT = project_root / "src" / "utils" / "calibrate_threshold.py"
ANALYZE_SCRIPT = project_root / "scripts" / "analysis" / "analyze_run.py"

def run_calibration(args, unknown_hydra_args):
    """Executes the Joint UQ Generation and Threshold Sweep."""
    print(f"\n{'='*70}")
    print(f"📐 JOINT UQ CALIBRATION | Dataset: {args.dataset} | Split: {args.calibration_split}")
    print(f"⚙️ Logical Contradiction Check: {'ON' if args.check_logic else 'OFF'} | Format: {args.output_format}")
    print(f"{'='*70}\n")

    env = os.environ.copy()

    # Pass the explicit args to the underlying scripts
    calib_cmd_base = [
        "--dataset", args.dataset,
        "--split", args.calibration_split,
        "--model", args.model,
        "--output_format", args.output_format,
        "--logic_eval_method", args.logic_eval_method
    ]
    
    if args.check_logic:
        calib_cmd_base.append("--check_logic")

    print("⏳ 1A: Generating UQ Scores for calibration...")
    gen_result = subprocess.run(["python", str(CALIBRATION_RUN_SCRIPT)] + calib_cmd_base + unknown_hydra_args, env=env)
    
    if gen_result.returncode != 0:
        print(f"❌ Failed to generate UQ scores. Aborting.")
        sys.exit(1)
        
    print("\n⏳ 1B: Training Ensemble Model & Injecting Cross-Validation Predictions...")
    ens_result = subprocess.run(["python", str(ENSEMBLER_SCRIPT)] + calib_cmd_base + unknown_hydra_args, env=env)
    
    if ens_result.returncode != 0:
        print(f"❌ Ensemble modeling failed.")
        sys.exit(1)
        
    print("\n⏳ 1C: Computing AUROC-Optimal Thresholds...")
    cal_result = subprocess.run(["python", str(CALIBRATE_SCRIPT)] + calib_cmd_base + unknown_hydra_args, env=env)
    
    if cal_result.returncode != 0:
        print(f"❌ Calibration sweep failed.")
        sys.exit(1)
        
    print(f"\n✅ Calibration fully completed for {args.dataset}.")

def run_evaluation(args, unknown_hydra_args):
    """Executes a single evaluation run and subsequent analysis."""
    print(f"\n{'='*70}")
    print(f"🚀 EVALUATION JOB | Dataset: {args.dataset} | Mode: {args.mode}")
    print(f"📝 Format: {args.output_format}")
    if args.uq_method:
        print(f"⚙️ UQ Method: {args.uq_method} | Calibrated on: {args.calibrated_split}")
    print(f"{'='*70}\n")
    
    # Construct the config dictionary equivalent to what the interactive menu builds
    config = {
        "dataset": args.dataset,
        "mode": args.mode,
        "output_format": args.output_format,
        "test_split": args.test_split,
        "calibration": "No",
        "check_logic": "Yes" if args.check_logic else "No",
        "logic_eval_method": args.logic_eval_method
    }

    # Inject UQ specific configurations if necessary
    if args.mode in ["uq_aware", "uq_decompose"]:
        if not args.uq_method or not args.calibrated_split:
            print("❌ Error: --uq_method and --calibrated_split are required for UQ modes.")
            sys.exit(1)
        config["uq_method"] = args.uq_method
        config["calibrated_split"] = args.calibrated_split
        config["calibration_method_used"] = "threshold_sweep"

    env = os.environ.copy()
    env["AUTO_CONFIG"] = json.dumps(config)

    active_hydra_args = unknown_hydra_args + [
        f"retriever.type={args.retriever_type}",
        f"llm.model_name={args.model}",
        f"check_logic={args.check_logic}",
        f"logic_eval_method={args.logic_eval_method}"
    ]
    
    print("⏳ Running experiment pipeline...")
    exp_result = subprocess.run(["python", str(RUN_SCRIPT)] + active_hydra_args, env=env)
    
    if exp_result.returncode == 0:
        print("\n📊 Experiment finished successfully. Running analysis...")
        subprocess.run(["python", str(ANALYZE_SCRIPT)] + active_hydra_args, env=env)
        print("\n🎉 Evaluation and Analysis Complete!")
    else:
        print(f"\n⚠️ Experiment failed with return code {exp_result.returncode}.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute a single experiment or calibration task.")
    
    # 1. Primary execution switch
    parser.add_argument("--run_type", choices=["calibrate", "evaluate"], required=True, help="Whether to calibrate thresholds or run an evaluation.")
    
    # 2. Shared arguments
    parser.add_argument("--dataset", type=str, required=True, help="e.g., scifact or quantemp")
    parser.add_argument("--model", type=str, required=True, help="Full HF model path (e.g., meta-llama/Llama-3.2-1B-Instruct)")
    parser.add_argument("--retriever_type", type=str, default="hybrid", help="e.g., vector or hybrid")
    
    # 3. Calibration-specific arguments
    parser.add_argument("--calibration_split", type=str, help="Split to calibrate on (Required if run_type=calibrate)")
    
    # <-- ABLATION ARGUMENTS -->
    parser.add_argument("--check_logic", action="store_true", help="Enable the Logical Contradiction check during calibration")
    parser.add_argument("--output_format", type=str, choices=["full_response", "label_only"], default="label_only", help="Format of the LLM generation")
    parser.add_argument("--logic_eval_method", type=str, choices=["discrete", "probabilistic"], default="discrete", help="Evaluation method for the logical contradiction")


    # 4. Evaluation-specific arguments
    parser.add_argument("--mode", type=str, help="e.g., never_retrieve, always_retrieve, uq_decompose (Required if run_type=evaluate)")
    parser.add_argument("--test_split", type=str, help="Split to evaluate on (Required if run_type=evaluate)")
    parser.add_argument("--uq_method", type=str, help="e.g., Perplexity, MeanTokenEntropy")
    parser.add_argument("--calibrated_split", type=str, help="The split the UQ method was calibrated on.")

    # Parse known args, leaving Hydra args untouched
    args, unknown_hydra_args = parser.parse_known_args()

    # Routing
    if args.run_type == "calibrate":
        if not args.calibration_split:
            parser.error("--calibration_split is required when --run_type is calibrate")
        run_calibration(args, unknown_hydra_args)
        
    elif args.run_type == "evaluate":
        if not args.mode or not args.test_split:
            parser.error("--mode and --test_split are required when --run_type is evaluate")
        run_evaluation(args, unknown_hydra_args)