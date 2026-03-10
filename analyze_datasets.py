import numpy as np
from transformers import AutoTokenizer
from tqdm import tqdm
import json

import numpy as np
from transformers import AutoTokenizer
from tqdm import tqdm
import json
import os

def load_documents(file_path):
    """Smart loader that handles JSON Arrays, JSON Dicts, and JSONL automatically."""
    print(f"Reading {os.path.basename(file_path)}...")
    
    # Attempt 1: Try reading it as a standard JSON
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            if isinstance(data, list):
                print("Detected standard JSON array format.")
                return data
                
            elif isinstance(data, dict):
                print("Detected standard JSON dictionary format.")
                if not data:
                    return []
                    
                first_val = next(iter(data.values()))
                
                # Case A: Dictionary of Dictionaries (e.g., {"doc1": {"text": "..."}})
                if isinstance(first_val, dict):
                    return list(data.values())
                    
                # Case B: Dictionary of Strings (e.g., QuanTemp: {"0": "text...", "1": "text..."})
                elif isinstance(first_val, str):
                    # Pack them into standard dictionaries so the next loop finds the "content"
                    return [{"id": key, "content": val} for key, val in data.items()]
                    
                else:
                    return [data]
                    
    except json.JSONDecodeError:
        pass # It's not standard JSON, move to Attempt 2
        
    # Attempt 2: Read it line-by-line as JSONL
    data = []
    print("Detected JSONL (JSON Lines) format.")
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip(): # Skip empty blank lines
                data.append(json.loads(line))
    return data

def profile_corpus_tokens(corpus_file_path, model_name="Qwen/Qwen3-4B-Instruct-2507"):
    print(f"Loading tokenizer {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    
    # Use our smart loader!
    documents = load_documents(corpus_file_path)
    lengths = []
    
    for doc in tqdm(documents, desc="Tokenizing Corpus"):
        # Extract title (if it exists) to be perfectly accurate with your RAG prompt
        title = doc.get("title", "")
        
        # Safely extract the main body
        body_data = doc.get("text", "") or doc.get("content", "") or doc.get("abstract", "")
        
        # --- THE FIX: Handle SciFact's list-of-sentences format ---
        if isinstance(body_data, list):
            body = " ".join([str(sentence) for sentence in body_data])
        else:
            body = str(body_data)
            
        # Combine title and body just like your Aggregator does
        full_text = f"Title: {title}\nContent: {body}".strip()
        
        # Count tokens without adding EOS/BOS
        if full_text:
            token_count = len(tokenizer.encode(full_text, add_special_tokens=False))
            lengths.append(token_count)
        
    lengths = np.array(lengths)
    
    # Calculate the crucial 95th Percentile
    p95 = np.percentile(lengths, 95)
    
    print("\n--- Corpus Statistics ---")
    print(f"Total Documents: {len(lengths)}")
    print(f"Mean length:   {np.mean(lengths):.1f} tokens")
    print(f"Median length: {np.median(lengths):.1f} tokens")
    print(f"95th Percentile: {p95:.0f} tokens")
    print(f"Max length:    {np.max(lengths)} tokens")
    
    return p95

# --- How to use it ---
# corpus_p95 = profile_corpus_tokens("data/scifact_

if __name__ == "__main__":
    corpus_file_path = "data/quantemp/corpus.json"
    profile_corpus_tokens(corpus_file_path)

# Example: If your top_k is 3
# max_tokens = 3 * p95