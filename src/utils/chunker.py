import json
from pathlib import Path
from tqdm import tqdm

def chunk_document(doc_id: str, title: str, sentences: list, target_words=450, overlap_words=60) -> list:
    """
    Splits a list of sentences into overlapping chunks, optimized for long-context 
    embedding models (BGE-M3, Qwen) while avoiding semantic dilution.
    """
    chunks = []
    current_chunk_sentences = []
    current_word_count = 0
    overlap_word_count = 0
    chunk_idx = 1

    for sentence in sentences:
        sentence_words = len(sentence.split())

        current_chunk_sentences.append(sentence)
        current_word_count += sentence_words

        # Once we hit our target length, save the chunk and create the overlap
        if current_word_count >= target_words:
            chunk_text = " ".join(current_chunk_sentences)
            final_text = f"Title: {title}\nContent: {chunk_text}" if title else f"Content: {chunk_text}"
            
            chunks.append({
                "chunk_id": f"{doc_id}_chunk{chunk_idx}",
                "source_id": str(doc_id),
                "text": final_text
            })
            chunk_idx += 1

            # Backtrack to build the overlap for the next chunk using a word budget
            overlap_sentences = []
            overlap_word_count = 0
            for prev_sent in reversed(current_chunk_sentences):
                # Add complete sentences to the overlap until we hit the budget threshold
                if overlap_word_count + len(prev_sent.split()) > overlap_words and overlap_sentences:
                    break 
                overlap_sentences.insert(0, prev_sent)
                overlap_word_count += len(prev_sent.split()) # number of overlapping words

            current_chunk_sentences = overlap_sentences
            current_word_count = overlap_word_count

    # Handle the remainder (the final piece of the document)
    if current_chunk_sentences:
        chunk_text = " ".join(current_chunk_sentences)
    
        # Smart Remainder Handling:
        # If the final leftover piece is extremely short (e.g., < 50 words), 
        # Calculate ONLY the brand new words, if it is too short, just append to previous chunk
        new_words = len(chunk_text.split()) - overlap_word_count

        if new_words < 60 and len(chunks) > 0:
            last_chunk = chunks[-1]
            # Strip the old title prefix to rebuild it cleanly
            old_content = last_chunk["text"].replace(f"Title: {title}\nContent: ", "").replace("Content: ", "")
            # Add only the new un-overlapped part
            merged_content = old_content + " " + " ".join(current_chunk_sentences[-1:]) 
            
            chunks[-1]["text"] = f"Title: {title}\nContent: {merged_content}" if title else f"Content: {merged_content}"
        else:
            # Save it as a normal final chunk
            final_text = f"Title: {title}\nContent: {chunk_text}" if title else f"Content: {chunk_text}"
            chunks.append({
                "chunk_id": f"{doc_id}_chunk{chunk_idx}",
                "source_id": str(doc_id),
                "text": final_text
            })

    return chunks

def build_chunked_corpus(data_dir="data/scifact"):
    base_path = Path(data_dir)
    input_corpus = base_path / "corpus.jsonl"
    output_corpus = base_path / "corpus_chunked.jsonl"
    
    if not input_corpus.exists():
        print(f"❌ Error: {input_corpus} not found.")
        return

    print(f"Reading unified corpus from {input_corpus}...")
    
    total_original_docs = 0
    total_chunks = 0
    total_chunk_words = 0
    
    with open(input_corpus, 'r', encoding='utf-8') as infile, \
         open(output_corpus, 'w', encoding='utf-8') as outfile:
         
        for line in tqdm(infile, desc="Chunking documents"):
            line = line.strip()
            if not line: continue
            
            doc = json.loads(line)
            total_original_docs += 1
            
            doc_id = str(doc.get("doc_id", ""))
            title = doc.get("title", "")
            sentences = doc.get("abstract", [])
            
            # Generate the context-aware chunks
            doc_chunks = chunk_document(doc_id, title, sentences)
            
            # Save the chunks to the new JSONL file
            for chunk in doc_chunks:
                outfile.write(json.dumps(chunk) + "\n")
                total_chunks += 1

                # Count the words in the final embedded payload
                total_chunk_words += len(chunk["text"].split())

    print("\n✅ Chunking Complete!")
    print(f"  - Original Documents: {total_original_docs:,}")
    print(f"  - Total Chunks Created: {total_chunks:,}")
    if total_original_docs > 0:
        print(f"  - Average Chunks per Doc: {total_chunks / total_original_docs:.2f}")

    if total_chunks > 0:
        print(f"  - Average Words per Chunk: {total_chunk_words / total_chunks:.0f}")

    print(f"  - Output saved to: {output_corpus}")

if __name__ == "__main__":
    build_chunked_corpus(data_dir="data/quantemp")