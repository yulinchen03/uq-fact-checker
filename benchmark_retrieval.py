"""
Retrieval Benchmark: Compare Dense vs Hybrid vs Hybrid+Reranker vs Gold

Measures retrieval quality (Recall@K, MRR, Precision@K, Hit Rate) across
retriever modes on the SciFact dataset using claims that have gold evidence
annotations.

New flags vs the original script
─────────────────────────────────
  --reranker-pool-size N    Candidate pool fed into the reranker (default 20).
                            Increase to give the reranker more to work with.

  --reranker-instruction STR  Override the instruction injected into every
                            reranker prompt. Defaults to the SciFact-specific
                            fact-checking instruction (evidential relevance,
                            stance-agnostic). Pass "default" to use the
                            original web-search instruction so you can ablate
                            the instruction effect.

  --debug-reranker          Log per-claim gold-doc rank before and after
                            reranking so you can inspect what the reranker
                            is actually doing.

Usage examples
──────────────
  # Full comparison (dense / hybrid-RRF / hybrid+reranker / gold):
  python benchmark_retrieval.py --split val

  # Ablate reranker instruction — compare scifact vs web-search instruction:
  python benchmark_retrieval.py --split val --reranker-instruction default

  # Debug mode — see gold-doc rank movement per claim:
  python benchmark_retrieval.py --split val --limit 20 --debug-reranker

Output
──────
  - Console comparison table
  - JSON  → results/benchmarks/retrieval_benchmark.json
  - Chart → results/benchmarks/retrieval_comparison.png
"""
import gc
import torch
import json
import argparse
import time
import os
import sys
from tqdm import tqdm
import numpy as np
from pathlib import Path
from collections import defaultdict
from src.modules.retriever import HybridRetriever

os.environ["TOKENIZERS_PARALLELISM"] = "false"

def parse_args():
    parser = argparse.ArgumentParser(description="Benchmark retrieval strategies")
    parser.add_argument("--dataset", type=str, default="scifact", choices=["scifact"])
    parser.add_argument("--split", type=str, default="val")
    parser.add_argument("--limit", type=int, default=0)
    
    # NOW ACCEPTS MULTIPLE K VALUES
    parser.add_argument("--top-k", type=int, nargs="+", default=[1, 2, 3],
                        help="List of final documents returned (e.g., --top-k 1 2 3)")
    
    parser.add_argument("--device", type=str, default="cuda")
    parser.add_argument("--no-plot", action="store_true")
    parser.add_argument("--reranker-pool-size", type=int, default=50)
    parser.add_argument("--reranker-instruction", type=str, default="default")
    parser.add_argument("--debug-reranker", action="store_true")
    parser.add_argument("--save-results-folder", type=str, default="default")
    return parser.parse_args()

def resolve_instruction(value: str) -> str:
    if value == "default":
        from src.modules.retriever import Qwen3Reranker
        return Qwen3Reranker.INSTRUCTION
    if value == "simplified":
        return "Given a claim, retrieve relevant passages that contain evidence for verifying the claim."
    return value

def load_claims(dataset: str, split: str, limit: int = 0):
    claims_path = Path(f"data/scifact/claims_{split}.jsonl")
    claims = []
    with open(claims_path) as f:
        for line in f:
            data = json.loads(line.strip())
            raw_evidence = data.get("evidence", {})
            gold = list(raw_evidence.keys()) if isinstance(raw_evidence, dict) and raw_evidence else data.get("cited_doc_ids", [])
            if not gold: continue
            claims.append({
                "id": str(data.get("id", "")),
                "claim": data.get("claim", ""),
                "gold_doc_ids": [str(g) for g in gold]
            })
    if limit > 0: claims = claims[:limit]
    return claims

def compute_metrics(retrieved_ids: list, gold_ids: list, k_list: list):
    """Calculates metrics for multiple K cutoffs simultaneously."""
    metrics = {}
    gold_set = set(gold_ids)
    for k in k_list:
        k_ids = retrieved_ids[:k] # Slice the list dynamically
        hit = 1 if gold_set.intersection(set(k_ids)) else 0
        recall = len(gold_set.intersection(set(k_ids))) / max(len(gold_set), 1)
        precision = len(gold_set.intersection(set(k_ids))) / max(len(k_ids), 1)
        mrr = 0.0
        for rank, doc_id in enumerate(k_ids, start=1):
            if doc_id in gold_set:
                mrr = 1.0 / rank
                break
        metrics[f"hit@{k}"] = hit
        metrics[f"recall@{k}"] = recall
        metrics[f"precision@{k}"] = precision
        metrics[f"mrr@{k}"] = mrr
    return metrics

