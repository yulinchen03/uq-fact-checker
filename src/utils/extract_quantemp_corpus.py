import json
import os
import re
from pathlib import Path
from tqdm import tqdm

# Import your custom LLM client
from src.utils.llm_client import LocalLLMClient

def split_into_sentences(text: str) -> list:
    """Splits a monolithic block of text into a list of individual sentences."""
    clean_text = re.sub(r'\s+', ' ', text).strip()
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"\'])', clean_text)
    return [s.strip() for s in sentences if s.strip()]

def generate_title(llm_client: LocalLLMClient, text: str) -> str:
    """Uses the LLM to generate a concise title using a Head+Tail truncation strategy."""
    
    # --- 1. Head + Tail Truncation Strategy ---
    words = text.split()
    if len(words) > 400:
        # Grab the first 400 words (the setup/claim) and the last 400 words (the verdict)
        truncated_text = " ".join(words[:400]) + "\n\n... [CONTENT TRUNCATED] ...\n\n" + " ".join(words[-400:])
    else:
        truncated_text = text
    
    # --- 2. Few-Shot Prompt ---
    prompt = (
        "You are an expert editor for a fact-checking database. Your task is to read a fact-check document "
        "and generate a highly concise, descriptive title (maximum 10 to 15 words) that encapsulates the core claim and context. "
        "Respond with STRICTLY the title itself. Do NOT include quotes, preambles, or markdown formatting.\n\n"
        
        "--- EXAMPLES ---\n"
        "Text: The India Today Anti-Fake News War Room found the viral video of Amit Shah's statement was clipped and presented out of context. "
        "A short video clip... [CONTENT TRUNCATED] ...Conclusion: The viral video is clipped. In the original video, Shah says PM Modi "
        "thinks about the welfare of the poor, 24 hours a day.\n"
        "Title: Clipped Video Misrepresents Amit Shah on PM Modi's Working Hours\n\n"
        
        "Text: The first Asia Cup encounter between India and Pakistan was washed away by rain. Against this backdrop, a viral video showing "
        "Pakistani players celebrating... [CONTENT TRUNCATED] ...Therefore, we can conclusively say that the viral video, claiming to show "
        "Pakistani players celebrating the rain-hit match against India in Asia Cup 2023, is misleading.\n"
        "Title: Old Video Falsely Linked to Pakistan Team Celebrating Rain-Hit 2023 Match\n"
        "----------------\n\n"
        
        f"Text:\n{truncated_text}\n"
        "Title:"
    )
    
    try:
        # We cap the output at 50 tokens since it's just a short title
        response = llm_client.generate(prompt, config={"max_new_tokens": 50})
        title = response.get("content", "").strip()
        
        # Clean up any stray quotes the LLM might stubbornly include
        title = title.strip('"').strip("'")
        
        # Fallback if the LLM completely fails
        if not title:
            return "Fact Check Article"
        return title
        
    except Exception as e:
        print(f"\n[Warning] Title generation failed: {e}")
        return "Fact Check Article"

def process_quantemp(data_dir="data/quantemp", model_name="Qwen/Qwen3-4B-Instruct-2507"):
    base_path = Path(data_dir)
    splits = ["claims_train.json", "claims_val.json", "claims_test.json"]
    
    unified_corpus = {}
    text_to_id = {}  
    doc_counter = 1  
    total_claims = 0
    titles_generated = 0
    
    # 1. Initialize the LLM Client
    print("Booting LLM for Title Generation...")
    # NOTE: Set gpu_memory_utilization in your llm_client appropriately for this model!
    llm = LocalLLMClient(model_name=model_name)
    
    for split in splits:
        split_path = base_path / split
        if not split_path.exists():
            print(f"⚠️ Warning: Could not find {split_path}")
            continue
            
        print(f"\nProcessing {split}...")
        with open(split_path, 'r', encoding='utf-8') as f:
            claims = json.load(f)
            
        updated_claims = []
        
        # We use tqdm here to show progress, as LLM generation takes time
        for item in tqdm(claims, desc=f"Extracting {split}"):
            total_claims += 1
            doc_text = item.get("doc", "").strip()
            
            if not doc_text:
                updated_claims.append(item)
                continue
                
            normalized_signature = re.sub(r'\s+', ' ', doc_text.lower()).strip()
            
            # 2. Deduplication & Title Generation
            if normalized_signature in text_to_id:
                # Duplicate article! We already generated a title for this.
                doc_id = text_to_id[normalized_signature]
            else:
                # NEW article! Generate the title.
                generated_title = generate_title(llm, doc_text)
                titles_generated += 1
                
                doc_id = doc_counter
                text_to_id[normalized_signature] = doc_id
                doc_counter += 1
                
                # Format exactly like SciFact
                unified_corpus[doc_id] = {
                    "doc_id": doc_id,                        
                    "title": generated_title,
                    "abstract": split_into_sentences(doc_text), 
                    "structured": False                      
                }

                print(f"Generated title: {generated_title}")
            
            item["cited_doc_ids"] = [doc_id]
            updated_claims.append(item)
            
        with open(split_path, 'w', encoding='utf-8') as f:
            json.dump(updated_claims, f, indent=4)
        print(f"  -> Saved linked claims to {split_path.name}")

    # 3. Save the Unified Corpus
    corpus_path = base_path / "corpus.jsonl"
    print(f"\nSaving Unified Corpus to {corpus_path}...")
    
    with open(corpus_path, 'w', encoding='utf-8') as f:
        for doc in unified_corpus.values():
            f.write(json.dumps(doc) + "\n")
            
    # 4. Clean up VRAM
    llm.close()
            
    print(f"\n✅ Extraction & Generation Complete!")
    print(f"  - Total Claims Processed: {total_claims}")
    print(f"  - Unique Documents Extracted: {len(unified_corpus)}")
    print(f"  - Synthetic Titles Generated: {titles_generated}")
    print(f"  - Unified Corpus Format: SciFact Standard")

if __name__ == "__main__":
    # You can change the model name here to whatever fits comfortably on your GPU
    process_quantemp(model_name="Qwen/Qwen3-4B-Instruct-2507")