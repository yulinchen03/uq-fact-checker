import json
import re
from typing import Dict, Any
from .abstract_components import PipelineComponent
from src.utils.metrics import MetricsRecorder

class LLMVerifier(PipelineComponent):
    """Verifies claims using an LLM with RAG or parametric templates."""

    def __init__(self, llm_client, cfg):
        self.llm_client = llm_client
        self.cfg = cfg
        self.dataset = cfg.data.dataset_name.lower()
        self.output_format = cfg.get("output_format", "label_only")

    def process(self, sample):
        if sample.mode in ("always_retrieve", "openai_always_retrieve", "uq_aware", "uq_decompose"):
            if self.output_format == "label_only":
                template = self.cfg.prompts.rag_short
            else:
                template = self.cfg.prompts.rag_long
                
            context = sample.aggregated_context if sample.aggregated_context else "No relevant evidence found."
            prompt = template.format(claim=sample.claim, context=context)
            
        elif sample.mode in ("never_retrieve", "openai_never_retrieve"):
            if self.output_format == "label_only":
                template = self.cfg.prompts.parametric_short
            else:
                template = self.cfg.prompts.parametric_long
                
            prompt = template.format(claim=sample.claim)
        
        else:
            raise ValueError(f"Unknown mode: {sample.mode}")

        prompt = prompt.replace("```json", "").strip()
        
        if self.output_format == "label_only":
            if not prompt.endswith("Verdict:"):
                prompt += "\nVerdict:"
            max_tokens = 5
        else:
            prompt += "\n```json\n"
            max_tokens = self.cfg.llm.get("max_new_tokens", 1024)

        generation_config = {
            "max_new_tokens": max_tokens, 
            "output_format": self.output_format,
            "dataset": self.dataset
        }

        response = self.llm_client.generate(prompt, generation_config)

        usage = response.get("usage", {})
        MetricsRecorder.record_token_usage(
            sample,
            input_tokens=usage.get("input_tokens", 0),
            output_tokens=usage.get("output_tokens", 0),
            step="generation"
        )
        MetricsRecorder.record_llm_call(sample)

        raw_content = response.get("content", "")
        verdict, explanation = self._parse_response(raw_content)
        
        sample.predicted_verdict = verdict
        sample.explanation = explanation

        return sample

    def _parse_response(self, text: str) -> tuple:
        clean_text = text.strip().replace("```json", "").replace("```", "").strip()
        
        verdict_str = clean_text
        explanation = "Label only generation." if self.output_format == "label_only" else "Parsing failed."

        match = re.search(r'(\{.*\})', clean_text, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group(1))
                verdict_str = data.get("verdict", verdict_str)
                explanation = data.get("explanation", explanation)
            except json.JSONDecodeError:
                pass
        elif self.output_format == "full_response":
            verdict_match = re.search(r'"?verdict"?\s*:\s*"?([A-Za-z_]+)"?', clean_text, re.IGNORECASE)
            if verdict_match:
                verdict_str = verdict_match.group(1)
                
            explanation_match = re.search(r'"?explanation"?\s*:\s*"?(.+?)(?:"\s*\}|"$)', clean_text, re.IGNORECASE | re.DOTALL)
            if explanation_match:
                explanation = explanation_match.group(1).strip()
                
        t = str(verdict_str).upper()
        
        if self.dataset == "scifact":
            if "SUPPORT" in t: verdict = "SUPPORT"
            elif "CONTRADICT" in t or "REFUTE" in t: verdict = "CONTRADICT"
            else: verdict = "NOT ENOUGH INFO"
            
        elif self.dataset == "quantemp":
            if "FALSE" in t: verdict = "False"
            elif "TRUE" in t: verdict = "True"
            elif "CONFLICT" in t: verdict = "Conflicting"
            else: verdict = "Conflicting"
            
        else:
            verdict = "NOT ENOUGH INFO"

        return verdict, explanation