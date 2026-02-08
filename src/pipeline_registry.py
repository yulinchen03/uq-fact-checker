import yaml
import hydra
from pathlib import Path
from typing import List
from omegaconf import DictConfig

from src.modules import (
    PipelineComponent, 
    IdentityGenerator, 
    VectorDBRetriever, 
    SimpleConcatAggregator, 
    LLMVerifier
)

from src.utils.llm_client import LocalLLMClient

def build_pipeline(cfg: DictConfig) -> List[PipelineComponent]:
    """Build a pipeline based on configuration."""
    pipeline = []
    
    # Hydra changes the working directory. We must use get_original_cwd() to find the config.
    try:
        original_cwd = Path(hydra.utils.get_original_cwd())
        prompts_path = original_cwd / "config" / "prompts.yaml"
    except (ValueError, ImportError):
        # Fallback if not running via Hydra (e.g. testing script directly)
        prompts_path = Path("config/prompts.yaml")

    if not prompts_path.exists():
        print(f"Warning: {prompts_path} not found. Verifier might fail.")
        prompt_templates = {}
    else:
        with open(prompts_path, 'r') as f:
            prompt_templates = yaml.safe_load(f)

    # 3. Initialize LLM Client ONCE
    print(f"Loading LLM: {cfg.llm.model_name}...")
    llm_client = LocalLLMClient(
        model_name=cfg.llm.model_name, 
        device=cfg.llm.device
    )
    
    # 4. Build Components
    if cfg.mode == "always_retrieve":
        pipeline.append(IdentityGenerator())
        
        # Pass all required config args to Retriever
        pipeline.append(VectorDBRetriever(
            db_path=cfg.retriever.db_path,
            embedding_model=cfg.retriever.embedding_model,
            top_k=cfg.retriever.top_k,
            device=cfg.llm.device,
            debug=cfg.retriever.debug
        ))
        
        pipeline.append(SimpleConcatAggregator(
            max_tokens=cfg.aggregator.get("max_context_tokens", 2000)
        ))
        
    elif cfg.mode == "never_retrieve":
        pass
        
    elif cfg.mode == "UQ-aware":
        pass 
        
    else:
        raise ValueError(f"Unknown mode: {cfg.mode}")
    
    # 5. Add Verifier
    pipeline.append(LLMVerifier(
        llm_client=llm_client, 
        prompt_templates=prompt_templates,
        cfg=cfg,
    ))
    
    return pipeline