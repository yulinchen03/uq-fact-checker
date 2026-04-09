import os
import re
import time
import hydra
from omegaconf import DictConfig
from typing import Dict, Any
from .abstract_components import PipelineComponent
from src.utils.metrics import MetricsRecorder

# Force vLLM to use spawn for multiprocessing workers
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"

from src.utils.llm_client import LocalLLMClient

class AtomicDecomposer(PipelineComponent):
    """Decomposes a complex claim into atomic facts for FActScore verification."""

    def __init__(self, llm_client, cfg):
        self.llm_client = llm_client
        self.cfg = cfg
        
        self.prompt_template = self.cfg.decomposer.prompt

    def process(self, sample):
        # print(f"[DEBUG] DECOMPOSER INPUT | CLAIM: {sample.claim}")
        prompt = self.prompt_template.format(claim=sample.claim)
        
        generation_config = {
            "max_new_tokens": 256, 
        }

        # Generate Decomposition
        response = self.llm_client.generate(prompt, generation_config)

        # Record Metrics
        usage = response.get("usage", {})
        MetricsRecorder.record_token_usage(
            sample,
            input_tokens=usage.get("input_tokens", 0),
            output_tokens=usage.get("output_tokens", 0),
            step="decompose"
        )
        MetricsRecorder.record_llm_call(sample)

        # Parse and store facts
        raw_text = response.get("content", "")
        sample.atomic_facts = self._parse_facts(raw_text)
        
        # Fallback if parsing fails completely
        if not sample.atomic_facts:
            sample.atomic_facts = [sample.claim]

        # ==========================================
        # DEBUG PRINT: Original vs Decomposed Claims
        # ==========================================
        # print("\n" + "="*50)
        # print("Decomposing claim...")
        # print(f"🛠️ [DEBUG] DECOMPOSER OUTPUT | ID: {sample.id}")
        # print("-" * 50)
        # print(f"📍 ORIGINAL CLAIM:\n{sample.claim}\n")
        # print(f"✂️  DECOMPOSED CLAIM INTO ({len(sample.atomic_facts)} ATOMIC CLAIMS):")
        # for idx, fact in enumerate(sample.atomic_facts):
        #     print(f"  {idx + 1}. {fact}")
        # print("="*50)
        # ==========================================

        return sample

    def _parse_facts(self, text: str) -> list[str]:
        facts = []
        for line in text.split('\n'):
            line = line.strip()
            if line.startswith('- ') or line.startswith('* '):
                cleaned_fact = re.sub(r'^[-*]\s*', '', line).strip()
                if cleaned_fact:
                    facts.append(cleaned_fact)
            elif re.match(r'^\d+\.\s', line):
                cleaned_fact = re.sub(r'^\d+\.\s*', '', line).strip()
                if cleaned_fact:
                    facts.append(cleaned_fact)
                    
        if not facts and text.strip():
            facts = [f.strip() for f in text.split('.') if f.strip()]
            
        return facts

@hydra.main(version_base=None, config_path="../../config", config_name="config")
def main(cfg: DictConfig):
    from src.data_models import FactCheckSample

    print("🚀 Initializing vLLM Client for Decomposer Test...")

    # Initialize your standard Qwen model 
    llm = LocalLLMClient(model_name="Qwen/Qwen3-4B-Instruct-2507")
    
    decomposer = AtomicDecomposer(llm, cfg)
    
    test_samples = [
        FactCheckSample(
            id="test_1",
            claim="Since 2000, global extreme poverty has fallen by more than half, from nearly 30 percent of the global population to less than 10 percent.",
            mode="factscore"
        ),
        FactCheckSample(
            id="test_2",
            claim="0-dimensional biomaterials lack inductive properties.",
            mode="factscore"
        ),
        FactCheckSample(
            id="test_3",
            claim="A T helper 2 cell (Th2) environment impedes disease development in patients with systemic lupus erythematosus (SLE).",
            mode="factscore"
        )
    ]
    
    print("\n" + "="*60)
    print("🔬 RUNNING ATOMIC DECOMPOSER (PIPELINE MODE)")
    print("="*60)
    
    for i, sample in enumerate(test_samples):
        print(f"\n[{i+1}] Testing Sample ID: {sample.id}")
        print(f"Original Claim : {sample.claim}")
                
        try:
            processed_sample = decomposer.process(sample)
            print(processed_sample)
        except Exception as e:
            print(f"Error processing claim: {e}")
            continue
                        
    print("\n✅ Testing Complete!")

if __name__ == "__main__":
    main()