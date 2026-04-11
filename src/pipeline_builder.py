import os
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

from src.modules.retriever import BaseRetriever, get_model_alias
from src.utils.llm_client import LocalLLMClient

def _load_retriever(cfg: DictConfig) -> BaseRetriever:
    """Helper to dynamically instantiate the correct retriever based on config."""
    retriever_type = cfg.retriever.get("type", "vector")
    root_path = cfg.data.get("root_path", ".")
    dataset_name = cfg.data.dataset_name
    
    if retriever_type == "gold":
        embedding_model = cfg.retriever.get("embedding_model", "Qwen/Qwen3-Embedding-0.6B")
        safe_dense = get_model_alias(embedding_model)
        db_path = os.path.join(root_path, "vector_db", f"{dataset_name}_{safe_dense}")
        collection_name = f"{dataset_name}_{safe_dense}_docs"
        
        return GoldRetriever(
            dataset_name=dataset_name,
            db_path=db_path,
            collection=collection_name
        )

    elif retriever_type == "hybrid":
        return HybridRetriever(
            dataset_name=cfg.data.dataset_name,
            root_path=root_path,
            model_type=cfg.retriever.get("model_type", "qwen-splade"),
            top_k_retrieve=cfg.retriever.top_k_retrieve,
            top_k_rerank=cfg.retriever.top_k_rerank,
            top_k_final=cfg.retriever.top_k_final,
            rrf_k=cfg.retriever.rrf_k,
            alpha=cfg.retriever.get("alpha", 0.5),
            device=cfg.llm.device,
            debug=cfg.retriever.debug,
            use_reranker=cfg.retriever.get("use_reranker", True),
            reranker_model=cfg.retriever.get("reranker_model", "Qwen/Qwen3-Reranker-0.6B"),
            dense_model=cfg.retriever.get("dense_model", "Qwen/Qwen3-Embedding-0.6B"),
            sparse_model=cfg.retriever.get("sparse_model", "naver/splade-cocondenser-ensembledistil")
        )
    else: # 'vector'
        return VectorDBRetriever(
            dataset_name=dataset_name,
            root_path=root_path,
            dense_model=cfg.retriever.get("embedding_model", "Qwen/Qwen3-Embedding-0.6B"),
            sparse_model=cfg.retriever.get("sparse_model", "naver/splade-cocondenser-ensembledistil"),
            top_k=cfg.retriever.top_k,
            device=cfg.llm.device,
            debug=cfg.retriever.debug
        )

def build_pipeline(cfg: DictConfig) -> List[PipelineComponent]:
    """Build a pipeline based on configuration."""
    pipeline = []

    # 3. Initialize LLM Client
    print(f"Loading LLM: {cfg.llm.model_name}...")
    llm_client = LocalLLMClient(
        model_name=cfg.llm.model_name, 
        device=cfg.llm.device
    )
    
    # 4. Build Components
    if cfg.mode == "always_retrieve": 
        # First, Retrieve
        pipeline.append(_load_retriever(cfg))
        
        # Then, aggregate evidence
        pipeline.append(EvidenceAggregator())

        # Finally, verify claim with evidence
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
        aggregator = EvidenceAggregator()
        
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
            cfg=cfg
        ))

    elif cfg.mode == "uq_decompose":

        model, tokenizer = llm_client.get_backend_objects()

        # Tool A: Retriever
        retriever = _load_retriever(cfg)

        # Tool B: Aggregator
        aggregator = EvidenceAggregator()

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