def aggregate_metrics(results):
    agg = {}
    if not results: return agg
    for key in results[0].keys():
        agg[key] = float(np.mean([r[key] for r in results]))
    return agg

def _build_hybrid_retriever(args, use_reranker: bool, instruction: str = None, alpha: float = 0.5, architecture: str = "bgem3", dense_model: str = "BAAI/bge-m3", reranker_model: str = None):
    safe_name = dense_model.split("/")[-1].replace("-", "_").replace(".", "_").lower()
    return HybridRetriever(
        collection=f"{args.dataset}_{safe_name}_dense",
        db_path=f"data/vector_db/{args.dataset}_{safe_name}",
        sparse_index_path=f"data/vector_db/{args.dataset}_{safe_name}/sparse_index.pkl",
        model_type=architecture,
        dense_model=dense_model,
        top_k_retrieve=100,
        top_k_rerank=args.reranker_pool_size,
        top_k_final=max(args.top_k), # FETCH MAX K
        rrf_k=60, alpha=alpha, device=args.device, debug=args.debug_reranker,
        use_reranker=use_reranker, reranker_model=reranker_model, reranker_instruction=instruction
    )

def benchmark_gold(claims, args):
    results = []
    for claim in claims:
        results.append(compute_metrics(claim["gold_doc_ids"], claim["gold_doc_ids"], args.top_k))
    return results, 0.0

def benchmark_dense(claims, args, db_path: str, collection: str, model_name: str):
    from src.modules.retriever import VectorDBRetriever
    retriever = VectorDBRetriever(collection=collection, db_path=db_path, embedding_model=model_name, top_k=max(args.top_k), device=args.device)
    results, latencies = [], []
    with open(os.devnull, 'w') as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            for claim in tqdm(claims, desc="  Retrieving", file=sys.stdout, leave=False):
                start = time.time()
                docs = retriever._retrieve(claim["claim"])
                latencies.append(time.time() - start)
                results.append(compute_metrics([doc.source_id for doc in docs], claim["gold_doc_ids"], args.top_k))
        finally: sys.stderr = old_stderr
    return results, np.mean(latencies)

def benchmark_hybrid_rrf_only(claims, args, architecture: str, dense_model: str, alpha: float = 0.5):
    retriever = _build_hybrid_retriever(args, use_reranker=False, alpha=alpha, architecture=architecture, dense_model=dense_model)
    results, latencies = [], []
    with open(os.devnull, 'w') as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            for claim in tqdm(claims, desc=f"  Retrieving (RRF a={alpha})", file=sys.stdout, leave=False):
                start = time.time()
                docs = retriever._retrieve(claim["claim"])
                latencies.append(time.time() - start)
                results.append(compute_metrics([doc.source_id for doc in docs], claim["gold_doc_ids"], args.top_k))
        finally: sys.stderr = old_stderr
    return results, np.mean(latencies)

def benchmark_dense_with_reranker(claims, args, instruction: str, db_path: str, collection: str, model_name: str, reranker_model: str):
    from src.modules.retriever import VectorDBRetriever, Qwen3Reranker
    retriever = VectorDBRetriever(collection=collection, db_path=db_path, embedding_model=model_name, top_k=args.reranker_pool_size, device=args.device)
    reranker = Qwen3Reranker(model_name=reranker_model, instruction=instruction, device=args.device, max_length=4096)
    results, latencies = [], []
    with open(os.devnull, 'w') as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            for claim in tqdm(claims, desc=f"  Dense+Rerank ({reranker_model.split('/')[-1]})", file=sys.stdout, leave=False):
                start = time.time()
                docs = retriever._retrieve(claim["claim"])
                final_docs = reranker.rerank(claim["claim"], docs)[:max(args.top_k)] if docs else []
                latencies.append(time.time() - start)
                results.append(compute_metrics([doc.source_id for doc in final_docs], claim["gold_doc_ids"], args.top_k))
        finally: sys.stderr = old_stderr
    return results, np.mean(latencies)

