import os
import hydra
import json
import logging
import time
from pathlib import Path  # <--- Essential for path handling
from omegaconf import DictConfig
from tqdm import tqdm
from dotenv import load_dotenv
from src.pipeline_registry import build_pipeline
from src.utils.metrics import MetricsRecorder
from src.data.loader import LocalDataLoader 

load_dotenv()
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
logging.getLogger("chromadb").setLevel(logging.ERROR)
logging.getLogger("transformers").setLevel(logging.ERROR)
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg: DictConfig):
    # 1. Initialize Loader & Data
    loader = LocalDataLoader(data_root=cfg.data.root_path)
    print(f"Loading dataset: {cfg.data.dataset_name} ({cfg.data.split})...")
    dataset = loader.load(dataset_name=cfg.data.dataset_name, split=cfg.data.split)
    
    # 2. Build Pipeline
    pipeline_steps = build_pipeline(cfg)

    # --- INSPECTION BLOCK ---
    print("\n-----------------------")
    print(f"Pipeline for: {cfg.mode}")
    for i, step in enumerate(pipeline_steps):
        print(f"  Step {i+1}: {step.__class__.__name__}")
    print("-----------------------\n")
    
    # 3. Define Output Path
    # Structure: results/RQ1/<dataset>/<mode>/results_<split>.jsonl
    output_dir = Path("results/RQ1") / cfg.data.dataset_name / cfg.mode
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / f"results_{cfg.data.split}.jsonl"
    
    print(f"Running Experiment: {cfg.experiment_name} | Mode: {cfg.mode} | Data Split: {cfg.data.split}")
    print(f"Saving results to: {output_file}")
    
    # 4. Execution Loop
    with open(output_file, 'w') as f_out:
        for i, sample in enumerate(tqdm(dataset)):
            sample.mode = cfg.mode 
            
            # --- START TIMER ---
            start_time = time.perf_counter()
            
            # --- RUN PIPELINE ---
            for component in pipeline_steps:
                try:
                    component.process(sample)
                except Exception as e:
                    print(f"Error processing claim {sample.id}: {e}")
                    sample.explanation = f"Pipeline Error: {str(e)}"
            
            # --- STOP TIMER ---
            end_time = time.perf_counter()
            
            # --- SAVE LATENCY ---
            if hasattr(sample, 'metrics'):
                sample.metrics.latency_seconds = end_time - start_time
            
            # --- SAVE RESULT ---
            f_out.write(sample.model_dump_json() + "\n")
            f_out.flush() 

if __name__ == "__main__":
    main()