import json
import statistics
from pathlib import Path

def calculate_corpus_stats(file_path: str):
    path = Path(file_path)
    if not path.exists():
        print(f"❌ Error: Could not find {path}")
        return

    lengths = []
    claims_below_1200 = []
    
    print(f"Analyzing {path.name}...")
    
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
                
            doc = json.loads(line)
            
            # Handle the SciFact format where text is a list of sentences in 'abstract'
            if "abstract" in doc and isinstance(doc["abstract"], list):
                text = " ".join(doc["abstract"])
            # Fallback just in case the raw text is stored differently
            elif "text" in doc:
                text = str(doc["text"])
            else:
                text = ""
                
            # Calculate word count (splitting by whitespace)
            word_count = len(text.split())
            if word_count < 800:
                claims_below_1200.append(doc)
            lengths.append(word_count)

    if not lengths:
        print("No documents found to analyze.")
        return

    # Calculate statistics
    min_len = min(lengths)
    max_len = max(lengths)
    mean_len = statistics.mean(lengths)
    median_len = statistics.median(lengths)
    total_docs = len(lengths)
    print(f"% Claims below 1200 words: {100 * len(claims_below_1200)/total_docs:.2f}% or {len(claims_below_1200)}/{len(lengths)} documents")

    # Print results
    print("\n📊 Corpus Length Statistics (in words)")
    print("-" * 40)
    print(f"Total Documents: {total_docs:,}")
    print(f"Min Length:      {min_len:,} words")
    print(f"Max Length:      {max_len:,} words")
    print(f"Mean Length:     {mean_len:.2f} words")
    print(f"Median Length:   {median_len:.2f} words")
    print("-" * 40)

if __name__ == "__main__":
    corpus_file = "data/scifact/corpus.jsonl"
    calculate_corpus_stats(corpus_file)