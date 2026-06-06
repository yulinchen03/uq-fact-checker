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

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.pipeline_builder import build_pipeline
from src.utils.metrics import MetricsRecorder
from src.utils.loader import LocalDataLoader 
import inspect
import inquirer
import lm_polygraph.estimators as estimators
from transformers import set_seed

os.environ["PYTORCH_ALLOC_CONF"] = "expandable_segments:True"

import multiprocessing as mp
try:
    mp.set_start_method('spawn', force=True)
except RuntimeError:
    pass

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
                      choices=['never_retrieve', 'always_retrieve', 'granular', 'uq_aware', 'uq_decompose', 'openai_never_retrieve', 'openai_always_retrieve']),
        
        inquirer.List('output_format',
                      message="Select the output format",
                      choices=['label_only', 'full_response']),
        
        inquirer.List('uq_method',
                      message="Select the UQ Method for this run",
                      choices=available_estimators,
                      ignore=lambda answers: answers.get('mode') not in ('uq_aware', 'uq_decompose')),

        inquirer.List('calibration', 
                      message="Apply calibration?",
                      choices=['Yes', 'No'],
                      ignore=lambda answers: answers.get('mode') not in ('uq_aware', 'uq_decompose')),

        inquirer.List('calibrated_split',
                      message="Select the data split which was used for calibration",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini'],
                      ignore=lambda answers: answers.get('calibration') == 'Yes' or answers.get('mode') not in ('uq_aware', 'uq_decompose')),

        inquirer.List('check_logic',
                      message="Was the Logic check enabled for this run?",
                      choices=['Yes', 'No']),
                      
        inquirer.List('logic_eval_method',
                      message="Select the Logic evaluation method",
                      choices=['discrete', 'probabilistic'],
                      ignore=lambda answers: answers.get('check_logic') == 'No'),

        inquirer.List('test_split',
                      message="Select the test data split",
                      choices=['train', 'val', 'test', 'train_mini', 'val_mini', 'test_mini'],
                      ignore=lambda answers: answers.get('calibration') == 'Yes'),
    ]

    return inquirer.prompt(questions)


@hydra.main(version_base=None, config_path="../config", config_name="config")
def main(cfg: DictConfig):
    seed = cfg.get("seed", 42)
    lock_random_seeds(seed)
    
    model_name = cfg.llm.model_name.split("/")[-1]
    
    output_format = cfg.get("output_format", "label_only")

    logic_suffix = f"logic_{cfg.get('logic_eval_method', 'discrete')}" if cfg.get('check_logic', False) else f"logic_OFF"
    
    if cfg.mode in ('uq_aware', 'uq_decompose'):
        calib_split = cfg.data.get("calibrated_split", "val")
        
        calibrated_thresh_path = project_root / "run_results" / f"seed_{seed}" / cfg.data.dataset_name / model_name / "calibration" / f"optimal_thresholds_{calib_split}_{output_format}_{logic_suffix}.json"        
        if calibrated_thresh_path.exists():
            with open(calibrated_thresh_path, 'r') as f:
                thresh_data = json.load(f)
                
                if cfg.uncertainty.method in thresh_data:
                    method_data = thresh_data[cfg.uncertainty.method]
                    cfg.uncertainty.threshold = float(method_data.get("optimal_threshold", cfg.uncertainty.threshold))
                    print(f"🎯 Loaded calibrated threshold: {cfg.uncertainty.threshold} for {cfg.uncertainty.method} (from {calib_split} split, {output_format} format)")
                else:
                    print(f"⚠️ UQ method {cfg.uncertainty.method} not found in threshold dict. Using manual threshold: {cfg.uncertainty.threshold}")
        else:
            print(f"⚠️ Calibration file not found at {calibrated_thresh_path}.")
            print(f"Falling back to manual configured threshold: {cfg.uncertainty.threshold}")
    else:
        cfg.uncertainty.method = "UQ module disabled"
        cfg.uncertainty.threshold = 0.0

    print(f"\n🚀 Starting run on {cfg.data.dataset_name} ({cfg.data.split})")
    print(f"Mode: {cfg.mode} | Format: {output_format} | UQ Method: {cfg.uncertainty.method}")
    if cfg.mode in ('uq_aware', 'uq_decompose'):
        print(f"Threshold: {cfg.uncertainty.threshold}")

    loader = LocalDataLoader(data_root=str(project_root / "data"))
    
    dataset = loader.load(dataset_name=cfg.data.dataset_name, split=cfg.data.split, mode=cfg.mode)
    
    pipeline_steps, llm_client = build_pipeline(cfg)

    print("\n-----------------------")
    print(f"Pipeline components:")
    for i, step in enumerate(pipeline_steps):
        print(f"  Step {i+1}: {step.__class__.__name__}")
    print("-----------------------\n")
    
    base_out_dir = project_root / "run_results" / f"seed_{seed}" / cfg.data.dataset_name / model_name
    
    if cfg.mode in ("uq_aware", "uq_decompose"):
        final_dir = base_out_dir / cfg.mode / cfg.uncertainty.method
    else:
        final_dir = base_out_dir / cfg.mode
        
    final_dir.mkdir(parents=True, exist_ok=True)
    
    final_file = final_dir / f"results_{cfg.data.split}_{output_format}_{logic_suffix}.jsonl"

    print(f"Saving results to: {final_file.relative_to(project_root)}")

    open(final_file, 'w').close()
    
    # Pipeline execution loop
    with open(final_file, 'w') as f_out:
        for i, sample in enumerate(tqdm(dataset, desc=f"Running {cfg.data.dataset_name}|{cfg.data.split}|{cfg.mode}|{output_format}")):
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

    print("🧹 Cleaning up vLLM engine and releasing VRAM...")
    try:
        llm_client.close()
        del llm_client
        del pipeline_steps
        del dataset
    except Exception:
        pass
        
    import gc
    gc.collect()

    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    try:
        import torch.distributed as dist
        if dist.is_available() and dist.is_initialized():
            dist.destroy_process_group()
    except Exception:
        pass
        
    print("✨ Engine shut down securely.")
    os._exit(0)

if __name__ == "__main__":
    config = get_experiment_config()
    
    if not config:
        print("Experiment cancelled.")
        sys.exit(0)

    active_split = config.get('test_split', 'train')

    sys.argv.append(f"data={config['dataset']}")
    sys.argv.append(f"data.split={active_split}")
    sys.argv.append(f"mode={config['mode']}")
    
    sys.argv.append(f"output_format={config['output_format']}")

    sys.argv.append(f"check_logic={'True' if config.get('check_logic') == 'Yes' else 'False'}")
    sys.argv.append(f"logic_eval_method={config.get('logic_eval_method', 'discrete')}")
    
    if config['mode'] in ('uq_aware', 'uq_decompose'):
        sys.argv.append(f"uncertainty.method={config['uq_method']}")
        
        if config.get('calibrated_split'):
            sys.argv.append(f"data.calibrated_split={config['calibrated_split']}")

    main()

    try:
        import torch.distributed as dist
        if dist.is_available() and dist.is_initialized():
            dist.destroy_process_group()
    except Exception:
        pass