def benchmark_hybrid_with_reranker(claims, args, instruction: str, architecture: str, dense_model: str, reranker_model: str, alpha: float = 0.5):
    retriever = _build_hybrid_retriever(args, use_reranker=True, instruction=instruction, alpha=alpha, architecture=architecture, dense_model=dense_model, reranker_model=reranker_model)
    results, latencies = [], []
    with open(os.devnull, 'w') as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            for claim in tqdm(claims, desc=f"  Retrieving ({reranker_model.split('/')[-1]})", file=sys.stdout, leave=False):
                start = time.time()
                docs = retriever._retrieve(claim["claim"], gold_ids=claim["gold_doc_ids"])
                latencies.append(time.time() - start)
                results.append(compute_metrics([doc.source_id for doc in docs], claim["gold_doc_ids"], args.top_k))
        finally: sys.stderr = old_stderr
    return results, np.mean(latencies)

def print_comparison_table(all_metrics, latencies, args):
    methods = list(all_metrics.keys())
    display_k = max(args.top_k) # Pick highest K for console display to avoid wrapping
    
    header = f"{'Method':<35} | {'Hit Rate@'+str(display_k):<10} | {'Recall@'+str(display_k):<10} | {'Prec@'+str(display_k):<10} | {'MRR@'+str(display_k):<10} | {'Latency (s)':<12}"
    sep = "=" * len(header)
    print(f"\n{sep}\n{'RETRIEVAL BENCHMARK COMPARISON':^{len(header)}}\n{sep}\n{header}\n{'-' * len(header)}")
    
    for method in methods:
        m = all_metrics[method]
        lat = latencies[method]
        row = f"{method[:33]:<35} | {m[f'hit@{display_k}']:<10.4f} | {m[f'recall@{display_k}']:<10.4f} | {m[f'precision@{display_k}']:<10.4f} | {m[f'mrr@{display_k}']:<10.4f} | {lat:<12.4f}"
        print(row)
    print(sep)

