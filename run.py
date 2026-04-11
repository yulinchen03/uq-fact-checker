import os
import random
import sys
import hydra
import json
import logging
import time
from pathlib import Path
import numpy as np
from omegaconf import DictConfig
from tqdm import tqdm
from dotenv import load_dotenv

# --- DYNAMIC PATH CORRECTION ---
# __file__ is run.py (located in the root directory)
project_root = Path(__file__).resolve().parent
sys.path.append(str(project_root))

from src.pipeline_builder import build_pipeline
from src.utils.metrics import MetricsRecorder
from src.utils.loader import LocalDataLoader 
import inspect
import inquirer
import lm_polygraph.estimators as estimators
from transformers import set_seed

# --- PREVENT MEMORY FRAGMENTATION ---
os.environ["PYTORCH_ALLOC_CONF"] = "expandable_segments:True"

import multiprocessing as mp
# This forces Python to spawn fresh processes instead of cloning locked CUDA memory.
try:
    mp.set_start_method('spawn', force=True)
except RuntimeError:
    pass

# Tell vLLM explicitly to use spawn
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"
import torch

def lock_random_seeds(seed: int = 42):
    """Locks all random number generators for deterministic pipeline execution."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    set_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

load_dotenv()
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
logging.getLogger("chromadb").setLevel(logging.ERROR)
logging.getLogger("transformers").setLevel(logging.ERROR)
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

def validate_float(answers, current):
    """Validates that the user input can be safely cast to a float."""
    try:
        float(current)
        return True
    except ValueError:
        return False

def get_experiment_config():
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

        inquirer.List('calibration', 
                      message="Apply calibration?",
                      choices=['Yes', 'No'],
                      ignore=lambda answers: answers.get('mode') not in ('uq_aware', 'uq_decompose')),

        inquirer.List('calibration_split',
                      message="Select the data split for calibration",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini'],
                      ignore=lambda answers: answers.get('calibration') != 'Yes'),

        inquirer.List('calibrated_split',
                      message="Select the data split which was used for calibration",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini'],
                      ignore=lambda answers: answers.get('calibration') == 'Yes' or answers.get('mode') not in ('uq_aware', 'uq_decompose')),

        inquirer.List('calibration_method_used',
                      message="Select the calibration method that was used",
                      choices=['naive', 'threshold_sweep'],
                      ignore=lambda answers: answers.get('calibration') == 'Yes' or answers.get('mode') not in ('uq_aware', 'uq_decompose')),

        inquirer.List('test_split',
                      message="Select the test data split",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini'],
                      ignore=lambda answers: answers.get('calibration') == 'Yes'),
    ]

    return inquirer.prompt(questions)


@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg: DictConfig):
    lock_random_seeds(42)
    
    model_name = cfg.llm.model_name.split("/")[1]
    
    if cfg.mode in ('uq_aware', 'uq_decompose'):
        if not cfg.uncertainty.calibration_mode:
            calib_split = cfg.data.calibrated_split
            calib_method = cfg.data.calibration_method_used
            
            # --- FIXED: Calibration path perfectly mapped to results/active_run/... ---
            calibrated_thresh_path = project_root / "results" / "active_run" / cfg.data.dataset_name / model_name / "calibration" / calib_method / cfg.uncertainty.method / f"optimal_threshold_{calib_split}.json"
            
            if calibrated_thresh_path.exists():
                with open(calibrated_thresh_path, 'r') as f:
                    thresh_data = json.load(f)
                    cfg.uncertainty.threshold = float(thresh_data.get("optimal_threshold", cfg.uncertainty.threshold))
                print(f"🎯 Loaded calibrated threshold: {cfg.uncertainty.threshold} for {cfg.uncertainty.method} (from {calib_split} split, method={calib_method})")
            else:
                print(f"⚠️ Calibration file not found at {calibrated_thresh_path}.")
                print(f"Falling back to manual configured threshold: {cfg.uncertainty.threshold}")
    else:
        cfg.uncertainty.method = "UQ module disabled"
        cfg.uncertainty.threshold = 0.0
        cfg.uncertainty.calibration_mode = False 

    print(f"\n🚀 Starting run on {cfg.data.dataset_name} ({cfg.data.split})")
    print(f"Mode: {cfg.mode} | UQ Method: {cfg.uncertainty.method}")
    if cfg.mode in ('uq_aware', 'uq_decompose'):
        print(f"Threshold: {cfg.uncertainty.threshold} | Calibration Mode: {cfg.uncertainty.calibration_mode}")

    # 4. Initialize Loader & Data
    loader = LocalDataLoader(data_root=str(project_root / "data"))
    
    dataset = loader.load(dataset_name=cfg.data.dataset_name, split=cfg.data.split, mode=cfg.mode)
    
    # 5. Build Pipeline
    pipeline_steps = build_pipeline(cfg)

    print("\n-----------------------")
    print(f"Pipeline components:")
    for i, step in enumerate(pipeline_steps):
        print(f"  Step {i+1}: {step.__class__.__name__}")
    print("-----------------------\n")
    
    # 6. Define Output Paths 
    base_out_dir = project_root / "results" / "active_run" / cfg.data.dataset_name / model_name
    
    if cfg.uncertainty.calibration_mode:
        final_dir = base_out_dir / "calibration" / cfg.uncertainty.method
    elif cfg.mode in ("uq_aware", "uq_decompose"):
        calib_method_used = cfg.data.calibration_method_used
        final_dir = base_out_dir / cfg.mode / calib_method_used / cfg.uncertainty.method
    else:
        final_dir = base_out_dir / cfg.mode
        
    final_dir.mkdir(parents=True, exist_ok=True)
    final_file = final_dir / f"results_{cfg.data.split}.jsonl"

    print(f"Saving results to: {final_file.relative_to(project_root)}")

    # Empty the results file before starting
    open(final_file, 'w').close()
    
    # 7. Execution Loop 
    with open(final_file, 'w') as f_out:
        for i, sample in enumerate(tqdm(dataset, desc=f"Running {cfg.data.dataset_name}|{cfg.data.split}|{cfg.mode}|{cfg.uncertainty.method}")):
            sample.mode = cfg.mode 
            
            start_time = time.perf_counter()
            
            for component in pipeline_steps:
                try:
                    component.process(sample)
                except Exception as e:
                    print(f"Error processing claim {sample.id}: {e}")
                    sample.explanation = f"Pipeline Error: {str(e)}"
            
            end_time = time.perf_counter()
            
            if hasattr(sample, 'metrics'):
                sample.metrics.latency_seconds = end_time - start_time
            
            f_out.write(sample.model_dump_json() + "\n")
            f_out.flush() 

    print(f"\n✅ Run complete! Results saved to {final_file.relative_to(project_root)}")

if __name__ == "__main__":
    config = get_experiment_config()
    
    if not config:
        print("Experiment cancelled.")
        sys.exit(0)

    if config.get('calibration') == 'Yes':
        active_split = config['calibration_split']
    else:
        active_split = config['test_split']

    sys.argv.append(f"data={config['dataset']}")
    sys.argv.append(f"data.split={active_split}")
    sys.argv.append(f"mode={config['mode']}")
    
    if config['mode'] in ('uq_aware', 'uq_decompose'):
        sys.argv.append(f"uncertainty.method={config['uq_method']}")
        sys.argv.append(f"uncertainty.calibration_mode={config['calibration'] == 'Yes'}")
        
        if config.get('calibrated_split'):
            sys.argv.append(f"data.calibrated_split={config['calibrated_split']}")
        if config.get('calibration_method_used'):
            sys.argv.append(f"data.calibration_method_used={config['calibration_method_used']}")

    main()

    try:
        import torch.distributed as dist
        if dist.is_available() and dist.is_initialized():
            dist.destroy_process_group()
    except Exception:
        pass