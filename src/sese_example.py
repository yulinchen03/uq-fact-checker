import logging
import sys
import os

# Optional: suppress some of the verbose logs from transformers/numba
logging.basicConfig(level=logging.ERROR)

print("Loading SeSE models... (this may take a minute first time)")
from SeSE.construct_semantic_graph import build_semantic_graph
from SeSE.structural_entropy import compute_se

def calculate_sese_score(question, responses):
    """
    Computes the Structural Semantic Entropy (SeSE) for a list of responses.
    
    Lower Score = High consistency (confident, specific answers)
    Higher Score = Low consistency (confusion, conflict, or vagueness)
    """
    
    # 1. Build the Semantic Graph
    # This uses DeBERTa (entailment) and Sentence Transformers (similarity)
    # to create a matrix representing how much the answers agree with each other.
    print(f"\nProcessing {len(responses)} responses for question: '{question}'...")
    adjacency_matrix = build_semantic_graph(responses, question)
    
    # 2. Compute Structural Entropy
    # This analyzes the graph topology to measure 'disorder' (uncertainty).
    entropy = compute_se(adjacency_matrix)
    
    return entropy

if __name__ == "__main__":
    # --- Example 1: Consistent / Low Entropy ---
    # The model is sure about the answer.
    q1 = "What is the capital of France?"
    r1 = [
        "The capital is Paris.",
        "Paris is the capital city of France.",
        "It's Paris.",
        "France's capital is Paris."
    ]
    
    score1 = calculate_sese_score(q1, r1)
    print(f"Score 1 (Consistent): {score1:.4f}")

    # --- Example 2: Inconsistent / High Entropy ---
    # The model is hallucinating or confused.
    q2 = "Who won the 2024 US Election?"
    r2 = [
        "Joe Biden won the election.",
        "Donald Trump was the winner.",
        "The election has not happened yet.",
        "It was Kamala Harris."
    ]
    
    score2 = calculate_sese_score(q2, r2)
    print(f"Score 2 (Conflicting): {score2:.4f}")