import json
import pickle
import argparse
import gc
import sys
import os
from pathlib import Path
from collections import defaultdict
import torch
import chromadb
import chromadb.errors
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForMaskedLM, AutoTokenizer

from src.modules.sparse_encoder import SpladeEncoder

from huggingface_hub import snapshot_download

def parse_args():
    parser = argparse.ArgumentParser(description="Build hybrid dense+sparse index")
    parser.add_argument("--dataset", type=str, default="scifact", choices=["scifact", "quantemp"])
    parser.add_argument("--model-type", type=str, default="qwen-splade", choices=["bgem3", "qwen-splade"])
    
    # Model configuration parameters
    parser.add_argument("--model-bgem3", type=str, default="BAAI/bge-m3", help="HuggingFace ID for unified model")
    parser.add_argument("--model-dense", type=str, default="Qwen/Qwen3-Embedding-0.6B", help="HuggingFace ID for dense model")
    parser.add_argument("--model-sparse", type=str, default="naver/splade-cocondenser-ensembledistil", help="HuggingFace ID for sparse model")
    
    parser.add_argument("--corpus-path", type=str, default=None)
    parser.add_argument("--db-path", type=str, default=None)
    parser.add_argument("--collection-name", type=str, default=None)
    parser.add_argument("--sparse-out", type=str, default=None)
    
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    
    args = parser.parse_args()
    
    # ── Dynamic Path Generation based on Specific Model ──
    if args.model_type == "bgem3":
        base_model_name = args.model_bgem3.split("/")[-1]
    else:
        base_model_name = args.model_dense.split("/")[-1]
        
    # Convert "Qwen3-Embedding-0.6B" to "qwen3_embedding_0_6b"
    safe_name = base_model_name.replace("-", "_").replace(".", "_").lower()
    
    if args.corpus_path is None: 
        ext = "jsonl" if args.dataset == "scifact" else "json"
        args.corpus_path = f"data/{args.dataset}/corpus.{ext}"
        
    if args.db_path is None: 
        args.db_path = f"data/vector_db/{args.dataset}_{safe_name}"
        
    if args.collection_name is None: 
        args.collection_name = f"{args.dataset}_{safe_name}_dense"
        
    if args.sparse_out is None: 
        args.sparse_out = f"data/vector_db/{args.dataset}_{safe_name}/sparse_index.pkl"
    
    return args


