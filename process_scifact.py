import json
import os
from pathlib import Path
from tqdm import tqdm

def process_scifact(claims_file_path, corpus_file_path, output_dir):
    print(f"Loading full corpus from {corpus_file_path}...")
    # Load ALL Abstracts first
    full_corpus = {}
    with open(corpus_file_path, 'r', encoding='utf-8') as f:
        for line in tqdm(f):
            doc = json.loads(line)
            full_corpus[str(doc['doc_id'])] = {
                "title": doc['title'],
                "abstract": " ".join(doc['abstract']) # Join sentences
            }

    print("Corpus loaded. Processing claims...")
    processed_claims = []
    referenced_corpus = {} # We will save ONLY the docs that appear in the training set for now
    
    # Process Claims
    with open(claims_file_path, 'r', encoding='utf-8') as f:
        for line in tqdm(f):
            row = json.loads(line)
            
            claim_id = str(row['id'])
            claim_text = row['claim']
            cited_docs = row['cited_doc_ids']
            evidence_map = row['evidence'] 
            
            found_labels = set()
            valid_doc_ids = []
            
            for doc_id in cited_docs:
                doc_id_str = str(doc_id)
                
                if doc_id_str not in full_corpus:
                    continue
                
                referenced_corpus[doc_id_str] = full_corpus[doc_id_str]
                valid_doc_ids.append(doc_id_str)
                
                # Check label
                if doc_id_str in evidence_map:
                    items = evidence_map[doc_id_str]
                    if items:
                        found_labels.add(items[0]['label'])
            
            if "SUPPORT" in found_labels and "CONTRADICT" in found_labels:
                final_verdict = "Partially True"
            elif "SUPPORT" in found_labels:
                final_verdict = "True"
            elif "CONTRADICT" in found_labels:
                final_verdict = "False"
            else:
                final_verdict = "Not Enough Info"

            # Create Entry (IDs ONLY)
            if valid_doc_ids:
                entry = {
                    "id": claim_id,
                    "claim": claim_text,
                    "doc_ids": valid_doc_ids,
                    "label": final_verdict,
                    "dataset": "scifact"
                }
                processed_claims.append(entry)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    claims_out = output_path / "train_claims_scifact.json"
    with open(claims_out, 'w', encoding='utf-8') as f:
        json.dump(processed_claims, f, indent=4)
        
    corpus_out = output_path / "train_corpus_scifact.json"
    with open(corpus_out, 'w', encoding='utf-8') as f:
        json.dump(referenced_corpus, f, indent=4)
    
    print("\nProcessing Complete!")
    print(f"1. Claims saved to: {claims_out}")
    print(f"2. Corpus map saved to: {corpus_out}")
    print(f"   (Saved {len(referenced_corpus)} unique abstracts)")

if __name__ == "__main__":
    CLAIMS_FILE = "data/scifact/claims_train.jsonl" 
    CORPUS_FILE = "data/scifact/corpus.jsonl"
    OUTPUT_DIR = "data/scifact/processed"
    
    process_scifact(CLAIMS_FILE, CORPUS_FILE, OUTPUT_DIR)