"""
Generation module for RAG (Retrieval-Augmented Generation) system.

This module provides text generation functionality using retrieved context
to augment queries and generate complete, insightful responses.
"""

from typing import List, Tuple, Dict, Optional
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


class RAGGenerator:
    def __init__(self, model_name: str = "Qwen/Qwen2.5-0.5B-Instruct", device: str = "auto"):
        """
        Initialize the RAG Generator with a language model.

        Args:
            model_name: HuggingFace model name for generation
            device: Device to run the model on ('auto', 'cuda', 'cpu')
        """
        self.model_name = model_name
        self.device = device

        print(f"Loading generation model: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            device_map=device if device != "auto" else None
        )

        # Create generation pipeline
        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            device_map=device if device != "auto" else None
        )

        print(f"Generation model loaded successfully")

    def format_context(self, retrieved_docs: List[Tuple[str, float, Dict]]) -> str:
        """
        Format retrieved documents into context for generation.

        Args:
            retrieved_docs: List of (chunk_text, relevance_score, metadata) tuples

        Returns:
            Formatted context string
        """
        if not retrieved_docs:
            return "No relevant information found."

        context_parts = []
        for chunk_text, score, metadata in retrieved_docs:
            # Clean up the text and remove any numbering that might interfere
            clean_text = chunk_text.strip()
            context_parts.append(clean_text)

        return "\n\n".join(context_parts)

    def create_augmented_prompt(self, query: str, context: str, max_sentences: int = 2, max_words: int = 40) -> str:
        """
        Create an augmented prompt combining query with retrieved context.

        Args:
            query: Original user query
            context: Retrieved context documents
            max_sentences: Maximum number of sentences in response
            max_words: Maximum number of words in response

        Returns:
            Augmented prompt for generation
        """
        if not context or context == "No relevant information found.":
            # Fallback when no context is available
            return f"""Question: {query}

IMPORTANT: Limit your response to exactly {max_sentences} sentences maximum. Do NOT exceed this limit. Be concise and direct. Maximum {max_words} words total.

Answer:"""

        # When context is available, present it naturally
        prompt = f"""Relevant information:
<context>        
{context}
</context>

Question: {query}

IMPORTANT: Relevant context has been provided within the <context> tags. Prioritize information in there that can help answer the question. Limit your response to exactly {max_sentences} sentences maximum. Do NOT exceed this limit. Be concise and direct. Maximum {max_words} words total.

Answer:"""

        return prompt

    def generate_response(
        self,
        query: str,
        retrieved_docs: List[Tuple[str, float, Dict]],
        max_new_tokens: int = 80,  # Target ~50 words with buffer
        temperature: float = 0.5,   # Lower for more focused, factual responses
        top_p: float = 0.8,        # More deterministic
        do_sample: bool = True,
        max_sentences: int = 2,    # Maximum sentences in response
        max_words: int = 40        # Maximum words in response
    ) -> Dict:
        """
        Generate a response using RAG (Retrieval-Augmented Generation).

        Args:
            query: User query
            retrieved_docs: Retrieved document chunks
            max_new_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            top_p: Nucleus sampling parameter
            do_sample: Whether to use sampling

        Returns:
            Dictionary containing response, context, and metadata
        """
        # Format the retrieved context
        context = self.format_context(retrieved_docs)

        # Create augmented prompt
        augmented_prompt = self.create_augmented_prompt(query, context, max_sentences, max_words)

        # Generate response
        responses = self.generator(
            augmented_prompt,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            do_sample=do_sample,
            pad_token_id=self.tokenizer.eos_token_id,
            return_full_text=False
        )

        generated_text = responses[0]['generated_text'].strip()

        return {
            'query': query,
            'response': generated_text,
            'context': context,
            'retrieved_docs': retrieved_docs,
            'model_used': self.model_name,
            'generation_params': {
                'max_new_tokens': max_new_tokens,
                'temperature': temperature,
                'top_p': top_p,
                'do_sample': do_sample
            }
        }

    def query_with_rag(
        self,
        query: str,
        retriever,
        top_k: int = 3,
        generation_params: Optional[Dict] = None,
        max_sentences: int = 2,
        max_words: int = 40
    ) -> Dict:
        """
        Complete RAG pipeline: retrieve relevant documents and generate response.

        Args:
            query: User query
            retriever: RAGRetriever instance
            top_k: Number of documents to retrieve
            generation_params: Optional generation parameters

        Returns:
            Complete RAG result with response and retrieval information
        """
        # Retrieve relevant documents
        retrieved_docs = retriever.retrieve(query, top_k=top_k)

        # Set default generation parameters if not provided
        if generation_params is None:
            generation_params = {
                'max_new_tokens': 80,  # Target ~50 words with buffer
                'temperature': 0.5,     # More focused, factual responses
                'top_p': 0.8,           # More deterministic output
                'do_sample': True
            }

        # Generate response
        result = self.generate_response(query, retrieved_docs, max_sentences=max_sentences, max_words=max_words, **generation_params)

        # Add retrieval metadata
        result['retrieval_metadata'] = {
            'num_retrieved_docs': len(retrieved_docs),
            'top_k': top_k,
            'avg_relevance_score': sum(score for _, score, _ in retrieved_docs) / len(retrieved_docs) if retrieved_docs else 0
        }

        return result

    def format_rag_result(self, result: Dict) -> str:
        """
        Format RAG result for display.

        Args:
            result: RAG result dictionary

        Returns:
            Formatted string for display
        """
        output = []
        output.append("\n" + "="*80)
        output.append("🤖 Generated Response:")
        output.append(result['response'])
        output.append("\n" + "-"*80)
        output.append("📊 Generation Info:")
        output.append(f"- Model: {result['model_used']}")
        output.append(f"- Context docs used: {result['retrieval_metadata']['num_retrieved_docs']}")
        output.append(f"- Avg relevance score: {result['retrieval_metadata']['avg_relevance_score']:.4f}")
        output.append("="*80)

        return "\n".join(output)