def load_corpus_jsonl(corpus_path: str):
    documents = []
    with open(corpus_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            try:
                doc = json.loads(line)
                doc_id = str(doc.get("doc_id") or doc.get("_id") or doc.get("id"))
                title = doc.get("title", "")
                text_raw = doc.get("abstract") or doc.get("text") or doc.get("content") or ""
                text_body = " ".join(text_raw) if isinstance(text_raw, list) else str(text_raw)
                full_text = f"Title: {title}\nContent: {text_body}".strip()
                documents.append({"doc_id": doc_id, "title": title, "full_text": full_text})
            except json.JSONDecodeError:
                continue
    return documents


def load_corpus_keyvalue(corpus_path: str):
    print(f"Loading key-value JSON from {corpus_path}...")
    with open(corpus_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    documents = []
    for doc_id, text in data.items():
        doc_id = str(doc_id)
        if isinstance(text, dict):
            title = text.get("title", "")
            body = text.get("text") or text.get("content") or text.get("abstract") or ""
            full_text = f"Title: {title}\nContent: {body}".strip()
        else:
            title = ""
            full_text = str(text)
        documents.append({"doc_id": doc_id, "title": title, "full_text": full_text})
    return documents


def build_index(args):
    corpus_path = Path(args.corpus_path)
    if args.dataset == "quantemp":
        documents = load_corpus_keyvalue(str(corpus_path))
    else:
        documents = load_corpus_jsonl(str(corpus_path))
    print(f"Loaded {len(documents)} documents.")
    
    db_path = Path(args.db_path)
    db_path.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(db_path))
    try:
        client.delete_collection(args.collection_name)
    except (ValueError, chromadb.errors.NotFoundError):
        pass
    collection = client.create_collection(name=args.collection_name, metadata={"hnsw:space": "cosine"})

    batch_size = args.batch_size
    total = len(documents)
    inverted_index = defaultdict(dict)

    if args.model_type == "bgem3":
        print(f"\n--- SINGLE PASS: Unified Encoding ({args.model_bgem3}) ---")
        from FlagEmbedding import BGEM3FlagModel
        print(f"Loading {args.model_bgem3} on {args.device}...")
        model_bgem3 = BGEM3FlagModel(args.model_bgem3, use_fp16=(args.device == "cuda"))

        for start in tqdm(range(0, total, batch_size), desc="Encoding (Dense + Sparse)"):
            batch = documents[start:start + batch_size]
            texts = [d["full_text"] for d in batch]
            doc_ids = [d["doc_id"] for d in batch]
            titles = [d["title"] for d in batch]

            with open(os.devnull, 'w') as devnull:
                old_stderr = sys.stderr
                sys.stderr = devnull
                try:
                    output = model_bgem3.encode(
                        texts, return_dense=True, return_sparse=True, return_colbert_vecs=False, batch_size=batch_size, max_length=512
                    )
                finally:
                    sys.stderr = old_stderr

            dense_vecs = output["dense_vecs"].tolist()
            lexical_weights = output["lexical_weights"]

            collection.upsert(
                ids=doc_ids,
                embeddings=dense_vecs,
                documents=texts,
                metadatas=[{"title": t, "source": args.dataset} for t in titles]
            )

            for i, weights in enumerate(lexical_weights):
                did = doc_ids[i]
                for token_id, weight in weights.items():
                    inverted_index[token_id][did] = float(weight)

        del model_bgem3
        torch.cuda.empty_cache()
        gc.collect()

    else:
        # --- PASS 1: Dense Encoding ---
        print(f"\n--- PASS 1: Dense Encoding ({args.model_dense}) ---")
        print(f"Loading {args.model_dense} on {args.device}...")
        
        safe_repo_name = "models--" + args.model_dense.replace("/", "--")
        snapshot_dir = f"/hf_cache/hub/{safe_repo_name}/snapshots"
        
        try:
            # Manually grab the hash folder (e.g., '0437e45...')
            hash_folder = os.listdir(snapshot_dir)[0]
            local_model_path = os.path.join(snapshot_dir, hash_folder)
        except Exception:
            # Fallback just in case
            local_model_path = args.model_dense 
            
        # Feed the physical directory directly to SentenceTransformer
        dense_model = SentenceTransformer(local_model_path, device=args.device, trust_remote_code=True)
        dense_model.max_seq_length = 512

        for start in tqdm(range(0, total, batch_size), desc="Dense Pass"):
            batch = documents[start:start + batch_size]
            texts = [d["full_text"] for d in batch]
            doc_ids = [d["doc_id"] for d in batch]
            titles = [d["title"] for d in batch]
            
            dense_vecs = dense_model.encode(texts, batch_size=batch_size, normalize_embeddings=True, show_progress_bar=False).tolist()

            collection.upsert(
                ids=doc_ids,
                embeddings=dense_vecs,
                documents=texts,
                metadatas=[{"title": t, "source": args.dataset} for t in titles]
            )
            del dense_vecs

        print("Clearing Dense Model from VRAM...")
        del dense_model
        torch.cuda.empty_cache()
        gc.collect()

        # --- PASS 2: Sparse Encoding ---
        print(f"\n--- PASS 2: Sparse Encoding ({args.model_sparse}) ---")
        print(f"Loading {args.model_sparse} on {args.device}...")
        sparse_model = SpladeEncoder(args.model_sparse, device=args.device)

        for start in tqdm(range(0, total, batch_size), desc="Sparse Pass"):
            batch = documents[start:start + batch_size]
            texts = [d["full_text"] for d in batch]
            doc_ids = [d["doc_id"] for d in batch]

            lexical_weights = sparse_model.encode(texts, max_length=512)

            for i, weights in enumerate(lexical_weights):
                did = doc_ids[i]
                for token_id, weight in weights.items():
                    inverted_index[token_id][did] = float(weight)
            del lexical_weights

        print("Clearing Sparse Model from VRAM...")
        del sparse_model
        torch.cuda.empty_cache()
        gc.collect()

    # ── Final Serialize ──
    sparse_out = Path(args.sparse_out)
    sparse_out.parent.mkdir(parents=True, exist_ok=True)
    with open(sparse_out, 'wb') as f:
        pickle.dump(dict(inverted_index), f, protocol=pickle.HIGHEST_PROTOCOL)
    
    print(f"\n✅ Hybrid index build complete! (Saved to: {args.db_path})")

if __name__ == "__main__":
    args = parse_args()
    build_index(args)