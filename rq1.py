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
                      choices=['never_retrieve', 'always_retrieve', 'uq_aware']),
        
        inquirer.List('uq_method',
                      message="Select the UQ Method for this run",
                      choices=available_estimators,
                      ignore=lambda answers: answers.get('mode') != 'uq_aware'),

        inquirer.List('calibration', 
                      message="Apply calibration?",
                      choices=['Yes', 'No'],
                      ignore=lambda answers: answers.get('mode') != 'uq_aware'),

        inquirer.Text('tolerance',
                      message="For calibration, enter the max acceptable accuracy drop from full RAG (delta, e.g., 0.05 for 5%)",
                      validate=validate_float,
                      default="0.05",
                      ignore=lambda answers: answers.get('calibration') != 'Yes'),

        inquirer.List('calibration_split',
                      message="Select the data split for calibration",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini'],
                      ignore=lambda answers: answers.get('calibration') != 'Yes'),

        inquirer.List('calibrated_split',
                      message="Select the data split which was used for calibration",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini'],
                      ignore=lambda answers: answers.get('calibration') == 'Yes' or answers.get('mode') != 'uq_aware'),

        inquirer.List('test_split',
                      message="Select the test data split",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini'],
                      ignore=lambda answers: answers.get('calibration') == 'Yes'),
    ]

    return inquirer.prompt(questions)


@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg: DictConfig):
    lock_random_seeds(42)
    
    if cfg.data.dataset_name == "scifact":
        cfg.retriever.db_path = "./data/vector_db/scifact"
        cfg.retriever.collection_name = "scifact_docs"
    elif cfg.data.dataset_name == "quantemp":
        cfg.retriever.db_path = "./data/vector_db/quantemp"
        cfg.retriever.collection_name = "quantemp_docs"
    else:
        raise ValueError(f"Unsupported dataset: {cfg.data.dataset_name}")
    
    model_name = cfg.llm.model_name.split("/")[1]
    
    if cfg.mode == 'uq_aware':
        if not cfg.uncertainty.calibration_mode:
            # Dynamically fetch the split the user said they calibrated on
            calib_split = cfg.data.calibrated_split
            calibrated_thresh_path = Path(f"results/RQ1/{cfg.data.dataset_name}/{model_name}/calibration/{cfg.uncertainty.method}/optimal_threshold_{calib_split}.json")
            
            if calibrated_thresh_path.exists():
                with open(calibrated_thresh_path, 'r') as f:
                    thresh_data = json.load(f)
                    cfg.uncertainty.threshold = float(thresh_data.get("optimal_threshold", cfg.uncertainty.threshold))
                print(f"🎯 Loaded calibrated threshold: {cfg.uncertainty.threshold} for {cfg.uncertainty.method} (from {calib_split} split)")
            else:
                print(f"⚠️ Calibration file not found at {calibrated_thresh_path}.")
                print(f"Falling back to manual configured threshold: {cfg.uncertainty.threshold}")
    else:
        # Default fallbacks for non-UQ modes
        cfg.uncertainty.method = "UQ module disabled"
        cfg.uncertainty.threshold = 0.0
        cfg.uncertainty.calibration_mode = False 

    # 3. Print Execution Summary
    print(f"\n🚀 Starting run on {cfg.data.dataset_name} ({cfg.data.split})")
    print(f"Mode: {cfg.mode} | UQ Method: {cfg.uncertainty.method}")
    print(f"Using evidence token limit of {cfg.aggregator.max_context_tokens} tokens.")
    if cfg.mode == 'uq_aware':
        print(f"Threshold: {cfg.uncertainty.threshold} | Calibration Mode: {cfg.uncertainty.calibration_mode}")

    # 4. Initialize Loader & Data
    loader = LocalDataLoader(data_root=cfg.data.root_path)
    dataset = loader.load(dataset_name=cfg.data.dataset_name, split=cfg.data.split)
    
    # 5. Build Pipeline
    pipeline_steps = build_pipeline(cfg)

    print("\n-----------------------")
    print(f"Pipeline components:")
    for i, step in enumerate(pipeline_steps):
        print(f"  Step {i+1}: {step.__class__.__name__}")
    print("-----------------------\n")
    
    # 6. Define Output Path
    if cfg.uncertainty.calibration_mode:
        output_dir = Path("results/RQ1") / cfg.data.dataset_name / model_name / "calibration" / cfg.uncertainty.method
    elif cfg.mode == "uq_aware":
        output_dir = Path("results/RQ1") / cfg.data.dataset_name / model_name / "uq_aware" / cfg.uncertainty.method
    else:
        output_dir = Path("results/RQ1") / cfg.data.dataset_name / model_name / cfg.mode
        
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save the file using the active split being run right now
    output_file = output_dir / f"results_{cfg.data.split}.jsonl"
    print(f"Saving results to: {output_file}")

    # Empty the results file before starting
    open(output_file, 'w').close()
    
    # 7. Execution Loop
    with open(output_file, 'w') as f_out:
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

if __name__ == "__main__":
    config = get_experiment_config()
    
    if not config:
        print("Experiment cancelled.")
        sys.exit(0)

    # 1. Determine the active split mapping for the DataLoader
    if config.get('calibration') == 'Yes':
        active_split = config['calibration_split']
    else:
        active_split = config['test_split']

    # 2. Dynamically override Hydra's defaults via sys.argv
    sys.argv.append(f"data={config['dataset']}")
    sys.argv.append(f"data.split={active_split}")
    sys.argv.append(f"mode={config['mode']}")
    
    if config['mode'] == 'uq_aware':
        sys.argv.append(f"uncertainty.method={config['uq_method']}")
        sys.argv.append(f"uncertainty.calibration_mode={config['calibration'] == 'Yes'}")
        
        # Inject the historical calibration split so main() can find the file
        if config.get('calibrated_split'):
            sys.argv.append(f"data.calibrated_split={config['calibrated_split']}")

    # Launch Hydra (do not pass custom arguments directly here)
    main()

    try:
        import torch.distributed as dist
        if dist.is_available() and dist.is_initialized():
            dist.destroy_process_group()
    except Exception:
        pass