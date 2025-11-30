"""
Retrieval module for RAG (Retrieval-Augmented Generation) system.

This module provides document chunking, embedding creation, and semantic search
functionality for retrieving relevant document chunks.
"""

from .retriever import RAGRetriever

__all__ = ['RAGRetriever']