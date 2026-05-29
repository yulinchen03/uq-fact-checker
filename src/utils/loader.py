import json
from pathlib import Path
from typing import List
from src.data_models import FactCheckSample, FactCheckMetrics

class LocalDataLoader:
    def __init__(self, data_root: str = "./data"):
        self.data_root = Path(data_root)

    def load(self, dataset_name: str, split: str, mode: str = "always_retrieve") -> List[FactCheckSample]:
        dataset_name = dataset_name.lower()
        base_path = self.data_root / dataset_name
        
        file_jsonl = base_path / f"claims_{split}.jsonl"
        file_json = base_path / f"claims_{split}.json"
        
        if file_jsonl.exists():
            file_path = file_jsonl
            is_jsonl = True
        elif file_json.exists():
            file_path = file_json
            is_jsonl = False
        else:
            raise FileNotFoundError(f"Claims file not found for {dataset_name} at {base_path}")

        print(f"Loading {dataset_name} from {file_path}...")

        if is_jsonl:
            with open(file_path, 'r', encoding='utf-8') as f:
                data_list = [json.loads(line) for line in f if line.strip()]
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                data_list = json.load(f)

        samples = []
        for idx, data in enumerate(data_list):
            sample_id = str(data.get("id", f"{split}_{idx}"))
            
            if "label" in data:
                raw_label = str(data["label"])
            else:
                raw_label = self._extract_scifact_label(data)
                
            gold_ids = []
            evidence = data.get("evidence")
            
            if isinstance(evidence, dict):
                gold_ids = list(evidence.keys())
            elif isinstance(evidence, list):
                gold_ids = [str(x) for x in evidence if not isinstance(x, dict)]
            
            if not gold_ids:
                if data.get("cited_doc_ids"):
                    gold_ids = [str(x) for x in data["cited_doc_ids"]]

            sample = FactCheckSample(
                id=sample_id,
                claim=data.get("claim", ""),
                gold_label=raw_label,
                gold_evidence=gold_ids,
                mode=mode,
                metrics=FactCheckMetrics(latency_seconds=0.0, input_tokens=0, output_tokens=0)
            )
            samples.append(sample)
            
        print(f"Loaded {len(samples)} samples for {dataset_name}.")
        return samples

    def _extract_scifact_label(self, data: dict) -> str:
        """Derives a single gold label from SciFact's nested evidence dictionary."""
        evidence = data.get("evidence", {})
        if not evidence:
            return "NOT ENOUGH INFO"
        
        for doc_id, evidences in evidence.items():
            for ev in evidences:
                if "label" in ev:
                    return ev["label"]
        
        return "NOT ENOUGH INFO"