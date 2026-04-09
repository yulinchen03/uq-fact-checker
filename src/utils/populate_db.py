import json
import chromadb
import chromadb.errors 
import inquirer
import torch
import os
import gc
import ijson
from pathlib import Path
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import sys
import hydra
from omegaconf import DictConfig

os.environ["PYTORCH_ALLOC_CONF"] = "expandable_segments:True"

def get_experiment_config(cfg: DictConfig):
    # If not interactive (e.g. Slurm batch job), use the config's dataset
    if not sys.stdout.isatty():
        dataset = cfg.data.get("dataset_name", "scifact").lower()
        if dataset not in ['scifact', 'quantemp']:
            dataset = 'scifact'
        return {'dataset': dataset}

    questions = [
        inquirer.List('dataset',
                      message="Select the dataset to create vector DB for",
                      choices=['scifact', 'quantemp']), 
    ]
    return inquirer.prompt(questions)

class VectorDBBuilder:
    def __init__(self, cfg: DictConfig):
        self.cfg = cfg
        model_name = cfg.retriever.embedding_model
        print(f"Loading embedding model: {model_name}...")
        
        self.encoder = SentenceTransformer(
            model_name, 
            device=cfg.llm.device, 
            trust_remote_code=True,
            model_kwargs={"torch_dtype": torch.float16} 
        )
        
        self.encoder.max_seq_length = 4096
        print(f"Model loaded. Max Sequence Length restricted to: {self.encoder.max_seq_length}")
        
        # Initialize ChromaDB
        db_path = Path(cfg.retriever.db_path) 
        db_path.mkdir(parents=True, exist_ok=True)
        print(f"Initializing ChromaDB at: {db_path}")
        
        self.client = chromadb.PersistentClient(path=str(db_path))
        
        collection_name = cfg.retriever.collection_name
        try:
            self.client.delete_collection(collection_name)
            print(f"Deleted existing collection '{collection_name}' to rebuild.")
        except (ValueError, chromadb.errors.NotFoundError):
            pass

        self.collection = self.client.create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )

    def build(self):
        """
        Main entry point. Dispatches to the correct builder based on config.
        """
        dataset = self.cfg.data.dataset_name.lower()
        print(f"Starting build for dataset: {dataset}")

        if dataset == "scifact":
            self._build_scifact()
        elif dataset == "quantemp":
            self._build_quantemp()
        else:
            raise ValueError(f"No corpus builder implemented for: {dataset}")

    def _build_scifact(self):
        # Path: data/scifact/corpus.jsonl
        corpus_path = Path(self.cfg.data.root_path) / "scifact" / "corpus.jsonl"
        self._process_jsonl(corpus_path, "SciFact")

    def _build_quantemp(self):
        # Path: data/quantemp/corpus.json
        corpus_path = Path(self.cfg.data.root_path) / "quantemp" / "corpus.json"
        self._process_key_value_json(corpus_path, "Quantemp")

    def _process_jsonl(self, file_path: Path, dataset_name: str):
        """
        Generic processor for JSONL corpus files.
        Assumes fields: doc_id/id, title, abstract/text
        """
        if not file_path.exists():
            raise FileNotFoundError(f"Corpus file not found: {file_path}")

        print(f"Reading corpus from {file_path}...")
        
        # Count lines for progress bar
        total_lines = sum(1 for _ in open(file_path, 'r', encoding='utf-8'))
        
        batch_size = 32
        batch_docs = []
        batch_ids = []
        batch_metadatas = []

        with open(file_path, 'r', encoding='utf-8') as f:
            for line in tqdm(f, total=total_lines, desc=f"Indexing {dataset_name}"):
                line = line.strip()
                if not line: continue
                
                try:
                    doc = json.loads(line)
                    
                    # --- NORMALIZE FIELDS ---
                    # Handle differences between SciFact (doc_id) and Quantemp (id/_id)
                    doc_id = str(doc.get("doc_id") or doc.get("_id") or doc.get("id"))
                    
                    title = doc.get("title", "")
                    # SciFact uses 'abstract', others might use 'text' or 'content'
                    text_raw = doc.get("abstract") or doc.get("text") or doc.get("content") or ""
                    
                    if isinstance(text_raw, list):
                        text_body = " ".join(text_raw)
                    else:
                        text_body = str(text_raw)

                    # Create content for embedding
                    full_text = f"Title: {title}\nContent: {text_body}".strip()

                    batch_docs.append(full_text)
                    batch_ids.append(doc_id)
                    batch_metadatas.append({"title": title, "source": dataset_name})

                    # --- BATCH UPSERT ---
                    if len(batch_docs) >= batch_size:
                        self._upsert_batch(batch_docs, batch_ids, batch_metadatas)
                        batch_docs = []
                        batch_ids = []
                        batch_metadatas = []
                
                except json.JSONDecodeError:
                    continue

            # Upsert remaining
            if batch_docs:
                self._upsert_batch(batch_docs, batch_ids, batch_metadatas)
        
        print(f"✅ {dataset_name} Indexing Complete.")

    
    def _process_key_value_json(self, file_path: Path, dataset_name: str):
        """
        Handles format: {"id1": "text1", "id2": "text2", ...}
        """
        if not file_path.exists():
            raise FileNotFoundError(f"Corpus file not found: {file_path}")

        print(f"Streaming JSON from {file_path} (High Performance Mode)...")
        
        # PERFORMANCE SETTINGS
        # --------------------
        DB_BATCH_SIZE = 512      # Accumulate x docs before writing to DB
        ENCODE_BATCH_SIZE = 8   # Encode x docs at once on GPU
        # --------------------
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)  # Load the BIG dictionary

        print(f"Indexing {len(data)} documents...")

        batch_docs = []
        batch_ids = []
        batch_metadatas = []

        # Open in binary mode for ijson
        with open(file_path, 'rb') as f:
            # ijson.kvitems yields (key, value) pairs from the root object without loading the whole file
            # This allows processing massive files with constant RAM usage.
            cursor = ijson.kvitems(f, "")
            
            for doc_id, text_content in tqdm(cursor, total=len(data), desc=f"Indexing {dataset_name}"):
                
                clean_id = str(doc_id)
                clean_text = str(text_content).strip()
                full_text = f"Content: {clean_text}"

                batch_docs.append(full_text)
                batch_ids.append(clean_id)
                batch_metadatas.append({"source": dataset_name, "original_id": clean_id})

                if len(batch_docs) >= DB_BATCH_SIZE:
                    self._upsert_batch(batch_docs, batch_ids, batch_metadatas, batch_size=ENCODE_BATCH_SIZE)
                    batch_docs = []
                    batch_ids = []
                    batch_metadatas = []

            if batch_docs:
                self._upsert_batch(batch_docs, batch_ids, batch_metadatas, batch_size=ENCODE_BATCH_SIZE)
        
        print(f"✅ {dataset_name} Indexing Complete.")


    def _upsert_batch(self, documents, ids, metadatas, batch_size=128):
        try:
            embeddings = self.encoder.encode(
                documents, 
                normalize_embeddings=True,
                batch_size=batch_size, 
                show_progress_bar=False,
                convert_to_numpy=True
            )

            self.collection.upsert(
                ids=ids,
                embeddings=embeddings.tolist(),
                documents=documents,
                metadatas=metadatas
            )
            
            del embeddings
            torch.cuda.empty_cache()
            gc.collect()

        except Exception as e:
            print(f"⚠️ Batch Error: {e}. Retrying individually...")
            # Fallback (slow but safe)
            for i in range(len(documents)):
                self._upsert_single(documents[i], ids[i], metadatas[i])

    def _upsert_single(self, document, doc_id, metadata):
        try:
            embedding = self.encoder.encode(
                document, 
                normalize_embeddings=True, 
                convert_to_numpy=True
            )
            self.collection.upsert(
                ids=[doc_id],
                embeddings=[embedding.tolist()],
                documents=[document],
                metadatas=[metadata]
            )
        except Exception as e:
            print(f"❌ Failed to upsert doc {doc_id}: {e}")

@hydra.main(version_base=None, config_path="../../config", config_name="config")
def main(cfg: DictConfig):
    config = get_experiment_config(cfg)
    
    if not config:
        print("Setup aborted...")
        return
    
    cfg.data.dataset_name = config['dataset']
    cfg.retriever.db_path = f"./data/vector_db/{cfg.data.dataset_name}"
    cfg.retriever.collection_name = f"{cfg.data.dataset_name}_docs"

    builder = VectorDBBuilder(cfg)
    builder.build()

if __name__ == "__main__":
    main()