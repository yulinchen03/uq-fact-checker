import pickle
import os
from pathlib import Path
from typing import List, Tuple, Dict, Optional

import numpy as np
import torch
from sentence_transformers import SentenceTransformer, util

try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    LANGCHAIN_AVAILABLE = True
except ImportError:
    LANGCHAIN_AVAILABLE = False
    print("Warning: LangChain text splitters not available. Falling back to custom chunking.")


class RAGRetriever:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", chunk_size: int = 200, overlap: int = 50):
        """
        Initialize the RAG Retriever with a sentence transformer model.

        Args:
            model_name: HuggingFace model name for embeddings
            chunk_size: Maximum characters per chunk
            overlap: Number of overlapping characters between chunks
        """
        self.model_name = model_name
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.model = SentenceTransformer(model_name)
        self.chunks = []
        self.chunk_metadata = []
        self.embeddings = None

        # Initialize text splitter (LangChain if available, otherwise fallback)
        if LANGCHAIN_AVAILABLE:
            self.text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size,
                chunk_overlap=self.overlap,
                length_function=len,
                separators=["\n\n", "\n", " ", ""]
            )
        else:
            self.text_splitter = None

    def _get_document_files_info(self, documents_dir: str) -> Dict[str, float]:
        """
        Get information about all document files in the directory.

        Args:
            documents_dir: Path to documents directory

        Returns:
            Dictionary with file paths as keys and modification times as values
        """
        documents_path = Path(documents_dir)
        files_info = {}

        if not documents_path.exists():
            return files_info

        for file_path in documents_path.glob("*.txt"):
            if file_path.is_file():
                files_info[str(file_path)] = file_path.stat().st_mtime

        return files_info

    def _get_cache_info(self, cache_file: str) -> Optional[float]:
        """
        Get the modification time of the cache file.

        Args:
            cache_file: Path to cache file

        Returns:
            Cache modification time or None if file doesn't exist
        """
        cache_path = Path(cache_file)
        if cache_path.exists():
            return cache_path.stat().st_mtime
        return None

    def should_refresh_cache(self, documents_dir: str, cache_file: str) -> bool:
        """
        Check if the cache should be refreshed based on document modifications.

        Args:
            documents_dir: Path to documents directory
            cache_file: Path to cache file

        Returns:
            True if cache should be refreshed, False otherwise
        """
        # If cache doesn't exist, need to create it
        if not Path(cache_file).exists():
            return True

        # Load cache to get stored file info
        try:
            with open(cache_file, 'rb') as f:
                cache_data = pickle.load(f)

            # Check if cache contains file modification times
            stored_files_info = cache_data.get('files_info', {})
            if not stored_files_info:
                # Old cache format, refresh to add file tracking
                return True

            # Get current files info
            current_files_info = self._get_document_files_info(documents_dir)

            # Check if files were added or deleted
            if set(current_files_info.keys()) != set(stored_files_info.keys()):
                return True

            # Check if any files were modified
            for file_path, current_mtime in current_files_info.items():
                stored_mtime = stored_files_info.get(file_path, 0)
                if current_mtime > stored_mtime:
                    return True

            return False

        except Exception as e:
            # If we can't read cache, refresh it
            print(f"Cache validation error: {e}")
            return True

    def save_embeddings_with_file_info(self, cache_file: str, documents_dir: str):
        """
        Save embeddings with file modification information.

        Args:
            cache_file: Path to save embeddings
            documents_dir: Path to documents directory
        """
        if self.embeddings is None:
            raise ValueError("No embeddings to save. Call create_embeddings() first.")

        files_info = self._get_document_files_info(documents_dir)

        cache_data = {
            'chunks': self.chunks,
            'chunk_metadata': self.chunk_metadata,
            'embeddings': self.embeddings.cpu().numpy(),
            'model_name': self.model_name,
            'files_info': files_info  # Add file modification times
        }

        with open(cache_file, 'wb') as f:
            pickle.dump(cache_data, f)
        print(f"Embeddings with file info saved to {cache_file}")

    def smart_load_embeddings(self, documents_dir: str, cache_file: str) -> bool:
        """
        Smart loading that automatically refreshes cache if needed.

        Args:
            documents_dir: Path to documents directory
            cache_file: Path to cache file

        Returns:
            True if loaded successfully, False otherwise
        """
        if self.should_refresh_cache(documents_dir, cache_file):
            if Path(cache_file).exists():
                print("  🔄 Documents changed, refreshing cache...")
            else:
                print("  📄 No cache found, creating new cache...")

            self.load_documents(documents_dir)
            self.create_embeddings()
            self.save_embeddings_with_file_info(cache_file, documents_dir)
            return True
        else:
            print("  📄 Cache is up to date, loading...")
            return self.load_embeddings(cache_file)

    def chunk_text(self, text: str, source_file: str) -> List[str]:
        """
        Split text into semantic chunks using LangChain or custom fallback.

        Args:
            text: Input text to chunk
            source_file: Source file name for metadata

        Returns:
            List of text chunks
        """
        if LANGCHAIN_AVAILABLE and self.text_splitter:
            # Use LangChain
            chunks = self.text_splitter.split_text(text)
        else:
            print("ERROR: LangChain not available.")
            chunks = []

        # Filter out very small chunks
        return [chunk.strip() for chunk in chunks if chunk.strip() and len(chunk.strip()) > 50]

    def load_documents(self, documents_dir: str) -> None:
        """
        Load and chunk all text documents from a directory.

        Args:
            documents_dir: Path to directory containing text files
        """
        documents_path = Path(documents_dir)
        self.chunks = []
        self.chunk_metadata = []

        for file_path in documents_path.glob("*.txt"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()

                if content:
                    file_chunks = self.chunk_text(content, file_path.name)
                    if file_chunks:
                        self.chunks.extend(file_chunks)

                        # Store metadata for each chunk
                        for chunk in file_chunks:
                            self.chunk_metadata.append({
                                'source_file': file_path.name,
                                'chunk_length': len(chunk)
                            })
                    else:
                        print(f"Warning: Chunking failed for document in {file_path}")

            except Exception as e:
                print(f"Error loading {file_path}: {e}")

        print(f"Loaded {len(self.chunks)} chunks from {len(list(documents_path.glob('*.txt')))} files")

    def create_embeddings(self) -> None:
        """Create embeddings for all document chunks."""
        if not self.chunks:
            raise ValueError("No chunks loaded. Call load_documents() first.")

        print("Creating embeddings for document chunks...")
        self.embeddings = self.model.encode(
            self.chunks,
            convert_to_tensor=True,
            show_progress_bar=True
        )
        print(f"Created embeddings with shape: {self.embeddings.shape}")

    def save_embeddings(self, cache_file: str) -> None:
        """
        Save embeddings to cache file.

        Args:
            cache_file: Path to save embeddings
        """
        if self.embeddings is None:
            raise ValueError("No embeddings to save. Call create_embeddings() first.")

        cache_data = {
            'chunks': self.chunks,
            'chunk_metadata': self.chunk_metadata,
            'embeddings': self.embeddings.cpu().numpy(),
            'model_name': self.model_name
        }

        with open(cache_file, 'wb') as f:
            pickle.dump(cache_data, f)
        print(f"Embeddings saved to {cache_file}")

    def load_embeddings(self, cache_file: str) -> bool:
        """
        Load embeddings from cache file.

        Args:
            cache_file: Path to load embeddings from

        Returns:
            True if loaded successfully, False otherwise
        """
        try:
            with open(cache_file, 'rb') as f:
                cache_data = pickle.load(f)

            self.chunks = cache_data['chunks']
            self.chunk_metadata = cache_data['chunk_metadata']
            # Convert numpy embeddings back to tensor on the same device as the model
            device = next(self.model.parameters()).device
            self.embeddings = torch.tensor(cache_data['embeddings'], device=device)
            self.model_name = cache_data['model_name']

            print(f"Loaded {len(self.chunks)} chunks from cache")
            return True
        except Exception as e:
            print(f"Error loading cache: {e}")
            return False

    def retrieve(self, query: str, top_k: int = 3) -> List[Tuple[str, float, Dict]]:
        """
        Retrieve most relevant document chunks for a query.

        Args:
            query: Search query
            top_k: Number of top results to return

        Returns:
            List of tuples containing (chunk_text, relevance_score, metadata)
        """
        if self.embeddings is None:
            raise ValueError("No embeddings available. Call create_embeddings() or load_embeddings() first.")

        # Encode the query
        query_embedding = self.model.encode(query, convert_to_tensor=True)

        # Ensure both tensors are on the same device
        if self.embeddings.device != query_embedding.device:
            query_embedding = query_embedding.to(self.embeddings.device)

        # Compute cosine similarity
        cosine_scores = util.pytorch_cos_sim(query_embedding, self.embeddings)[0]

        # Get top-k results
        top_indices = np.argsort(cosine_scores.cpu().numpy())[-top_k:][::-1]

        results = []
        for idx in top_indices:
            score = cosine_scores[idx].item()
            chunk_text = self.chunks[idx]
            metadata = self.chunk_metadata[idx]
            results.append((chunk_text, score, metadata))

        return results