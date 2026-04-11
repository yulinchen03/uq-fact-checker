import os
import time
import json
import hydra
from omegaconf import DictConfig
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Load environment variables
load_dotenv()

# Force vLLM to use spawn for multiprocessing workers
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"

from src.data_models import FactCheckSample
from src.modules.decomposer import AtomicDecomposer
from src.utils.llm_client import LocalLLMClient, GeminiLLMClient, OpenAILLMClient

# --- FIXED: Dynamic Path Resolution ---
# __file__ is scripts/experiments/experiment_decomposer.py
ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
EXP_DIR = ROOT_DIR / "decomp_exp" # Output directory for this experiment

def load_scifact(path=None, limit=300):
    if path is None:
        path = DATA_DIR / "scifact" / "claims_val.jsonl"
        
    samples = []
    if path.exists():
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                if len(samples) >= limit:
                    break
                item = json.loads(line)
                samples.append(FactCheckSample(
                    id=f"scifact_{item.get('id', len(samples))}",
                    claim=item['claim'],
                    mode="factscore"
                ))
    else:
        print(f"⚠️ Warning: {path} not found.")
    return samples

def load_quantemp(path=None, limit=300):
    if path is None:
        # Try .jsonl first to match our new unified structure, then fallback to .json
        path = DATA_DIR / "quantemp" / "claims_val.jsonl"
        if not path.exists():
            path = DATA_DIR / "quantemp" / "claims_val.json"
            
    samples = []
    if path.exists():
        with open(path, 'r', encoding='utf-8') as f:
            if path.suffix == '.jsonl':
                for i, line in enumerate(f):
                    if len(samples) >= limit: break
                    if line.strip():
                        item = json.loads(line)
                        samples.append(FactCheckSample(
                            id=f"quantemp_{i}",
                            claim=item['claim'],
                            mode="factscore"
                        ))
            else:
                items = json.load(f)
                for i, item in enumerate(items):
                    if len(samples) >= limit: break
                    samples.append(FactCheckSample(
                        id=f"quantemp_{i}",
                        claim=item['claim'],
                        mode="factscore"
                    ))
    else:
        print(f"⚠️ Warning: {path} not found.")
    return samples

def parse_existing_markdown(md_path):
    """Parses existing markdown to recover state and discard the failed Pro run."""
    detailed_results = {}
    if not md_path.exists():
        return detailed_results
    
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_id = None
    for line in lines:
        line = line.strip()
        if line.startswith("## Sample ID:"):
            current_id = line.replace("## Sample ID:", "").strip()
            detailed_results[current_id] = {"models": {}}
        elif line.startswith("**Original Claim**:"):
            detailed_results[current_id]["original_claim"] = line.replace("**Original Claim**:", "").strip()
        elif line.startswith("|") and len(line.split("|")) >= 4:
            parts = [p.strip() for p in line.split("|")]
            model_name = parts[1]
            
            # Skip headers and the failed Pro model
            if model_name in ["Model", "---", "gemini-3.1-pro-preview"]:
                continue
                
            facts_str = parts[2]
            if facts_str == "*No claims extracted or error*":
                facts = []
            else:
                # Strip numbering and HTML breaks
                facts = [f.split(". ", 1)[-1] for f in facts_str.split("<br>") if ". " in f]
            
            detailed_results[current_id]["models"][model_name] = facts
    return detailed_results

def save_results_to_jsonl(detailed_results, ds_name):
    """Saves the fully merged dataset to JSONL format."""
    EXP_DIR.mkdir(parents=True, exist_ok=True)
    path = EXP_DIR / f"decomposer_results_{ds_name}.jsonl"
    with open(path, 'w', encoding='utf-8') as f:
        for sample_id, data in detailed_results.items():
            record = {
                "id": sample_id,
                "original_claim": data.get("original_claim", ""),
                "models": data.get("models", {})
            }
            f.write(json.dumps(record) + "\n")
    print(f"💾 Raw merged results saved to {path.relative_to(ROOT_DIR)}")

def run_evaluation(decomposer, samples, model_name, dataset_name, detailed_results):
    print(f"\n--- Running {model_name} on {dataset_name} ({len(samples)} samples) ---")
    total_facts = 0
    valid_samples = 0
    for i, sample in enumerate(samples):
        print(f"[{i+1}/{len(samples)}] Processing: {sample.id}")
        
        if sample.id not in detailed_results[dataset_name]:
            detailed_results[dataset_name][sample.id] = {
                "original_claim": sample.claim,
                "models": {}
            }

        print("*"*50)
        print(f"Processing: {sample.claim}")
        print("*"*50)
            
        sample_copy = FactCheckSample(id=sample.id, claim=sample.claim, mode=sample.mode)
        
        try:
            processed = decomposer.process(sample_copy)
            facts = processed.atomic_facts
            print(facts)
            detailed_results[dataset_name][sample.id]["models"][model_name] = facts
            total_facts += len(facts)
            valid_samples += 1
            print(f"  -> Extracted {len(facts)} claims")
        except Exception as e:
            detailed_results[dataset_name][sample.id]["models"][model_name] = []
            print(f"  -> Error processing claim: {e}")
        
        if "gemini" in model_name.lower() or "gpt" in model_name.lower():
            time.sleep(1)  # Throttle APIs slightly to prevent limits
            
    avg_facts = total_facts / valid_samples if valid_samples > 0 else 0
    print(f"--- Completed. Avg facts per claim: {avg_facts:.2f} ---")
    return avg_facts

