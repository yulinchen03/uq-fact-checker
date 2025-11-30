"""
Generation module for RAG (Retrieval-Augmented Generation) system.

This module provides text generation functionality using retrieved context
to augment queries and generate complete, insightful responses.
"""

from .generator import RAGGenerator

__all__ = ['RAGGenerator']