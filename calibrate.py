import json
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def optimize_threshold(file_path):
    print(f"Loading calibration data from: {file_path}")
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    if not data:
        print("Error: No data found in file.")
        return

    # 1. Extract Data
    # scores = Array of unbounded floats (e.g., 0.1, 4.5, 12.9)
    scores = np.array([d['uncertainty_score'] for d in data])
    y_true = np.array([d['gold_label'] for d in data])
    y_para = np.array([d.get('parametric_verdict', 'NOT ENOUGH INFO') for d in data])
    y_rag = np.array([d.get('rag_prediction', 'NOT ENOUGH INFO') for d in data])

    print(f"\n--- Score Distribution Statistics ---")
    print(f"Min Score: {scores.min():.4f}")
    print(f"Max Score: {scores.max():.4f}")
    print(f"Mean Score: {scores.mean():.4f}")
    print("-" * 30)

    best_acc = 0
    best_thresh = scores.min() # Start at the bottom
    
    # 2. Dynamic Threshold Search
    # Instead of 0.0 to 1.0, we search from min_score to max_score
    # We add a small buffer to ensure we cover the edges
    search_space = np.linspace(scores.min(), scores.max(), num=1000)
    
    results = []

    for t in search_space:
        # LOGIC:
        # High Score = High Uncertainty = Need Retrieval
        # If score < t: CONFIDENT -> Use Parametric
        # If score >= t: UNCERTAIN -> Use RAG
        
        y_hybrid = np.where(scores < t, y_para, y_rag) # If score < t, take parametric verdict; else take RAG
        
        acc = accuracy_score(y_true, y_hybrid)
        
        # Calculate Retrieval Rate (How often do we call RAG?)
        # This is crucial for "efficiency" arguments in your thesis
        retrieval_rate = np.mean(scores >= t)
        
        results.append((t, acc, retrieval_rate))
        
        if acc > best_acc:
            best_acc = acc
            best_thresh = t

    # 3. Print Results
    print(f"\n--- Optimization Results ---")
    print(f"Optimal Threshold: {best_thresh:.4f}")
    print(f"Peak Accuracy:     {best_acc:.4f} ({(best_acc*100):.2f}%)")
    
    # Get stats for the optimal point
    opt_retrieval_rate = np.mean(scores >= best_thresh)
    print(f"Retrieval Rate:    {opt_retrieval_rate:.2%} (Percentage of calls sent to RAG)")

    print(f"\n--- Baselines ---")
    acc_para = accuracy_score(y_true, y_para)
    acc_rag = accuracy_score(y_true, y_rag)
    print(f"Parametric Only (Never Retrieve): {acc_para:.4f}")
    print(f"RAG Only (Always Retrieve):       {acc_rag:.4f}")
    
    return best_thresh

if __name__ == "__main__":
    # Update this path to your actual results file
    # path = "results/RQ1/scifact/uq_aware/results_train.jsonl" 
    path = "results/RQ1/quantemp/uq_aware/results_val.jsonl"
    optimize_threshold(path)