def plot_results(results, datasets_list, models_list):
    EXP_DIR.mkdir(parents=True, exist_ok=True)
    
    x = np.arange(len(datasets_list))
    width = 0.85 / len(models_list) 
    
    fig, ax = plt.subplots(figsize=(14, 8))

    for i, model in enumerate(models_list):
        avgs = [results[ds].get(model, 0) for ds in datasets_list]
        offset = (i - len(models_list)/2 + 0.5) * width
        rects = ax.bar(x + offset, avgs, width, label=model)
        ax.bar_label(rects, padding=3, fmt='%.2f', fontsize=9) 

    ax.set_ylabel('Avg Decomposed Claims per Original Claim')
    ax.set_title('Decomposition Rate Comparison: Local vs Proprietary Models')
    ax.set_xticks(x)
    ax.set_xticklabels([ds.capitalize() for ds in datasets_list])
    ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1))

    fig.tight_layout()
    plot_path = EXP_DIR / "decomposer_comparison_plot.png"
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    print(f"\n📊 Visualization saved to {plot_path.relative_to(ROOT_DIR)}")

def generate_markdown_reports(detailed_results, models_list):
    EXP_DIR.mkdir(parents=True, exist_ok=True)
    
    for ds_name, data in detailed_results.items():
        if not data:
            continue
            
        md_lines = [f"# {ds_name.capitalize()} Decomposition Comparison\n"]
        
        for sample_id, info in data.items():
            md_lines.append(f"## Sample ID: {sample_id}")
            md_lines.append(f"**Original Claim**: {info.get('original_claim', '')}\n")
            
            md_lines.append("| Model | Decomposed Claims | Count |")
            md_lines.append("|---|---|---|")
            
            for model_name in models_list:
                facts = info.get("models", {}).get(model_name, [])
                count = len(facts)
                if count == 0:
                    facts_str = "*No claims extracted or error*"
                else:
                    facts_html = "<br>".join([f"{idx+1}. {f}" for idx, f in enumerate(facts)])
                    facts_str = facts_html
                
                md_lines.append(f"| {model_name} | {facts_str} | {count} |")
                
            md_lines.append("\n---\n")
            
        report_path = EXP_DIR / f"decomposer_comparison_{ds_name}.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(md_lines))
        print(f"📄 Markdown report overwritten at {report_path.relative_to(ROOT_DIR)}")

