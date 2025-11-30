import os
import json
import hashlib
from pathlib import Path
from typing import Set, List, Dict, Any

from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain_chroma import Chroma
from langchain_core.documents import Document

# 1. Identify where this script is located (src/utils)
CURRENT_SCRIPT_DIR = Path(__file__).resolve().parent

# 2. Calculate Project Root
PROJECT_ROOT = CURRENT_SCRIPT_DIR.parent.parent

# 3. Define Absolute Paths for Data
DEFAULT_DB_PATH = PROJECT_ROOT / "chroma_db_semantic"
DEFAULT_DATA_PATH = PROJECT_ROOT / "data"

class VectorDBIngestor:
    """
    Ingests documents into a Chroma Vector Database.
    - PDFs: Processed with PyPDFLoader and SemanticChunker.
    - JSONL (FactCheck-GPT): Processed with custom extraction and hash-based deduplication.
    """
    def __init__(self, db_path=None, embedding_model_name="sentence-transformers/all-MiniLM-L6-v2"):
        """
        Args:
            db_path: (Optional) Path to the vector DB. Defaults to PROJECT_ROOT/chroma_db_semantic
        """
        # Use the calculated default if no path is provided
        self.db_path = str(db_path) if db_path else str(DEFAULT_DB_PATH)
        
        print(f"Target Database: {self.db_path}")
        print(f"Initializing Embedding Model ({embedding_model_name})...")
        self.embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)
        
        print("Initializing Semantic Splitter (for PDFs)...")
        self.text_splitter = SemanticChunker(
            self.embedding_model,
            breakpoint_threshold_type="percentile",
            breakpoint_threshold_amount=90
        )

    def _get_processed_files(self) -> Set[str]:
        """Retrieves a set of file paths that have already been ingested."""
        if not os.path.exists(self.db_path):
            return set()

        # Initialize ephemeral client just to read metadata
        db = Chroma(persist_directory=self.db_path, embedding_function=self.embedding_model)
        
        try:
            data = db.get(include=['metadatas'])
            metadatas = data.get('metadatas', [])
            processed_files = set()
            for meta in metadatas:
                if meta and 'source' in meta:
                    # Normalize path to handle / vs \ consistently
                    try:
                        clean_path = str(Path(meta['source']).resolve())
                        processed_files.add(clean_path)
                    except Exception:
                        continue # Skip malformed paths
            return processed_files
        except Exception as e:
            print(f"Warning: Could not read existing DB state: {e}")
            return set()

    def _generate_id(self, text: str) -> str:
        """Creates a unique ID for deduplication based on text content."""
        return hashlib.md5(text.strip().encode('utf-8')).hexdigest()

    def _extract_factcheck_evidence(self, file_path: Path) -> List[Dict[str, Any]]:
        """
        Parses FactCheck-GPT dataset (.jsonl) to extract unique evidence snippets.
        Returns a list of dicts with 'id', 'text', and 'metadata'.
        """
        data = []
        
        # Read .jsonl line by line to avoid JSONDecodeError
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    data.append(json.loads(line))

        corpus = {}  # Deduplication buffer: {hash: {id, text, metadata}}

        for entry in data:
            if "sentences" not in entry:
                continue

            for sent_key, sent_data in entry["sentences"].items():
                
                # --- 1. Process Automated Evidence ---
                if "auto_evidence" in sent_data and "auto_evidence_url" in sent_data:
                    auto_evs = sent_data["auto_evidence"]
                    auto_urls = sent_data["auto_evidence_url"]

                    # Ensure lists are aligned
                    if len(auto_evs) == len(auto_urls):
                        for i in range(len(auto_evs)): # Loop through claims
                            ev_list = auto_evs[i]
                            url_list = auto_urls[i]
                            
                            for text, url in zip(ev_list, url_list):
                                if not text: continue # Skip empty
                                
                                doc_id = self._generate_id(text)
                                if doc_id not in corpus:
                                    corpus[doc_id] = {
                                        "id": doc_id,
                                        "text": text,
                                        "metadata": {
                                            "source": str(file_path.resolve()), # Standardize 'source' field
                                            "source_type": "auto_retrieval",
                                            "url": url,
                                            "origin_sentence": sent_key
                                        }
                                    }

                # --- 2. Process Human Evidence ---
                if "human_evidence" in sent_data:
                    for text_blob in sent_data["human_evidence"]:
                        if not text_blob: continue

                        # Basic cleaning: Split URL from text if formatted like "URL\n\nText"
                        parts = text_blob.split('\n', 1)
                        if len(parts) > 1 and parts[0].strip().startswith('http'):
                            url = parts[0].strip()
                            content = parts[1].strip()
                        else:
                            url = "N/A"
                            content = text_blob.strip()

                        if content:
                            doc_id = self._generate_id(content)
                            if doc_id not in corpus:
                                corpus[doc_id] = {
                                    "id": doc_id,
                                    "text": content,
                                    "metadata": {
                                        "source": str(file_path.resolve()), # Standardize 'source' field
                                        "source_type": "human_gold",
                                        "url": url,
                                        "origin_sentence": sent_key
                                    }
                                }

        return list(corpus.values())

    def ingest_file(self, file_path):
        """
        Ingests a single file. Logic branches based on file extension.
        """
        path_obj = Path(file_path)
        
        if not path_obj.exists():
            print(f"Error: File not found at {path_obj}")
            return

        print(f"\n--- Processing: {path_obj.name} ---")
        
        try:
            # Initialize DB connection
            db = Chroma(persist_directory=self.db_path, embedding_function=self.embedding_model)

            # --- STRATEGY: Handle .jsonl (FactCheck-GPT Evidence) ---
            if path_obj.suffix.lower() == '.jsonl':
                print("Detected JSONL format. Extracting atomic evidence snippets...")
                raw_items = self._extract_factcheck_evidence(path_obj)
                
                if not raw_items:
                    print("Warning: No valid evidence found in JSONL file.")
                    return

                # Convert to LangChain Documents
                # We do NOT use the semantic splitter here because these are already atomic snippets.
                docs = []
                ids = []
                for item in raw_items:
                    docs.append(Document(
                        page_content=item['text'],
                        metadata=item['metadata']
                    ))
                    ids.append(item['id'])
                
                # Add to DB with explicit IDs for deduplication
                db.add_documents(docs, ids=ids)
                print(f"Success! Added {len(docs)} unique evidence snippets.")

            # --- STRATEGY: Handle .pdf (Raw Documents) ---
            elif path_obj.suffix.lower() == '.pdf':
                print("Detected PDF format. Loading and chunking...")
                loader = PyPDFLoader(str(path_obj))
                raw_docs = loader.load()
                
                # PDFs are long, so we MUST split them semantically
                chunks = self.text_splitter.split_documents(raw_docs)
                
                # Add source metadata consistency
                for chunk in chunks:
                    chunk.metadata['source'] = str(path_obj.resolve())

                if chunks:
                    db.add_documents(chunks)
                    print(f"Success! Added {len(chunks)} semantic chunks from PDF.")
                else:
                    print("Warning: No text content extracted from PDF.")
            
            else:
                print(f"Unsupported file type: {path_obj.suffix}")

        except Exception as e:
            print(f"Failed to process {path_obj.name}: {e}")

    def ingest_folder(self, folder_path=None, extensions=[".pdf", ".jsonl"]):
        """
        Scans a folder for new files with specific extensions and ingests them.
        Args:
            folder_path: (Optional) Folder to scan. Defaults to PROJECT_ROOT/docs
            extensions: List of file extensions to process.
        """
        # Use default docs path if none provided
        target_folder = Path(folder_path) if folder_path else DEFAULT_DATA_PATH

        if not target_folder.exists():
            print(f"Folder not found: {target_folder}")
            return

        print(f"Scanning '{target_folder}' for new files ({', '.join(extensions)})...")
        
        # 1. Get processed files (normalized to absolute paths)
        already_in_db = self._get_processed_files()
        
        # 2. Gather all candidate files
        files_to_process = []
        for ext in extensions:
            # Case insensitive search would require more complex globbing, assume lowercase for now
            found_files = list(target_folder.glob(f"*{ext}"))
            
            for file_path in found_files:
                # Convert to absolute string for comparison
                abs_path_str = str(file_path.resolve())
                
                if abs_path_str not in already_in_db:
                    files_to_process.append(file_path)
                else:
                    print(f"Skipping: {file_path.name} (Already in DB)")

        if not files_to_process:
            print("\nEverything is up to date! No new files found.")
            return

        print(f"\nFound {len(files_to_process)} new files. Starting ingestion...")
        
        for file_path in files_to_process:
            self.ingest_file(file_path)

# --- Usage Example ---
if __name__ == "__main__":    
    ingestor = VectorDBIngestor()
    
    # Process the default docs folder for both PDFs and JSONL files
    ingestor.ingest_folder()