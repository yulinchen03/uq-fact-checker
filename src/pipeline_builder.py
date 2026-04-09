import yaml
import hydra
from pathlib import Path
from typing import List
from omegaconf import DictConfig

from src.modules import (
    PipelineComponent, 
    VectorDBRetriever, 
    GoldRetriever,
    HybridRetriever,
    EvidenceAggregator, 
    LLMVerifier,
    UncertaintyAwarePipeline,
    UQDecomposePipeline,
    AtomicDecomposer,
    FactScoreVerifier
)

from src.modules.retriever import BaseRetriever
from src.utils.llm_client import LocalLLMClient

def _load_retriever(cfg: DictConfig) -> BaseRetriever:
    """Helper to dynamically instantiate the correct retriever based on config."""
    retriever_type = cfg.retriever.get("type", "vector")
    
    if retriever_type == "gold":
        return GoldRetriever(
            dataset_name=cfg.data.dataset_name,
            db_path=cfg.retriever.db_path,
            collection=cfg.retriever.collection_name
        )
    elif retriever_type == "hybrid":
        return HybridRetriever(
            collection=cfg.retriever.hybrid_collection_name,
            db_path=cfg.retriever.hybrid_db_path,
            sparse_index_path=cfg.retriever.sparse_index_path,
            top_k_retrieve=cfg.retriever.top_k_retrieve,
            top_k_final=cfg.retriever.top_k_final,
            rrf_k=cfg.retriever.rrf_k,
            alpha=cfg.retriever.get("alpha", 0.5),
            device=cfg.llm.device,
            debug=cfg.retriever.debug
        )
    else:
        return VectorDBRetriever(
            collection=cfg.retriever.collection_name,
            db_path=cfg.retriever.db_path,
            embedding_model=cfg.retriever.embedding_model,
            top_k=cfg.retriever.top_k,
            device=cfg.llm.device,
            debug=cfg.retriever.debug
        )

def build_pipeline(cfg: DictConfig) -> List[PipelineComponent]:
    """Build a pipeline based on configuration."""
    pipeline = []

    # vLLM has a strict maximum context length.
    # We must reserve tokens for the generation (max_new_tokens) and the prompt template.
    max_model_len = cfg.llm.get("max_model_len", 4096)  
    max_new_tokens = cfg.llm.get("max_new_tokens", 256)
    template_buffer = 512  # prompt template

    # Calculate exactly how much room is left for the evidence
    safe_evidence_limit = max_model_len - max_new_tokens - template_buffer

    # Prevent negative values if config is misconfigured
    safe_evidence_limit = max(safe_evidence_limit, 500) 

    print(f"Using evidence token limit of {safe_evidence_limit} tokens.")
    context_limit = safe_evidence_limit

    # 3. Initialize LLM Client
    print(f"Loading LLM: {cfg.llm.model_name}...")
    llm_client = LocalLLMClient(
        model_name=cfg.llm.model_name, 
        device=cfg.llm.device
    )
    
    # 4. Build Components
    if cfg.mode == "always_retrieve": 
        # --- Dynamically load Vector or Gold retriever ---
        pipeline.append(_load_retriever(cfg))
        
        pipeline.append(EvidenceAggregator(
            max_tokens=context_limit
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
        # Tool A: Retriever (Dynamically load Vector or Gold retriever)
        retriever = _load_retriever(cfg)
        
        # Tool B: Aggregator
        aggregator = EvidenceAggregator(
            max_tokens=context_limit, 
            tokenizer=tokenizer
        )
        
        # Tool C: RAG Verifier
        rag_verifier_tool = LLMVerifier(llm_client=llm_client, cfg=cfg)

        # 2. Instantiate the Orchestrator
        uq_module = UncertaintyAwarePipeline(
            cfg=cfg,
            retriever=retriever,
            aggregator=aggregator,
            rag_verifier=rag_verifier_tool,
            model=model,
            tokenizer=tokenizer
        )
        
        # 3. Add ONLY the orchestrator to the pipeline
        pipeline.append(uq_module) 
        
    elif cfg.mode == "factscore":
        
        # Tool A: Retriever (Dynamically load Vector or Gold retriever)
        retriever = _load_retriever(cfg)
        
        # Tool B: Decomposer (Breaks down claim into atomic facts)
        pipeline.append(AtomicDecomposer(
            llm_client=llm_client, 
            cfg=cfg
        ))
        
        # Tool C: FactScore Verifier (Loops through facts, retrieves, and aggregates)
        pipeline.append(FactScoreVerifier(
            llm_client=llm_client, 
            retriever=retriever, 
            cfg=cfg,
            max_tokens=context_limit
        ))

    elif cfg.mode == "uq_decompose":

        model, tokenizer = llm_client.get_backend_objects()

        # Tool A: Retriever
        retriever = _load_retriever(cfg)

        # Tool B: Aggregator
        aggregator = EvidenceAggregator(
            max_tokens=context_limit,
            tokenizer=tokenizer
        )

        # Tool C: RAG Verifier
        rag_verifier_tool = LLMVerifier(llm_client=llm_client, cfg=cfg)

        # Tool D: Decomposer
        decomposer = AtomicDecomposer(llm_client=llm_client, cfg=cfg)

        # Orchestrator
        uq_decompose_module = UQDecomposePipeline(
            cfg=cfg,
            retriever=retriever,
            aggregator=aggregator,
            rag_verifier=rag_verifier_tool,
            decomposer=decomposer,
            model=model,
            tokenizer=tokenizer
        )

        pipeline.append(uq_decompose_module)
    
    else:
        raise ValueError(f"Unknown mode: {cfg.mode}")
    
    return pipeline