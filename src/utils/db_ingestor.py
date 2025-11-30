import os
import glob
from pathlib import Path
from typing import Set
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain_chroma import Chroma

# 1. Identify where this script is located (src/utils)
CURRENT_SCRIPT_DIR = Path(__file__).resolve().parent

# 2. Calculate Project Root
PROJECT_ROOT = CURRENT_SCRIPT_DIR.parent.parent

# 3. Define Absolute Paths for Data
DEFAULT_DB_PATH = PROJECT_ROOT / "chroma_db_semantic"
DEFAULT_DOCS_PATH = PROJECT_ROOT / "docs"

class VectorDBIngestor:
    """
    Ingests newly added documents into a Chroma Vector Database with semantic chunking.
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
        
        print("Initializing Semantic Splitter...")
        self.text_splitter = SemanticChunker(
            self.embedding_model,
            breakpoint_threshold_type="percentile",
            breakpoint_threshold_amount=90
        )

    def _get_processed_files(self) -> Set[str]:
        if not os.path.exists(self.db_path):
            return set()

        db = Chroma(persist_directory=self.db_path, embedding_function=self.embedding_model)
        
        try:
            data = db.get(include=['metadatas'])
            metadatas = data.get('metadatas', [])
            processed_files = set()
            for meta in metadatas:
                if meta and 'source' in meta:
                    # Normalize path to handle / vs \ consistently
                    clean_path = str(Path(meta['source']).resolve())
                    processed_files.add(clean_path)
            return processed_files
        except Exception as e:
            print(f"Warning: Could not read existing DB state: {e}")
            return set()

    def ingest_file(self, file_path):
        # Ensure we are working with a Path object
        path_obj = Path(file_path)
        
        if not path_obj.exists():
            print(f"Error: File not found at {path_obj}")
            return

        print(f"\n--- Processing: {path_obj.name} ---")
        try:
            loader = PyPDFLoader(str(path_obj))
            raw_docs = loader.load()
            
            chunks = self.text_splitter.split_documents(raw_docs)
            
            db = Chroma(persist_directory=self.db_path, embedding_function=self.embedding_model)
            db.add_documents(chunks)
            print(f"Success! Added {len(chunks)} chunks.")
            
        except Exception as e:
            print(f"Failed to process {path_obj.name}: {e}")

    def ingest_folder(self, folder_path=None, extension=".pdf"):
        """
        Args:
            folder_path: (Optional) Folder to scan. Defaults to PROJECT_ROOT/docs
        """
        # Use default docs path if none provided
        target_folder = Path(folder_path) if folder_path else DEFAULT_DOCS_PATH

        if not target_folder.exists():
            print(f"Folder not found: {target_folder}")
            return

        print(f"Scanning '{target_folder}' for new {extension} files...")
        
        # 1. Get all files using pathlib (cleaner than glob)
        all_files_on_disk = list(target_folder.glob(f"*{extension}"))
        
        # 2. Get processed files (normalized to absolute paths)
        already_in_db = self._get_processed_files()
        
        # 3. Calculate delta
        files_to_process = []
        for file_path in all_files_on_disk:
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
    
    ingestor.ingest_folder()