import os
import yaml
import hydra
from pathlib import Path
from typing import List
from omegaconf import DictConfig

from src.modules import (
    PipelineComponent, 
    DenseRetriever, 
    GoldRetriever,
    HybridRetriever,
    EvidenceAggregator, 
    LLMVerifier,
    UncertaintyAwarePipeline,
    UQDecomposePipeline,
    AtomicDecomposer,
    GranularVerifier
)

from src.modules.retriever import BaseRetriever, get_model_alias
from src.utils.llm_client import LocalLLMClient, OpenAILLMClient

def _load_retriever(cfg: DictConfig) -> BaseRetriever:
    """Dynamically instantiate the correct retriever based on config."""
    retriever_type = cfg.retriever.get("type", "vector")
    root_path = cfg.data.get("root_path", ".")
    dataset_name = cfg.data.dataset_name
    
    embedding_model = cfg.retriever.get("embedding_model", "Qwen/Qwen3-Embedding-0.6B")
    safe_dense = get_model_alias(embedding_model)
    default_db_path = os.path.join(root_path, "vector_db")
    
    db_path = cfg.retriever.get("db_path") or default_db_path
    collection_name = f"{dataset_name}_{safe_dense}_docs"
    
    if retriever_type == "gold":
        return GoldRetriever(
            dataset_name=dataset_name,
            db_path=db_path,
            collection=collection_name
        )

    elif retriever_type == "hybrid":
        return HybridRetriever(
            dataset_name=cfg.data.dataset_name,
            db_path=db_path,
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
            dense_model=cfg.retriever.get("embedding_model", "Qwen/Qwen3-Embedding-0.6B"),
            sparse_model=cfg.retriever.get("sparse_model", "naver/splade-cocondenser-ensembledistil")
        )

    elif retriever_type == "dense":
        return DenseRetriever(
            dataset_name=dataset_name,
            db_path=db_path,
            dense_model=cfg.retriever.get("embedding_model", "Qwen/Qwen3-Embedding-0.6B"),
            sparse_model=cfg.retriever.get("sparse_model", "naver/splade-cocondenser-ensembledistil"),
            top_k=cfg.retriever.top_k,
            device=cfg.llm.device,
            debug=cfg.retriever.debug
        )

    else:
        raise ValueError(f"Unknown retriever type: {retriever_type}")

def _init_local_llm(cfg: DictConfig) -> LocalLLMClient:
    """Initialize the local vLLM-based LLM client."""
    print(f"Loading Local LLM: {cfg.llm.model_name}...")
    return LocalLLMClient(
        model_name=cfg.llm.model_name, 
        device=cfg.llm.device
    )

def _init_openai_llm(cfg: DictConfig) -> OpenAILLMClient:
    """Initialize the OpenAI API-based LLM client."""
    print(f"Loading OpenAI-Compatible LLM: {cfg.llm.model_name}...")
    return OpenAILLMClient(
        model_name=cfg.llm.model_name,
        base_url=cfg.llm.get("api_base_url", None),
        api_key_env=cfg.llm.get("api_key_env", "OPENAI_API_KEY"),
    )

def build_pipeline(cfg: DictConfig) -> List[PipelineComponent]:
    """Build a pipeline based on configuration."""
    pipeline = []
    
    if cfg.mode == "always_retrieve": 
        llm_client = _init_local_llm(cfg)
        pipeline.append(_load_retriever(cfg))
        pipeline.append(EvidenceAggregator())
        pipeline.append(LLMVerifier(llm_client=llm_client, cfg=cfg))
        
    elif cfg.mode == "never_retrieve":
        llm_client = _init_local_llm(cfg)
        pipeline.append(LLMVerifier(llm_client=llm_client, cfg=cfg))

    elif cfg.mode == "granular":
        llm_client = _init_local_llm(cfg)
        retriever = _load_retriever(cfg)
        
        pipeline.append(AtomicDecomposer(llm_client=llm_client, cfg=cfg))
        pipeline.append(GranularVerifier(
            llm_client=llm_client, 
            retriever=retriever, 
            cfg=cfg
        ))
        
    elif cfg.mode == "uq_aware":
        llm_client = _init_local_llm(cfg)
        model, tokenizer = llm_client.get_backend_objects()
        
        retriever = _load_retriever(cfg)
        aggregator = EvidenceAggregator()
        rag_verifier_tool = LLMVerifier(llm_client=llm_client, cfg=cfg)

        uq_module = UncertaintyAwarePipeline(
            cfg=cfg,
            retriever=retriever,
            aggregator=aggregator,
            rag_verifier=rag_verifier_tool,
            model=model,
            tokenizer=tokenizer
        )
        pipeline.append(uq_module) 

    elif cfg.mode == "uq_decompose":
        llm_client = _init_local_llm(cfg)
        model, tokenizer = llm_client.get_backend_objects()

        retriever = _load_retriever(cfg)
        aggregator = EvidenceAggregator()
        rag_verifier_tool = LLMVerifier(llm_client=llm_client, cfg=cfg)
        decomposer = AtomicDecomposer(llm_client=llm_client, cfg=cfg)

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

    elif cfg.mode == "openai_never_retrieve":
        llm_client = _init_openai_llm(cfg)
        pipeline.append(LLMVerifier(llm_client=llm_client, cfg=cfg))

    elif cfg.mode == "openai_always_retrieve":
        llm_client = _init_openai_llm(cfg)
        pipeline.append(_load_retriever(cfg))
        pipeline.append(EvidenceAggregator())
        pipeline.append(LLMVerifier(llm_client=llm_client, cfg=cfg))
    
    else:
        raise ValueError(f"Unknown mode: {cfg.mode}")
    
    return pipeline, llm_client