def create_visualization(all_metrics, latencies, save_path, args):
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    import matplotlib
    import os
    matplotlib.use("Agg")
    
    methods = list(all_metrics.keys())
    num_methods = len(methods)
    
    # Dynamic width: ~0.4 inches per method so 41 bars don't squish together
    fig_width = max(12, num_methods * 0.4)
    fig_height = 8 
    
    # Strip the ".png" from the save path so we can add suffixes
    base_path = str(save_path).replace(".png", "")
    
    # ── 1. Quality Metrics (Sorted Descending: Best on the left) ──
    metric_map = {
        "hit": "Hit Rate",
        "recall": f"Recall@{args.top_k}",
        "precision": f"Precision@{args.top_k}",
        "mrr": "MRR"
    }

    for metric_key, title in metric_map.items():
        data = [(m, all_metrics[m][metric_key]) for m in methods]
        # Sort descending so the highest value is first
        data.sort(key=lambda x: x[1], reverse=True) 
        
        sorted_methods = [d[0] for d in data]
        sorted_values = [d[1] for d in data]

        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        
        # ── FIXED: Rank-Based Color Gradient ──
        # Rank 0 gets 1.0 (bright yellow), Rank N gets 0.0 (dark purple)
        num_bars = len(sorted_values)
        if num_bars > 1:
            colors = [cm.viridis(1.0 - (i / (num_bars - 1))) for i in range(num_bars)]
        else:
            colors = [cm.viridis(0.8)]
        
        # Apply the gradient colors to the bars
        bars = ax.bar(sorted_methods, sorted_values, color=colors, edgecolor="black", alpha=0.85)
        
        # Add value labels on top of each bar (rotated to fit 41 bars)
        for bar, val in zip(bars, sorted_values):
            ax.text(bar.get_x() + bar.get_width()/2, val + 0.01, 
                    f"{val:.3f}", ha='center', va='bottom', fontsize=9, rotation=90)

        ax.set_ylabel("Score", fontsize=12)
        ax.set_title(f"Retrieval Quality: {title}", fontsize=14, pad=15)
        ax.set_ylim(0, 1.15) # Leave room on top for the text labels
        ax.grid(axis="y", linestyle="--", alpha=0.7)
        ax.spines[['top', 'right']].set_visible(False)

        # Rotate the long method names so they are readable
        plt.xticks(rotation=45, ha="right", fontsize=10)

        plt.tight_layout()
        out_file = f"{base_path}_{metric_key}.png"
        plt.savefig(out_file, dpi=200, bbox_inches="tight")
        print(f"📊 Saved: {out_file}")
        plt.close(fig)

    # ── 2. Latency (Sorted Ascending: Fastest on the left) ──
    lat_data = [(m, latencies[m]) for m in methods if latencies[m] > 0]
    
    if lat_data:
        # Sort ascending so the lowest latency is first
        lat_data.sort(key=lambda x: x[1])
        
        sorted_lat_methods = [d[0] for d in lat_data]
        sorted_lat_values = [d[1] for d in lat_data]

        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        
        # ── FIXED: Rank-Based Color Gradient for Latency ──
        # Rank 0 (Fastest) gets 1.0 (bright), Rank N (Slowest) gets 0.0 (dark)
        num_lat_bars = len(sorted_lat_values)
        if num_lat_bars > 1:
            lat_colors = [cm.plasma_r(1.0 - (i / (num_lat_bars - 1))) for i in range(num_lat_bars)]
        else:
            lat_colors = [cm.plasma_r(0.8)]
        
        bars = ax.bar(sorted_lat_methods, sorted_lat_values, color=lat_colors, edgecolor="black", alpha=0.85)
        
        max_lat = max(sorted_lat_values) if sorted_lat_values else 1.0
        ax.set_ylim(0, max_lat * 1.25)
        
        for bar, val in zip(bars, sorted_lat_values):
            ax.text(bar.get_x() + bar.get_width()/2, val + (max_lat * 0.01), 
                    f"{val:.3f}s", ha='center', va='bottom', fontsize=9, rotation=90)

        ax.set_ylabel("Average Latency (Seconds)", fontsize=12)
        ax.set_title("Retrieval Latency per Query", fontsize=14, pad=15)
        ax.grid(axis="y", linestyle="--", alpha=0.7)
        ax.spines[['top', 'right']].set_visible(False)

        plt.xticks(rotation=45, ha="right", fontsize=10)

        plt.tight_layout()
        out_file = f"{base_path}_latency.png"
        plt.savefig(out_file, dpi=200, bbox_inches="tight")
        print(f"📊 Saved: {out_file}")
        plt.close(fig)

