import sys
import pandas as pd
import numpy as np
import os
import time
import torch
from tqdm import tqdm
import transformers
from pathlib import Path
import json
from transformers import AutoModelForCausalLM, AutoTokenizer
from lm_polygraph.utils.model import WhiteboxModel
from lm_polygraph.utils import estimate_uncertainty
from lm_polygraph.estimators import *

def initialize():
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    os.environ["TRANSFORMERS_VERBOSITY"] = "error"
    transformers.logging.set_verbosity_error()

    model_path = "Qwen/Qwen2.5-1.5B-Instruct"
    base_model = AutoModelForCausalLM.from_pretrained(model_path, device_map="cuda:0")
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    # Note: Ensure lm_polygraph is compatible with this model type
    model = WhiteboxModel(base_model, tokenizer, model_path=model_path)
    return model

def fact_check_claim(claim, ue_method):
    prompt = f"""
    Fact-check the claim using internal knowledge. Provide your answer in the format as the examples below. If your knowledge

    Example 1:
    Claim: "The moon is made of green cheese."
    Verdict: False. Scientific evidence confirms the moon is composed of rock and metal.

    Example 2:
    Claim: "Water boils at 100 degrees Celsius at sea level."
    Verdict: True. This is the standard boiling point of water under normal atmospheric pressure.

    Example 3:
    Claim: {claim}
    Verdict:
    """
    # estimate_uncertainty returns a result object containing 'uncertainty' and 'generation_text'
    ue = estimate_uncertainty(model, ue_method, input_text=prompt) 
    return ue

if __name__ == "__main__":
    model = initialize()
    data_path = Path('../data/QuanTemp/data/raw_data/test_claims_quantemp.json')
    
    with open(data_path, 'r', encoding='utf-8') as file:
        claims = json.load(file)

    sample_size = len(claims)
    # Using a smaller sample for testing is recommended: sample_size = 5

    ue_methods = [MeanTokenEntropy(), MaximumTokenProbability(), MaximumSequenceProbability(), Perplexity()]
    
    # Storage structure
    benchmark_data = {type(m).__name__: {'scores': [], 'times': []} for m in ue_methods}

    print(f"\nBenchmarking {sample_size} claims...")
    print("="*80)

    for i, claim in tqdm(enumerate(claims[:sample_size]), total=sample_size):
        c = claim['claim']
        
        # --- 1. PRINT CLAIM HEADER (Once per claim) ---
        print(f"\n\nCLAIM {i+1}: \"{c}\"")
        print("-" * 80)
        
        for method in ue_methods:
            method_name = type(method).__name__ # Get clean class name
            
            try:
                start_time = time.perf_counter()
                
                with torch.no_grad():
                    result = fact_check_claim(c, method)
                
                end_time = time.perf_counter()
                duration = end_time - start_time

                # --- 2. PROCESS SCORE (Safe Extraction & Transformation) ---
                score = result.uncertainty
                
                # Step A: Convert from Torch/List to a Numpy Array first
                if hasattr(score, 'cpu'):
                    score = score.cpu().detach().numpy()
                elif isinstance(score, list):
                    score = np.array(score)
                
                # Step B: Handle Vector vs Scalar (Aggregation)
                # If the method returns a score per token (array), we average it.
                if type(score) in [np.ndarray] and score.ndim > 0:
                    score = np.mean(score)

                # Step C: Method-Specific Transformations
                # 1. Fix MaximumTokenProbability: Convert Log-Prob (negative) to Probability (0-1)
                if method_name == "MaximumTokenProbability":
                    score = np.exp(score)
                
                # 2. MaximumSequenceProbability often returns NLL (positive high number) or Log-Prob.
                # If your previous result was ~49.0 (NLL), leave it. 
                # If it ever returns negative numbers (Log-Prob), flip it with exp.
                elif method_name == "MaximumSequenceProbability" and score < 0:
                     score = np.exp(score)

                # Final cast to float for CSV/Printing
                score = float(score)

                # --- 3. BEAUTIFIED OUTPUT ---
                # Clean up the response text (remove newlines for cleaner table)
                clean_response = result.generation_text.replace('\n', ' ').strip()
                if len(clean_response) > 80:
                    clean_response = clean_response[:77] + "..."

                print(f"  ➜ {method_name:<25} | Score: {score:.4f} | Time: {duration:.2f}s")
                print(f"    Response: {clean_response}")
                print(f"    {'.'*70}") # Dotted separator between methods

                # Store Data
                benchmark_data[method_name]['times'].append(duration)
                benchmark_data[method_name]['scores'].append(score)

            except Exception as e:
                print(f"  [!] Skipped {method_name}: {e}")
                continue

    # --- SUMMARY & EXPORT ---
    summary_rows = []
    
    for method_name, data in benchmark_data.items():
        if not data['scores']: continue # Skip if empty
        
        scores = np.array(data['scores'])
        times = np.array(data['times'])
        
        row = {
            "Method": method_name,
            "Avg Score": np.mean(scores),
            "Std Dev": np.std(scores),
            "Min": np.min(scores),
            "Max": np.max(scores),
            "Median": np.median(scores),
            "Avg Time": np.mean(times)
        }
        summary_rows.append(row)

    df = pd.DataFrame(summary_rows)
    df = df.round(4)
    
    output_filename = "uq_benchmark_results.csv"
    df.to_csv(output_filename, index=False)
    
    print("\n" + "="*80)
    print("FINAL BENCHMARK RESULTS")
    print("="*80)
    # Use to_string() so pandas prints the whole table without hiding columns
    print(df.to_string(index=False)) 
    print(f"\nSuccessfully saved statistics to '{output_filename}'")

    del model
    torch.cuda.empty_cache()
    sys.exit(0)