import os
import json
import numpy as np
from pathlib import Path
from transformers import AutoTokenizer
from tqdm import tqdm
import inquirer

# --- Dynamic Path Resolution ---
ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"

def get_corpus_files(answers):
    """Dynamically fetches corpus files based on the chosen dataset."""
    dataset_dir = DATA_DIR / answers['dataset']
    files = [f.name for f in dataset_dir.glob("corpus*.json*")]
    return files if files else ["❌ NO FILES FOUND (Press Enter to exit)"]

def get_config():
    """Interactive CLI to select the dataset, the specific file, and tokenizer."""
    questions = [
        inquirer.List('dataset',
                      message="Select the dataset to analyze",
                      choices=['scifact', 'quantemp']),
        
        # Uses the callable to dynamically populate choices based on 'dataset'
        inquirer.List('filename',
                      message="Which stage of the corpus do you want to analyze?",
                      choices=get_corpus_files),
        
        inquirer.Text('model_name',
                      message="Enter the tokenizer model name to use",
                      default="Qwen/Qwen3-4B-Instruct-2507")
    ]
    
    answers = inquirer.prompt(questions)
    
    # Safety catch if they exited or no files were found
    if not answers or "NO FILES FOUND" in answers['filename']:
        return None
        
    return answers

def load_documents(file_path: Path):
    """Smart loader that handles JSON Arrays, JSON Dicts, and JSONL automatically."""
    print(f"\nReading {file_path.name}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            if isinstance(data, list):
                print("Detected standard JSON array format.")
                return data
                
            elif isinstance(data, dict):
                print("Detected standard JSON dictionary format.")
                if not data: return []
                first_val = next(iter(data.values()))
                
                if isinstance(first_val, dict):
                    return list(data.values())
                elif isinstance(first_val, str):
                    return [{"id": key, "content": val} for key, val in data.items()]
                else:
                    return [data]
                    
    except json.JSONDecodeError:
        pass 
        
    data = []
    print("Detected JSONL (JSON Lines) format.")
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip(): 
                data.append(json.loads(line))
    return data

def profile_corpus_tokens(corpus_file_path: Path, model_name: str):
    print(f"\nLoading tokenizer {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    
    documents = load_documents(corpus_file_path)
    lengths = []
    
    for doc in tqdm(documents, desc="Tokenizing Corpus"):
        # Safely extract title (if it exists yet)
        title = doc.get("title", "")
        
        # Safely extract the main body
        body_data = doc.get("text", "") or doc.get("content", "") or doc.get("abstract", "")
        
        # Handle SciFact's list-of-sentences format safely
        if isinstance(body_data, list):
            body = " ".join([str(sentence) for sentence in body_data])
        else:
            body = str(body_data)
            
        # Combine them just like the Aggregator does
        if title:
            full_text = f"Title: {title}\nContent: {body}".strip()
        else:
            full_text = body.strip()
        
        # Count tokens
        if full_text:
            token_count = len(tokenizer.encode(full_text, add_special_tokens=False))
            lengths.append(token_count)
        
    lengths = np.array(lengths)
    
    if len(lengths) == 0:
        print("❌ No documents found or parsed correctly.")
        return
    
    p95 = np.percentile(lengths, 95)
    
    print("\n" + "="*40)
    print(f"{'CORPUS STATISTICS':^40}")
    print("="*40)
    print(f"File Analyzed:   {corpus_file_path.name}")
    print(f"Total Documents: {len(lengths):,}")
    print(f"Mean length:     {np.mean(lengths):.1f} tokens")
    print(f"Median length:   {np.median(lengths):.1f} tokens")
    print(f"95th Percentile: {p95:.0f} tokens")
    print(f"Max length:      {np.max(lengths):,} tokens")
    print("="*40 + "\n")

if __name__ == "__main__":
    config = get_config()
    if not config:
        exit(0)
        
    target_corpus = DATA_DIR / config['dataset'] / config['filename']
    profile_corpus_tokens(target_corpus, config['model_name'])