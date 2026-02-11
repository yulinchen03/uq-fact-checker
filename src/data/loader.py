import json
from pathlib import Path
from typing import List
from src.data_models import FactCheckSample, FactCheckMetrics

class LocalDataLoader:
    def __init__(self, data_root: str = "./data"):
        self.data_root = Path(data_root)

    def load(self, dataset_name: str, split: str) -> List[FactCheckSample]:
        """
        Factory method to route to specific dataset loaders.
        """
        if dataset_name.lower() == "scifact":
            return self._load_scifact(split)
        elif dataset_name.lower() == "quantemp":
            return self._load_quantemp(split)
        else:
            raise ValueError(f"Unknown dataset: {dataset_name}")

    def _load_scifact(self, split: str) -> List[FactCheckSample]:
        # Path: data/scifact/claims_{split}.jsonl
        file_name = f"claims_{split}.jsonl"
        file_path = self.data_root / "scifact" / file_name
        
        if not file_path.exists():
            raise FileNotFoundError(f"SciFact file not found: {file_path}")

        samples = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line: continue
                
                data = json.loads(line)
                # Structure: {"id": 0, "claim": "...", "evidence": {}, ...}

                raw_evidence = data.get("evidence", {})
                gold_ids = []

                if isinstance(raw_evidence, dict):
                    gold_ids = list(raw_evidence.keys()) 
                # List format (fallback): ["doc_id", "doc_id"]
                elif isinstance(raw_evidence, list):
                    # Handle case where list contains dicts or strings
                    if raw_evidence and isinstance(raw_evidence[0], dict):
                         # If it's a list of objects (rare variant)
                         pass 
                    else:
                        gold_ids = [str(x) for x in raw_evidence]

                sample = FactCheckSample(
                    id=str(data.get("id")),
                    claim=data.get("claim"),
                    gold_label=self._extract_scifact_label(data),
                    gold_evidence=gold_ids,
                    mode="always_retrieve", 
                    metrics=FactCheckMetrics(latency_seconds=0.0, input_tokens=0, output_tokens=0)
                )
                samples.append(sample)
        
        print(f"Loaded {len(samples)} samples from {file_path}")
        return samples

    def _load_quantemp(self, split: str) -> List[FactCheckSample]:     
        # Path: data/quantemp/claims_train.json
        base_path = self.data_root / "quantemp"
        file_name = f"claims_{split}.json"
        
        file_path = base_path / file_name

        if not file_path.exists():
            raise FileNotFoundError(f"Quantemp file not found at: {file_path}")

        print(f"Loading Quantemp from {file_path}...")

        with open(file_path, 'r', encoding='utf-8') as f:
            data_list = json.load(f)

        samples = []
        for idx, data in enumerate(data_list):
            
            # 1. Generate Stable ID (Essential for tracking)
            # Format: qt_val_0, qt_val_1, etc.
            sample_id = f"{split}_{idx}"
            
            # 2. Raw Label (No Normalization)
            # We treat the raw label (True/False) as the gold standard
            raw_label = str(data.get("label", "False"))
            
            sample = FactCheckSample(
                id=sample_id,
                claim=data.get("claim"),
                gold_label=raw_label,   # Keeps "True", "False", "Conflicting"
                gold_evidence=[],       # Empty (Retrieval accuracy ignored)
                mode="always_retrieve",
                metrics=FactCheckMetrics(latency_seconds=0.0, input_tokens=0, output_tokens=0)
            )
            samples.append(sample)
            
        print(f"Loaded {len(samples)} Quantemp samples.")
        return samples

    def _extract_scifact_label(self, data: dict) -> str:
        """
        Derives a single gold label from SciFact's evidence dictionary.
        """
        evidence = data.get("evidence", {})
        
        # Case 1: Empty evidence dict -> No info
        if not evidence:
            return "NOT ENOUGH INFO"
        
        # Case 2: Iterate through evidence sets to find a label
        # structure: {"doc_id": [{"sentences": [4], "label": "CONTRADICT"}]}
        for doc_id, evidences in evidence.items():
            for ev in evidences:
                if "label" in ev:
                    return ev["label"] # Returns "SUPPORT" or "CONTRADICT"
        
        return "NOT ENOUGH INFO"