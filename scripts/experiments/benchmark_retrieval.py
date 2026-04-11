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
"""
import gc
import torch
import json
import argparse
import time
import os
import sys
import subprocess
from pathlib import Path

# --- NEW: Dynamic Path Resolution ---
# __file__ is scripts/experiments/benchmark_retrieval.py
project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from tqdm import tqdm
import numpy as np
from collections import defaultdict
from src.modules.retriever import HybridRetriever, VectorDBRetriever, QwenReranker

os.environ["TOKENIZERS_PARALLELISM"] = "false"

def parse_args():
    parser = argparse.ArgumentParser(description="Benchmark retrieval strategies")
    parser.add_argument("--dataset", type=str, default="scifact", choices=["scifact"])
    parser.add_argument("--split", type=str, default="val")
    parser.add_argument("--limit", type=int, default=0)
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
        return QwenReranker.INSTRUCTION
    if value == "simplified":
        return "Given a claim, retrieve relevant passages that contain evidence for verifying the claim."
    return value

def load_claims(dataset: str, split: str, limit: int = 0):
    claims_path = project_root / "data" / dataset / f"claims_{split}.jsonl"
    
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

def compute_metrics(retrieved_items: list, gold_ids: list, k_list: list):
    """
    FIXED: K-Aware Chunk Deduplication.
    Slices the top K chunks first, then extracts unique source_ids to simulate exactly 
    what the LLM context window will see before calculating metrics.
    """
    metrics = {}
    gold_set = set(gold_ids)
    
    for k in k_list:
        # 1. Take exactly the top K retrieved chunks/items
        k_items = retrieved_items[:k]
        
        # 2. Extract unique parent document IDs in rank order
        k_ids = []
        seen = set()
        for item in k_items:
            # Safely handle raw strings (Gold) or Document objects (Vector/Hybrid)
            doc_id = item if isinstance(item, str) else getattr(item, 'source_id', str(item))
            if doc_id not in seen:
                seen.add(doc_id)
                k_ids.append(doc_id)
                
        # 3. Compute Metrics based on unique documents in the context
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
    return HybridRetriever(
        dataset_name=args.dataset,
        root_path=str(project_root / "data"),
        model_type=architecture,
        dense_model=dense_model,
        sparse_model="naver/splade-cocondenser-ensembledistil",
        top_k_retrieve=100,
        top_k_rerank=args.reranker_pool_size,
        top_k_final=max(args.top_k),
        rrf_k=60, alpha=alpha, device=args.device, debug=args.debug_reranker,
        use_reranker=use_reranker, reranker_model=reranker_model, reranker_instruction=instruction
    )

def benchmark_gold(claims, args):
    results = []
    for claim in claims:
        # Pass the raw IDs, compute_metrics handles string vs objects now
        results.append(compute_metrics(claim["gold_doc_ids"], claim["gold_doc_ids"], args.top_k))
    return results, 0.0

def benchmark_dense(claims, args, model_name: str):
    retriever = VectorDBRetriever(
        dataset_name=args.dataset,
        root_path=str(project_root / "data"),
        dense_model=model_name, 
        sparse_model="naver/splade-cocondenser-ensembledistil" if "bge-m3" not in model_name.lower() else "",
        top_k=max(args.top_k), 
        device=args.device
    )
    results, latencies = [], []
    with open(os.devnull, 'w') as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            for claim in tqdm(claims, desc="  Retrieving", file=sys.stdout, leave=False):
                start = time.time()
                docs = retriever._retrieve(claim["claim"])
                latencies.append(time.time() - start)
                results.append(compute_metrics(docs, claim["gold_doc_ids"], args.top_k))
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
                results.append(compute_metrics(docs, claim["gold_doc_ids"], args.top_k))
        finally: sys.stderr = old_stderr
    return results, np.mean(latencies)

def benchmark_dense_with_reranker(claims, args, instruction: str, model_name: str, reranker_model: str):
    retriever = VectorDBRetriever(
        dataset_name=args.dataset,
        root_path=str(project_root / "data"),
        dense_model=model_name, 
        sparse_model="naver/splade-cocondenser-ensembledistil" if "bge-m3" not in model_name.lower() else "",
        top_k=args.reranker_pool_size, 
        device=args.device
    )
    reranker = QwenReranker(model_name=reranker_model, instruction=instruction, device=args.device, max_length=4096)
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
                results.append(compute_metrics(final_docs, claim["gold_doc_ids"], args.top_k))
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
                results.append(compute_metrics(docs, claim["gold_doc_ids"], args.top_k))
        finally: sys.stderr = old_stderr
    return results, np.mean(latencies)

def print_comparison_table(all_metrics, latencies, args):
    methods = list(all_metrics.keys())
    display_k = max(args.top_k) 
    
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
    matplotlib.use("Agg")
    
    methods = list(all_metrics.keys())
    num_methods = len(methods)
    fig_width = max(12, num_methods * 0.4)
    fig_height = 8 
    base_path = str(save_path).replace(".png", "")
    
    display_k = max(args.top_k)

    metric_map = {
        f"hit@{display_k}": "Hit Rate",
        f"recall@{display_k}": f"Recall@{display_k}",
        f"precision@{display_k}": f"Precision@{display_k}",
        f"mrr@{display_k}": f"MRR@{display_k}"
    }

    for metric_key, title in metric_map.items():
        data = [(m, all_metrics[m][metric_key]) for m in methods]
        data.sort(key=lambda x: x[1], reverse=True) 
        
        sorted_methods = [d[0] for d in data]
        sorted_values = [d[1] for d in data]

        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        
        num_bars = len(sorted_values)
        if num_bars > 1:
            colors = [cm.viridis(1.0 - (i / (num_bars - 1))) for i in range(num_bars)]
        else:
            colors = [cm.viridis(0.8)]
        
        bars = ax.bar(sorted_methods, sorted_values, color=colors, edgecolor="black", alpha=0.85)
        
        for bar, val in zip(bars, sorted_values):
            ax.text(bar.get_x() + bar.get_width()/2, val + 0.01, 
                    f"{val:.3f}", ha='center', va='bottom', fontsize=9, rotation=90)

        ax.set_ylabel("Score", fontsize=12)
        ax.set_title(f"Retrieval Quality: {title}", fontsize=14, pad=15)
        ax.set_ylim(0, 1.15) 
        ax.grid(axis="y", linestyle="--", alpha=0.7)
        ax.spines[['top', 'right']].set_visible(False)

        plt.xticks(rotation=45, ha="right", fontsize=10)
        plt.tight_layout()
        out_file = f"{base_path}_{metric_key}.png"
        plt.savefig(out_file, dpi=200, bbox_inches="tight")
        print(f"📊 Saved: {out_file}")
        plt.close(fig)

    # ── Latency (Sorted Ascending) ──
    lat_data = [(m, latencies[m]) for m in methods if latencies[m] > 0]
    
    if lat_data:
        lat_data.sort(key=lambda x: x[1])
        
        sorted_lat_methods = [d[0] for d in lat_data]
        sorted_lat_values = [d[1] for d in lat_data]

        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        
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

    # --- FIXED: Removed hardcoded db paths, added dynamic routing ---
    experiments = [
        {"name": "1. Gold (Upper Bound)", "type": "gold"},
        
        # Dense Only
        {"name": "2. Dense (BGE-M3)", "type": "dense", "model": "BAAI/bge-m3"},
        {"name": "3. Dense (Qwen3-0.6B)", "type": "dense", "model": "Qwen/Qwen3-Embedding-0.6B"},
        # {"name": "4. Dense (Qwen3-4B)", "type": "dense", "model": "Qwen/Qwen3-Embedding-4B"},
        # {"name": "5. Dense (Qwen3-8B)", "type": "dense", "model": "Qwen/Qwen3-Embedding-8B"},

        # Sparse Only (Simulated by setting alpha=0.0 in the Hybrid Retriever)
        {"name": "6. Sparse Only (BGE-M3)", "type": "hybrid_rrf", "arch": "bgem3", "dense": "BAAI/bge-m3", "alpha": 0.0},
        {"name": "7. Sparse Only (SPLADE)", "type": "hybrid_rrf", "arch": "qwen-splade", "dense": "Qwen/Qwen3-Embedding-0.6B", "alpha": 0.0},

        # Hybrid RRF Only (alpha=0.5)
        {"name": "8. Hybrid RRF (BGE-M3)", "type": "hybrid_rrf", "arch": "bgem3", "dense": "BAAI/bge-m3", "alpha": 0.5},
        {"name": "9. Hybrid RRF (Qwen3-0.6B+SPLADE)", "type": "hybrid_rrf", "arch": "qwen-splade", "dense": "Qwen/Qwen3-Embedding-0.6B", "alpha": 0.5},
        # {"name": "10. Hybrid RRF (Qwen3-4B+SPLADE)", "type": "hybrid_rrf", "arch": "qwen-splade", "dense": "Qwen/Qwen3-Embedding-4B", "alpha": 0.5},
        # {"name": "11. Hybrid RRF (Qwen3-8B+SPLADE)", "type": "hybrid_rrf", "arch": "qwen-splade", "dense": "Qwen/Qwen3-Embedding-8B", "alpha": 0.5},
    ]

    # Shared Reranker List
    rerankers = [
        # ("0.6B", "Qwen/Qwen3-Reranker-0.6B"),
        # ("4B", "Qwen/Qwen3-Reranker-4B"),
        # ("8B", "Qwen/Qwen3-Reranker-8B")
    ]

    exp_counter = 12

    # ── Dynamically Generate Dense + Reranker Matrix ──
    denses = [
        # ("BGE-M3", "BAAI/bge-m3"),
        # ("Qwen3-0.6B", "Qwen/Qwen3-Embedding-0.6B"),
        # ("Qwen3-4B", "Qwen/Qwen3-Embedding-4B"),
        # ("Qwen3-8B", "Qwen/Qwen3-Embedding-8B")
    ]

    for d_label, dense_mod in denses:
        for r_label, reranker_mod in rerankers:
            experiments.append({
                "name": f"{exp_counter}. Dense ({d_label}) + Reranker ({r_label})",
                "type": "dense_rerank",
                "model": dense_mod,
                "reranker": reranker_mod
            })
            exp_counter += 1

    # ── Dynamically Generate Sparse + Reranker Matrix ──
    sparses = [
        # ("BGE-M3 (Sparse)", "bgem3", "BAAI/bge-m3"),
        # ("SPLADE", "qwen-splade", "Qwen/Qwen3-Embedding-0.6B") 
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

    # ── Dynamically Generate Hybrid + Reranker Matrix ──
    hybrids = [
        # ("BGE-M3", "bgem3", "BAAI/bge-m3"),
        # ("Qwen3-0.6B", "qwen-splade", "Qwen/Qwen3-Embedding-0.6B"),
        # ("Qwen3-4B", "qwen-splade", "Qwen/Qwen3-Embedding-4B"),
        # ("Qwen3-8B", "qwen-splade", "Qwen/Qwen3-Embedding-8B")
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
                res, lat = benchmark_dense(claims, args, exp["model"])
                
            elif exp["type"] == "hybrid_rrf":
                res, lat = benchmark_hybrid_rrf_only(claims, args, architecture=exp["arch"], dense_model=exp["dense"], alpha=exp["alpha"])
                
            elif exp["type"] == "dense_rerank":
                res, lat = benchmark_dense_with_reranker(claims, args, instruction, exp["model"], exp["reranker"])

            elif exp["type"] == "hybrid_rerank":
                res, lat = benchmark_hybrid_with_reranker(claims, args, instruction, architecture=exp["arch"], dense_model=exp["dense"], reranker_model=exp["reranker"], alpha=exp["alpha"])

            all_metrics[exp["name"]] = aggregate_metrics(res)
            latencies[exp["name"]] = lat
            
            display_k = max(args.top_k) 
            print(f"  ✅ Done. Hit Rate: {all_metrics[exp['name']][f'hit@{display_k}']:.4f}, Latency: {lat:.3f}s")
            
        except Exception as e:
            print(f"  ⚠️  Failed: {e}")
            
        finally:
            if exp["type"] in ["hybrid_rerank", "dense_rerank"]:
                try:
                    from vllm.distributed.parallel_state import destroy_model_parallel, destroy_distributed_environment
                    destroy_model_parallel()
                    destroy_distributed_environment()
                except Exception as e:
                    print(f"  ⚠️ vLLM Cleanup warning: {e}")

            gc.collect()

            if torch.cuda.is_available():
                torch.cuda.synchronize()
                torch.cuda.empty_cache()
            
            time.sleep(2)

    # ── Print Results ──
    print_comparison_table(all_metrics, latencies, args)

    # ── Save JSON Results ──
    save_dir = project_root / "results" / "benchmarks" / args.save_results_folder
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
    print(f"\n📄 Results saved to: {json_path.relative_to(project_root)}")
    
    if not args.no_plot and all_metrics:
        try:
            plot_path = save_dir / "retrieval_exp.png"
            create_visualization(all_metrics, latencies, str(plot_path), args)

            # ── Create Visualization Dashboard ──
            vis_script = project_root / "scripts" / "visualization" / "vis_retrieval_exp.py"
            if vis_script.exists():
                print("\n🎨 Creating visualization dashboard...")
                max_k = str(max(args.top_k))
                vis_cmd = [
                    sys.executable, str(vis_script),
                    "--top-k", max_k,
                    "--save-results-folder", args.save_results_folder
                ]
                try:
                    subprocess.run(vis_cmd, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"⚠️ Visualization script failed with error: {e}")
            else:
                print(f"⚠️ Visualization script not found at {vis_script.relative_to(project_root)}")
        except ImportError:
            print("⚠️  matplotlib not available, skipping visualization")

if __name__ == "__main__":
    main()