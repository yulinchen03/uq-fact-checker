import json
import numpy as np
from pathlib import Path
from transformers import AutoTokenizer
from tqdm import tqdm

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"

def analyze_chunk_sizes(dataset_name, tokenizer_name="Qwen/Qwen3-4B-Instruct-2507"):
    file_path = DATA_DIR / dataset_name / "corpus_chunked.jsonl"
    
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        return

    print(f"\nLoading tokenizer {tokenizer_name}...")
    try:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, trust_remote_code=True)
    except Exception as e:
        print(f"Error loading tokenizer: {e}")
        tokenizer = None

    print(f"\nAnalyzing chunk sizes for {dataset_name} ({file_path.name})...")
    
    char_lengths = []
    word_lengths = []
    token_lengths = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in tqdm(f, desc=f"Processing {dataset_name}"):
                if not line.strip():
                    continue
                data = json.loads(line)
                text = data.get("text", "")
                
                if not text:
                    continue
                    
                char_lengths.append(len(text))
                word_lengths.append(len(text.split()))
                
                if tokenizer:
                    # Count tokens
                    tokens = tokenizer.encode(text, add_special_tokens=False)
                    token_lengths.append(len(tokens))
                    
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return

    if not char_lengths:
        print(f"❌ No valid text chunks found in {dataset_name}.")
        return

    char_lengths = np.array(char_lengths)
    word_lengths = np.array(word_lengths)
    
    print("\n" + "="*50)
    print(f"{'CHUNK SIZE STATISTICS: ' + dataset_name.upper():^50}")
    print("="*50)
    print(f"Total Chunks: {len(char_lengths):,}")
    
    print(f"\n[ Words ]")
    print(f"  Mean:   {np.mean(word_lengths):.1f}")
    print(f"  Median: {np.median(word_lengths):.1f}")
    print(f"  Min:    {np.min(word_lengths)}")
    print(f"  Max:    {np.max(word_lengths)}")
    print(f"  95th P: {np.percentile(word_lengths, 95):.0f}")

    if token_lengths:
        token_lengths = np.array(token_lengths)
        print(f"\n[ Tokens ({tokenizer_name}) ]")
        print(f"  Mean:   {np.mean(token_lengths):.1f}")
        print(f"  Median: {np.median(token_lengths):.1f}")
        print(f"  Min:    {np.min(token_lengths)}")
        print(f"  Max:    {np.max(token_lengths)}")
        print(f"  95th P: {np.percentile(token_lengths, 95):.0f}")

    print("="*50 + "\n")

if __name__ == "__main__":
    datasets = ["scifact", "quantemp"]
    for ds in datasets:
        analyze_chunk_sizes(ds)
