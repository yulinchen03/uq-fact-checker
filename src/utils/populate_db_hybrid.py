import json
import pickle
import sys
import os
import gc
from pathlib import Path
from collections import defaultdict

import torch
import chromadb
import chromadb.errors
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

import hydra
from omegaconf import DictConfig
import inquirer

os.environ["PYTORCH_ALLOC_CONF"] = "expandable_segments:True"

def get_experiment_config(cfg: DictConfig):
    if not sys.stdout.isatty():
        dataset = cfg.data.get("dataset_name", "scifact").lower()
        if dataset not in ['scifact', 'quantemp']:
            dataset = 'scifact'
        return {'dataset': dataset}

    questions = [
        inquirer.List('dataset',
                      message="Select the dataset to create the hybrid vector DB for",
                      choices=['scifact', 'quantemp']), 
    ]
    return inquirer.prompt(questions)

def load_chunked_corpus(corpus_path: Path):
    if not corpus_path.exists():
        raise FileNotFoundError(f"Chunked corpus not found at: {corpus_path}\nPlease run the chunking script first!")
        
    documents = []
    print(f"Loading chunked corpus from {corpus_path}...")
    with open(corpus_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            try:
                doc = json.loads(line)
                documents.append({
                    "chunk_id": str(doc["chunk_id"]),
                    "source_id": str(doc["source_id"]),
                    "text": str(doc["text"])
                })
            except json.JSONDecodeError:
                continue
    return documents

def get_model_alias(model_name: str) -> str:
    """Maps long HuggingFace repo IDs to clean, short aliases for file paths."""
    aliases = {
        "BAAI/bge-m3": "bge_m3",
        "Qwen/Qwen3-Embedding-0.6B": "qwen_06b",
        "naver/splade-cocondenser-ensembledistil": "splade",
    }
    
    # If the model is in our dictionary, return the nice short name
    if model_name in aliases:
        return aliases[model_name]
        
    # FALLBACK: If you test a new model and forget to add it to the dict,
    # just grab the first 12 characters of the model name so it doesn't crash.
    safe_fallback = model_name.split("/")[-1].replace("-", "").replace(".", "").lower()
    return safe_fallback[:12]

@hydra.main(version_base=None, config_path="../../config", config_name="config")
def main(cfg: DictConfig):
    config = get_experiment_config(cfg)
    
    if not config:
        print("Setup aborted...")
        return
        
    # --- 1. Extract configurations ---
    dataset = config['dataset']
    model_dense = cfg.retriever.get("embedding_model", "BAAI/bge-m3")
    model_sparse = cfg.retriever.get("sparse_model", "naver/splade-cocondenser-ensembledistil") 
    device = cfg.llm.device
    batch_size = cfg.retriever.get("batch_size", 8)
    
    is_bgem3 = "bge-m3" in model_dense.lower()
    
    # --- 2. Dynamic Path Generation ---
    root_path = Path(cfg.data.root_path)
    corpus_path = root_path / dataset / "corpus_chunked.jsonl"
    
    safe_dense = get_model_alias(model_dense)
    
    if is_bgem3:
        combined_name = safe_dense
    else:
        safe_sparse = get_model_alias(model_sparse)
        combined_name = f"{safe_dense}_{safe_sparse}"
        
    db_path = root_path / "vector_db" / f"{dataset}_{combined_name}"
    collection_name = f"{dataset}_{combined_name}_docs"
    sparse_out = db_path / "sparse_index.pkl"

    print(f"\n📁 Target Database Path: {db_path}")
    print(f"📁 Target Collection: {collection_name}")

    # --- 3. Load Data & Initialize DB ---
    documents = load_chunked_corpus(corpus_path)
    print(f"Loaded {len(documents)} chunks for vectorization.")
    
    db_path.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(db_path))
    try:
        client.delete_collection(collection_name)
    except (ValueError, chromadb.errors.NotFoundError):
        pass
    collection = client.create_collection(name=collection_name, metadata={"hnsw:space": "cosine"})

    total = len(documents)
    inverted_index = defaultdict(dict)

    # --- 4. Encoding Logic ---
    if is_bgem3:
        print(f"\n--- SINGLE PASS: Unified Hybrid Encoding ({model_dense}) ---")
        from FlagEmbedding import BGEM3FlagModel
        model_bgem3 = BGEM3FlagModel(model_dense, use_fp16=(device == "cuda"))

        for start in tqdm(range(0, total, batch_size), desc="Encoding Chunks (Dense + Sparse)"):
            batch = documents[start:start + batch_size]
            texts = [d["text"] for d in batch]
            chunk_ids = [d["chunk_id"] for d in batch]
            source_ids = [d["source_id"] for d in batch]

            with open(os.devnull, 'w') as devnull:
                old_stderr = sys.stderr
                sys.stderr = devnull
                try:
                    output = model_bgem3.encode(texts, return_dense=True, return_sparse=True, return_colbert_vecs=False, batch_size=batch_size, max_length=8192)
                finally:
                    sys.stderr = old_stderr

            dense_vecs = output["dense_vecs"].tolist()
            lexical_weights = output["lexical_weights"]

            collection.upsert(
                ids=chunk_ids,
                embeddings=dense_vecs,
                documents=texts,
                metadatas=[{"source_id": sid, "source": dataset} for sid in source_ids]
            )

            for i, weights in enumerate(lexical_weights):
                cid = chunk_ids[i]
                for token_id, weight in weights.items():
                    inverted_index[token_id][cid] = float(weight)

        del model_bgem3
        torch.cuda.empty_cache()
        gc.collect()

    else:
        # Fallback for separate dense/sparse models
        from src.utils.sparse_encoder import SpladeEncoder
        
        print(f"\n--- PASS 1: Dense Encoding ({model_dense}) ---")
        dense_model = SentenceTransformer(model_dense, device=device, trust_remote_code=True)
        dense_model.max_seq_length = 32768

        for start in tqdm(range(0, total, batch_size), desc="Dense Chunk Pass"):
            batch = documents[start:start + batch_size]
            texts = [d["text"] for d in batch]
            chunk_ids = [d["chunk_id"] for d in batch]
            source_ids = [d["source_id"] for d in batch]
            
            dense_vecs = dense_model.encode(texts, batch_size=batch_size, normalize_embeddings=True, show_progress_bar=False).tolist()

            collection.upsert(
                ids=chunk_ids,
                embeddings=dense_vecs,
                documents=texts,
                metadatas=[{"source_id": sid, "source": dataset} for sid in source_ids]
            )
            del dense_vecs

        del dense_model
        torch.cuda.empty_cache()
        gc.collect()

        print(f"\n--- PASS 2: Sparse Encoding ({model_sparse}) ---")
        sparse_model = SpladeEncoder(model_sparse, device=device)

        for start in tqdm(range(0, total, batch_size), desc="Sparse Chunk Pass"):
            batch = documents[start:start + batch_size]
            texts = [d["text"] for d in batch]
            chunk_ids = [d["chunk_id"] for d in batch]

            lexical_weights = sparse_model.encode(texts, max_length=512)

            for i, weights in enumerate(lexical_weights):
                cid = chunk_ids[i]
                for token_id, weight in weights.items():
                    inverted_index[token_id][cid] = float(weight)
            del lexical_weights

        del sparse_model
        torch.cuda.empty_cache()
        gc.collect()

    # --- 5. Serialize Sparse Index ---
    sparse_out.parent.mkdir(parents=True, exist_ok=True)
    with open(sparse_out, 'wb') as f:
        pickle.dump(dict(inverted_index), f, protocol=pickle.HIGHEST_PROTOCOL)
    
    print(f"\n✅ Hybrid chunk index build complete! (Saved to: {db_path})")

if __name__ == "__main__":
    main()