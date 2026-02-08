import json
import chromadb
import chromadb.errors 
import torch
import os
import gc
from pathlib import Path
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import hydra
from omegaconf import DictConfig

os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

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

    def build_scifact(self):
        corpus_path = Path(self.cfg.data.root_path) / "scifact" / "corpus.jsonl"
        if not corpus_path.exists():
            raise FileNotFoundError(f"Corpus not found at {corpus_path}")

        batch_size = 32 
        batch_docs = []
        batch_ids = []
        batch_metadatas = []

        print(f"Reading corpus from {corpus_path}...")
        total_lines = sum(1 for _ in open(corpus_path, 'r', encoding='utf-8'))

        with open(corpus_path, 'r', encoding='utf-8') as f:
            for line in tqdm(f, total=total_lines, desc="Indexing SciFact"):
                line = line.strip()
                if not line: continue
                
                doc = json.loads(line)
                doc_id = str(doc.get("doc_id"))
                title = doc.get("title", "")
                
                abstract_raw = doc.get("abstract", "")
                if isinstance(abstract_raw, list):
                    abstract = " ".join(abstract_raw)
                else:
                    abstract = str(abstract_raw)

                text_content = f"Title: {title}\nAbstract: {abstract}"

                batch_docs.append(text_content)
                batch_ids.append(doc_id)
                batch_metadatas.append({"title": title, "source": "scifact"})

                if len(batch_docs) >= batch_size:
                    self._upsert_batch(batch_docs, batch_ids, batch_metadatas)
                    batch_docs = []
                    batch_ids = []
                    batch_metadatas = []

            if batch_docs:
                self._upsert_batch(batch_docs, batch_ids, batch_metadatas)
        
        print("✅ SciFact Indexing Complete.")

    def _upsert_batch(self, documents, ids, metadatas):
        try:
            embeddings = self.encoder.encode(
                documents, 
                normalize_embeddings=True,
                batch_size=16,
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
            print(f"Error upserting batch: {e}")
            for i in range(len(documents)):
                self._upsert_single(documents[i], ids[i], metadatas[i])

    def _upsert_single(self, document, doc_id, metadata):
        # Fallback for extreme OOM cases
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

@hydra.main(version_base=None, config_path="../../config", config_name="config")
def main(cfg: DictConfig):
    builder = VectorDBBuilder(cfg)
    if cfg.data.dataset_name == "scifact":
        builder.build_scifact()
    else:
        print(f"No corpus builder for {cfg.data.dataset_name}. Skipping.")

if __name__ == "__main__":
    main()