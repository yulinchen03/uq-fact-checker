import torch
from transformers import AutoModelForMaskedLM, AutoTokenizer

class SpladeEncoder:
    def __init__(self, model_name="naver/splade-cocondenser-ensembledistil", device="cuda"):
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForMaskedLM.from_pretrained(model_name).to(device)
        self.model.eval()

    def encode(self, texts: list, max_length=512):
        inputs = self.tokenizer(texts, return_tensors='pt', padding=True, truncation=True, max_length=max_length).to(self.device)
        with torch.no_grad():
            logits = self.model(**inputs).logits
        
        relu_log = torch.log(1 + torch.relu(logits))
        attention_mask = inputs['attention_mask'].unsqueeze(-1)
        masked_relu_log = relu_log * attention_mask
        max_val, _ = torch.max(masked_relu_log, dim=1)
        
        batch_weights = []
        for i in range(max_val.size(0)):
            nonzero_idx = max_val[i].nonzero().squeeze(-1)
            weights = {str(idx.item()): float(max_val[i][idx].item()) for idx in nonzero_idx}
            batch_weights.append(weights)
        return batch_weights