import chromadb
import torch
from typing import List
from sentence_transformers import SentenceTransformer

from src.data_models import Document
from src.modules.abstract_components import PipelineComponent

class BaseRetriever(PipelineComponent):
    """Abstract base class for retrievers."""
    
    def _retrieve(self, query: str) -> List[Document]:
        """Retrieve documents for a given query."""
        raise NotImplementedError

class VectorDBRetriever(BaseRetriever):
    """Retriever using vector databases (ChromaDB)."""
    
    def __init__(self, collection: str, db_path: str, embedding_model: str, top_k: int = 3, device: str = "cuda", debug: bool = False):
        """
        Initialize connection to vector database and load embedding model.
        
        Args:
            collection: Name of the ChromaDB collection.
            db_path: Path to the vector database.
            embedding_model: Name of the embedding model.
            top_k: Number of documents to retrieve per query.
            device: 'cuda' or 'cpu'.
            debug: Whether to enable debug logging.
        """
        self.collection_name = collection
        self.top_k = top_k
        self.device = device
        self.debug = debug
        
        print(f"Loading Retriever: {embedding_model} on {device}...")
        
        # 1. Load Embedding Model
        # Trust remote code is needed for Qwen/newer models
        self.encoder = SentenceTransformer(
            embedding_model, 
            device=device,
            trust_remote_code=True
        )
        
        # 2. Connect to ChromaDB
        self.client = chromadb.PersistentClient(path=db_path)
        
        try:
            self.collection = self.client.get_collection(self.collection_name)
        except Exception as e:
            print(f"Error loading collection '{self.collection_name}': {e}")
            raise

    def _retrieve(self, query: str) -> List[Document]:
        """Retrieve documents for the given query."""
        
        # 1. Embed Query
        query_embedding = self.encoder.encode(
            [query], 
            convert_to_tensor=False,
            normalize_embeddings=True
        )[0].tolist()

        # 2. Query Database
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=self.top_k
        )

        # 3. Parse Results
        documents = []
        
        # Chroma returns lists of lists (batch format)
        ids = results.get("ids", [[]])[0]
        docs = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        for i in range(len(ids)):
            # Handle potential None metadata
            meta = metadatas[i] if metadatas and i < len(metadatas) else {}
            
            # Construct Document object
            doc = Document(
                source_id=ids[i],
                content=docs[i],
                score=distances[i] if i < len(distances) else 0.0,
                **meta
            )
            documents.append(doc)
            
        return documents
    
    def process(self, sample):
        """
        Process sample by retrieving evidence for all search queries.
        """
        all_results = []
        
        # If no queries exist (e.g. IdentityGenerator wasn't run), use claim
        queries = sample.search_queries if sample.search_queries else [sample.claim]
        
        for query in queries:
            results = self._retrieve(query)
            all_results.extend(results)
        
        # Deduplicate by source_id
        seen = set()
        unique_results = []
        for doc in all_results:
            if doc.source_id not in seen:
                seen.add(doc.source_id)
                unique_results.append(doc)
        
        sample.retrieved_evidence = unique_results

        # --- DEBUG PRINT (scifact) ---
        if self.debug and self.collection_name == "scifact_corpus":            
            retrieved_ids = [str(doc.source_id) for doc in unique_results]
            
            # Now we can just use the list directly!
            gold_ids = [str(gid) for gid in sample.gold_evidence]
            
            hits = set(retrieved_ids).intersection(set(gold_ids))
            
            print(f"\n[DEBUG] Claim {sample.id}:")
            print(f"   - Gold Refs: {gold_ids}")
            print(f"   - Retrieved: {retrieved_ids}")
            print(f"   - Overlap  : {len(hits)} / {len(gold_ids)}")
            # -----------------------------

        return sample


class SkipRetriever(BaseRetriever):
    """No-operation retriever (Never Retrieve mode)."""
    
    def _retrieve(self, query: str) -> List[Document]:
        return []
    
    def process(self, sample):
        """Do nothing and return the sample unchanged."""
        return sample