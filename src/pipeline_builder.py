import yaml
import hydra
from pathlib import Path
from typing import List
from omegaconf import DictConfig

from src.modules import (
    PipelineComponent, 
    VectorDBRetriever, 
    EvidenceAggregator, 
    LLMVerifier,
    UncertaintyAwarePipeline
)

from src.utils.llm_client import LocalLLMClient

def build_pipeline(cfg: DictConfig) -> List[PipelineComponent]:
    """Build a pipeline based on configuration."""
    pipeline = []

    # 3. Initialize LLM Client ONCE
    print(f"Loading LLM: {cfg.llm.model_name}...")
    llm_client = LocalLLMClient(
        model_name=cfg.llm.model_name, 
        device=cfg.llm.device
    )
    
    # 4. Build Components
    if cfg.mode == "always_retrieve": 
        # Pass all required config args to Retriever
        pipeline.append(VectorDBRetriever(
            collection=cfg.retriever.collection_name,
            db_path=cfg.retriever.db_path,
            embedding_model=cfg.retriever.embedding_model,
            top_k=cfg.retriever.top_k,
            device=cfg.llm.device,
            debug=cfg.retriever.debug
        ))
        
        pipeline.append(EvidenceAggregator(
            max_tokens=cfg.aggregator.get("max_context_tokens", 2000)
        ))

        pipeline.append(LLMVerifier(
            llm_client=llm_client, 
            cfg=cfg,
        ))
        
    elif cfg.mode == "never_retrieve":
        pipeline.append(LLMVerifier(
        llm_client=llm_client, 
        cfg=cfg,
    ))
        
    elif cfg.mode == "uq_aware":

        model, tokenizer = llm_client.get_backend_objects()
        
        # 1. Instantiate Tools
        # Tool A: Retriever
        retriever_tool = VectorDBRetriever(
            collection=cfg.retriever.collection_name,
            db_path=cfg.retriever.db_path,
            embedding_model=cfg.retriever.embedding_model,
            top_k=cfg.retriever.top_k,
            device=cfg.llm.device,
            debug=cfg.retriever.debug
        )
        
        # Tool B: Aggregator
        aggregator = EvidenceAggregator(
            max_tokens=2000, 
            tokenizer=tokenizer
        )
        
        # Tool C: RAG Verifier
        rag_verifier_tool = LLMVerifier(llm_client=llm_client, cfg=cfg)

        model, tokenizer = llm_client.get_backend_objects()
        
        # 2. Instantiate the Orchestrator
        uq_module = UncertaintyAwarePipeline(
            cfg=cfg,
            retriever=retriever_tool,
            aggregator=aggregator,
            rag_verifier=rag_verifier_tool,
            model=model,
            tokenizer=tokenizer
        )
        
        # 3. Add ONLY the orchestrator to the pipeline
        pipeline.append(uq_module) 
        
    else:
        raise ValueError(f"Unknown mode: {cfg.mode}")
    
    return pipeline