import os
import torch
import gc
from minicheck.minicheck import MiniCheck

if __name__ == "__main__":
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    print("Initializing...")

    claims = ["The students are preparing for an examination.", "The students are on vacation."]
    doc = "A group of students gather in the school library to study for their upcoming final exams."
    model_name = 'Bespoke-MiniCheck-7B'

    print(f"Loading {model_name} with safe settings...")
    
    # Initialize with limited context to save memory
    scorer = MiniCheck(
        model_name=model_name, 
        enable_prefix_caching=False, 
        cache_dir='./ckpts',
        max_model_len=4096,  # Limit context window
    )

    print("Model loaded. Scoring...")
    pred_label, raw_prob, _, _ = scorer.score(docs=[doc, doc], claims=claims)

    f = lambda x: round(x*100, 2)
    prob_percentages = [f(x) for x in raw_prob]

    print(f'\nEvaluating using model: {model_name}')
    for idx, claim in enumerate(claims):
        print(f'Prediction for claim: \n"{claim}": {bool(pred_label[idx])}')
        print(f'Truthful probability: {prob_percentages[idx]}%')

    # Cleanup
    del scorer
    gc.collect()
    torch.cuda.empty_cache()
    print("Done.")