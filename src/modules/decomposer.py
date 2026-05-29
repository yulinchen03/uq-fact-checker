import os
import re
from .abstract_components import PipelineComponent
from src.utils.metrics import MetricsRecorder

os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"

from src.utils.llm_client import LocalLLMClient

class AtomicDecomposer(PipelineComponent):
    """Decomposes a complex claim into atomic facts for granular verification."""

    def __init__(self, llm_client, cfg):
        self.llm_client = llm_client
        self.cfg = cfg
        self.prompt_template = self.cfg.decomposer.prompt

    def process(self, sample):
        prompt = self.prompt_template.format(claim=sample.claim)
        
        generation_config = {
            "max_new_tokens": 256, 
            "output_format": "full_response",
        }

        response = self.llm_client.generate(prompt, generation_config)

        usage = response.get("usage", {})
        MetricsRecorder.record_token_usage(
            sample,
            input_tokens=usage.get("input_tokens", 0),
            output_tokens=usage.get("output_tokens", 0),
            step="decompose"
        )
        MetricsRecorder.record_llm_call(sample)

        raw_text = response.get("content", "")
        sample.atomic_facts = self._parse_facts(raw_text)
        
        if not sample.atomic_facts:
            sample.atomic_facts = [sample.claim]

        # print("\n" + "="*50)
        # print("Decomposing claim...")
        # print(f"🛠️ [DEBUG] DECOMPOSER OUTPUT | ID: {sample.id}")
        # print("-" * 50)
        # print(f"📍 ORIGINAL CLAIM:\n{sample.claim}\n")
        # print(f"✂️  DECOMPOSED CLAIM INTO ({len(sample.atomic_facts)} ATOMIC CLAIMS):")
        # for idx, fact in enumerate(sample.atomic_facts):
        #     print(f"  {idx + 1}. {fact}")
        # print("="*50)

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