def main():
    args = parse_args()
    instruction = resolve_instruction(args.reranker_instruction)

    print("=" * 65)
    print(f"    RETRIEVAL BENCHMARK [{args.dataset.upper()}]: Full Configuration Sweep")
    print("=" * 65)

    claims = load_claims(args.dataset, args.split, args.limit)
    if not claims:
        print("No claims with gold evidence found.")
        return
    
    all_metrics: dict = {}
    latencies:   dict = {}

    # ── 1. Define Static Baselines ──
    experiments = [
        {"name": "1. Gold (Upper Bound)", "type": "gold"},
        
        # Dense Only
        {"name": "2. Dense (BGE-M3)", "type": "dense", "model": "BAAI/bge-m3", 
         "db": f"data/vector_db/{args.dataset}_bge_m3", "col": f"{args.dataset}_bge_m3_dense"},
        {"name": "3. Dense (Qwen3-0.6B)", "type": "dense", "model": "Qwen/Qwen3-Embedding-0.6B", 
         "db": f"data/vector_db/{args.dataset}_qwen3_embedding_0_6b", "col": f"{args.dataset}_qwen3_embedding_0_6b_dense"},
        {"name": "4. Dense (Qwen3-4B)", "type": "dense", "model": "Qwen/Qwen3-Embedding-4B", 
         "db": f"data/vector_db/{args.dataset}_qwen3_embedding_4b", "col": f"{args.dataset}_qwen3_embedding_4b_dense"},
        {"name": "5. Dense (Qwen3-8B)", "type": "dense", "model": "Qwen/Qwen3-Embedding-8B", 
         "db": f"data/vector_db/{args.dataset}_qwen3_embedding_8b", "col": f"{args.dataset}_qwen3_embedding_8b_dense"},

        # Sparse Only (Simulated by setting alpha=0.0 in the Hybrid Retriever)
        {"name": "6. Sparse Only (BGE-M3)", "type": "hybrid_rrf", "arch": "bgem3", "dense": "BAAI/bge-m3", "alpha": 0.0},
        {"name": "7. Sparse Only (SPLADE)", "type": "hybrid_rrf", "arch": "qwen-splade", "dense": "Qwen/Qwen3-Embedding-0.6B", "alpha": 0.0},

        # Hybrid RRF Only (alpha=0.5)
        {"name": "8. Hybrid RRF (BGE-M3)", "type": "hybrid_rrf", "arch": "bgem3", "dense": "BAAI/bge-m3", "alpha": 0.5},
        {"name": "9. Hybrid RRF (Qwen3-0.6B+SPLADE)", "type": "hybrid_rrf", "arch": "qwen-splade", "dense": "Qwen/Qwen3-Embedding-0.6B", "alpha": 0.5},
        {"name": "10. Hybrid RRF (Qwen3-4B+SPLADE)", "type": "hybrid_rrf", "arch": "qwen-splade", "dense": "Qwen/Qwen3-Embedding-4B", "alpha": 0.5},
        {"name": "11. Hybrid RRF (Qwen3-8B+SPLADE)", "type": "hybrid_rrf", "arch": "qwen-splade", "dense": "Qwen/Qwen3-Embedding-8B", "alpha": 0.5},
    ]

    # Shared Reranker List
    rerankers = [
        ("0.6B", "Qwen/Qwen3-Reranker-0.6B"),
        ("4B", "Qwen/Qwen3-Reranker-4B"),
        ("8B", "Qwen/Qwen3-Reranker-8B")
    ]

    exp_counter = 12

    # ── 2. Dynamically Generate Dense + Reranker Matrix ──
    denses = [
        ("BGE-M3", "BAAI/bge-m3", f"data/vector_db/{args.dataset}_bge_m3", f"{args.dataset}_bge_m3_dense"),
        ("Qwen3-0.6B", "Qwen/Qwen3-Embedding-0.6B", f"data/vector_db/{args.dataset}_qwen3_embedding_0_6b", f"{args.dataset}_qwen3_embedding_0_6b_dense"),
        ("Qwen3-4B", "Qwen/Qwen3-Embedding-4B", f"data/vector_db/{args.dataset}_qwen3_embedding_4b", f"{args.dataset}_qwen3_embedding_4b_dense"),
        ("Qwen3-8B", "Qwen/Qwen3-Embedding-8B", f"data/vector_db/{args.dataset}_qwen3_embedding_8b", f"{args.dataset}_qwen3_embedding_8b_dense")
    ]

    for d_label, dense_mod, db, col in denses:
        for r_label, reranker_mod in rerankers:
            experiments.append({
                "name": f"{exp_counter}. Dense ({d_label}) + Reranker ({r_label})",
                "type": "dense_rerank",
                "model": dense_mod,
                "db": db,
                "col": col,
                "reranker": reranker_mod
            })
            exp_counter += 1

    # ── 2.5. Dynamically Generate Sparse + Reranker Matrix ──
    # Note: We still pass a "dense" model string because the Hybrid class requires it to initialize, 
    # but alpha=0.0 ensures the dense scores are completely ignored during retrieval.
    sparses = [
        ("BGE-M3 (Sparse)", "bgem3", "BAAI/bge-m3"),
        ("SPLADE", "qwen-splade", "Qwen/Qwen3-Embedding-0.6B") 
    ]

    for s_label, arch, dense_mod in sparses:
        for r_label, reranker_mod in rerankers:
            experiments.append({
                "name": f"{exp_counter}. Sparse ({s_label}) + Reranker ({r_label})",
                "type": "hybrid_rerank",
                "arch": arch,
                "dense": dense_mod,
                "reranker": reranker_mod,
                "alpha": 0.0  # sparse only during rrf
            })
            exp_counter += 1

    # ── 3. Dynamically Generate Hybrid + Reranker Matrix ──
    hybrids = [
        ("BGE-M3", "bgem3", "BAAI/bge-m3"),
        ("Qwen3-0.6B", "qwen-splade", "Qwen/Qwen3-Embedding-0.6B"),
        ("Qwen3-4B", "qwen-splade", "Qwen/Qwen3-Embedding-4B"),
        ("Qwen3-8B", "qwen-splade", "Qwen/Qwen3-Embedding-8B")
    ]

    for h_label, arch, dense_mod in hybrids:
        for r_label, reranker_mod in rerankers:
            experiments.append({
                "name": f"{exp_counter}. Hybrid ({h_label}) + Reranker ({r_label})",
                "type": "hybrid_rerank",
                "arch": arch,
                "dense": dense_mod,
                "reranker": reranker_mod,
                "alpha": 0.5
            })
            exp_counter += 1

    # ── 4. Execute Pipeline ──
    for idx, exp in enumerate(experiments, start=1):
        print(f"\n[{idx}/{len(experiments)}] Running: {exp['name']}...")
        try:
            if exp["type"] == "gold":
                res, lat = benchmark_gold(claims, args)
            
            elif exp["type"] == "dense":
                res, lat = benchmark_dense(claims, args, exp["db"], exp["col"], exp["model"])
                
            elif exp["type"] == "hybrid_rrf":
                res, lat = benchmark_hybrid_rrf_only(claims, args, architecture=exp["arch"], dense_model=exp["dense"], alpha=exp["alpha"])
                
            elif exp["type"] == "dense_rerank":
                res, lat = benchmark_dense_with_reranker(claims, args, instruction, exp["db"], exp["col"], exp["model"], exp["reranker"])

            elif exp["type"] == "hybrid_rerank":
                res, lat = benchmark_hybrid_with_reranker(claims, args, instruction, architecture=exp["arch"], dense_model=exp["dense"], reranker_model=exp["reranker"], alpha=exp["alpha"])

            all_metrics[exp["name"]] = aggregate_metrics(res)
            latencies[exp["name"]] = lat
            
            # Dynamically grab the highest K value for the print statement
            display_k = max(args.top_k) 
            print(f"  ✅ Done. Hit Rate: {all_metrics[exp['name']][f'hit@{display_k}']:.4f}, Latency: {lat:.3f}s")
            
        except Exception as e:
            print(f"  ⚠️  Failed: {e}")
            
        finally:
            # 1. Dismantle vLLM's global state FIRST so it releases its grip on the VRAM
            if exp["type"] in ["hybrid_rerank", "dense_rerank"]:
                try:
                    from vllm.distributed.parallel_state import destroy_model_parallel, destroy_distributed_environment
                    destroy_model_parallel()
                    destroy_distributed_environment()
                except Exception as e:
                    print(f"  ⚠️ vLLM Cleanup warning: {e}")

            # 2. Force Python to destroy the local retriever/reranker objects
            gc.collect()

            # 3. NOW wipe the GPU cache (after all references are truly dead)
            if torch.cuda.is_available():
                torch.cuda.synchronize() # Wait for any lingering GPU processes to halt
                torch.cuda.empty_cache() # Flush the VRAM completely
            
            time.sleep(2)

    # ── Print Results ───────────────────────────────────────────────────
    print_comparison_table(all_metrics, latencies, args)

    # ── Save JSON Results ────────────────────────────────────────────────
    save_dir = Path(f"results/benchmarks/{args.save_results_folder}")
    save_dir.mkdir(parents=True, exist_ok=True)
    
    output = {
        "dataset": args.dataset,
        "split": args.split,
        "num_claims": len(claims),
        "top_k": args.top_k,
        "methods": {
            method: {**all_metrics[method], "avg_latency_seconds": latencies[method]}
            for method in all_metrics
        }
    }
    
    json_path = save_dir / "retrieval_exp.json"
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n📄 Results saved to: {json_path}")
    
    if not args.no_plot and all_metrics:
        try:
            plot_path = save_dir / "retrieval_exp.png"
            create_visualization(all_metrics, latencies, str(plot_path), args)
        except ImportError:
            print("⚠️  matplotlib not available, skipping visualization")

if __name__ == "__main__":
    main()