# --- FIXED: Hydra Config Path ---
@hydra.main(version_base=None, config_path="../../config", config_name="config")
def main(cfg: DictConfig):
    print("🚀 Initializing Decomposer Run with Markdown State Recovery...")

    datasets = {
        "scifact": load_scifact(limit=300),
        "quantemp": load_quantemp(limit=300)
    }

    # Use the dynamic EXP_DIR
    detailed_results = {
        "scifact": parse_existing_markdown(EXP_DIR / "decomposer_comparison_scifact.md"),
        "quantemp": parse_existing_markdown(EXP_DIR / "decomposer_comparison_quantemp.md")
    }

    # 1. Master List: Determines what gets written to tables and plots
    models_list = [
        # "Qwen/Qwen3-4B-Instruct-2507",
        # "Qwen/Qwen2.5-1.5B-Instruct",
        # "meta-llama/Llama-3.2-1B-Instruct",
        # "meta-llama/Llama-3.2-3B-Instruct",
        # "google/gemma-3-1b-it",
        # "google/gemma-3-4b-it",
        # "gemini-3-flash-preview", 
        # "gemini-3.1-flash-lite-preview",
        # "gemini-2.5-flash-lite",
        # "gemini-2.5-flash", 
        # "gpt-3.5-turbo-0125",
        # "gpt-4.1-mini-2025-04-14",
        # "gpt-5.4-nano-2026-03-17",
        # "gpt-5.4-mini-2026-03-17",
    ]

    local_models = [
        # "Qwen/Qwen3-4B-Instruct-2507",
        # "Qwen/Qwen2.5-1.5B-Instruct",
        # "meta-llama/Llama-3.2-3B-Instruct",
        # "meta-llama/Llama-3.2-1B-Instruct",
        # "google/gemma-3-1b-it",
        # "google/gemma-3-4b-it",
    ]
    
    # 2. Execution Lists
    openai_models_to_run = [
        # "gpt-5.4-nano-2026-03-17", 
        # "gpt-5.4-mini-2026-03-17", 
        # "gpt-4.1-mini-2025-04-14",
        # "gpt-3.5-turbo-0125",
    ]
    
    gemini_models_to_run = [
        # e.g., "gemini-3.1-pro-preview" 
        # "gemini-2.5-flash-lite",
        # "gemini-2.5-flash"
    ]

    # -- EXECUTE LOCAL MODELS ---
    if local_models:
        print("\n" + "="*80)
        print("RUNNING LOCAL MODELS")
        print("="*80)
        
        for l_model in local_models:
            try:
                print(f"\nInitializing {l_model}...")
                l_client = LocalLLMClient(model_name=l_model)
                l_decomposer = AtomicDecomposer(l_client, cfg)
                
                for ds_name, samples in datasets.items():
                    samples_to_run = [
                        s for s in samples 
                        if l_model not in detailed_results[ds_name].get(s.id, {}).get("models", {})
                    ]
                    
                    if samples_to_run:
                        run_evaluation(l_decomposer, samples_to_run, l_model, ds_name, detailed_results)
                    else:
                        print(f"Skipping {ds_name} - completely populated for {l_model}")
                        
                print(f"Cleaning up vLLM resources for {l_model}...")
                l_client.close()
                        
            except Exception as e:
                print(f"Failed to process with {l_model}: {e}")

    # --- EXECUTE OPENAI APIS ---
    if openai_models_to_run:
        print("\n" + "="*80)
        print("RUNNING OPENAI APIS")
        print("="*80)
        
        openai_key = os.environ.get("OPENAI_API_KEY")
        if not openai_key:
            print("⚠️ OPENAI_API_KEY is not set correctly in your .env file. Skipping OpenAI runs...")
        else:
            for o_model in openai_models_to_run:
                try:
                    print(f"\nInitializing {o_model}...")
                    o_client = OpenAILLMClient(model_name=o_model)
                    o_decomposer = AtomicDecomposer(o_client, cfg)
                    
                    for ds_name, samples in datasets.items():
                        samples_to_run = [
                            s for s in samples 
                            if o_model not in detailed_results[ds_name].get(s.id, {}).get("models", {})
                        ]
                        
                        if samples_to_run:
                            run_evaluation(o_decomposer, samples_to_run, o_model, ds_name, detailed_results)
                        else:
                            print(f"Skipping {ds_name} - completely populated for {o_model}")
                            
                except Exception as e:
                    print(f"Failed to process with {o_model}: {e}")

    # --- EXECUTE GEMINI APIS ---
    if gemini_models_to_run:
        print("\n" + "="*80)
        print("RUNNING GEMINI APIS")
        print("="*80)
        
        gemini_key = os.environ.get("GEMINI_API_KEY")
        if not gemini_key or gemini_key == "your_gemini_api_key_here":
            print("⚠️ GEMINI_API_KEY is not set correctly in your .env file. Skipping Gemini runs...")
        else:
            for g_model in gemini_models_to_run:
                try:
                    print(f"\nInitializing {g_model}...")
                    g_client = GeminiLLMClient(model_name=g_model)
                    g_decomposer = AtomicDecomposer(g_client, cfg)
                    
                    for ds_name, samples in datasets.items():
                        samples_to_run = [
                            s for s in samples 
                            if g_model not in detailed_results[ds_name].get(s.id, {}).get("models", {})
                        ]
                        
                        if samples_to_run:
                            run_evaluation(g_decomposer, samples_to_run, g_model, ds_name, detailed_results)
                        else:
                            print(f"Skipping {ds_name} - completely populated for {g_model}")
                            
                except Exception as e:
                    print(f"Failed to process with {g_model}: {e}")

    # --- CALCULATE & PLOT RESULTS ---
    results = {"scifact": {}, "quantemp": {}}
    for ds_name in datasets.keys():
        for model_name in models_list:
            total_facts = 0
            valid_count = 0
            for s_id, data in detailed_results[ds_name].items():
                if model_name in data.get("models", {}):
                    total_facts += len(data["models"][model_name])
                    valid_count += 1
            results[ds_name][model_name] = total_facts / valid_count if valid_count > 0 else 0

    # Dump the merged dictionary to JSONL, save the plot, and rewrite the Markdown
    for ds_name in datasets.keys():
        save_results_to_jsonl(detailed_results[ds_name], ds_name)
        
    plot_results(results, list(datasets.keys()), models_list)
    generate_markdown_reports(detailed_results, models_list)

if __name__ == "__main__":
    main()