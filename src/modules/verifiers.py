import json
import re
from typing import Dict, Any
from .base import PipelineComponent
from src.utils.metrics import MetricsRecorder

class LLMVerifier(PipelineComponent):
    """Verifies claims using an LLM with RAG or parametric templates."""

    def __init__(self, llm_client, cfg):
        self.llm_client = llm_client
        self.cfg = cfg

    def process(self, sample):
        # 1. Select Template
        if sample.mode == "always_retrieve":
            template = self.cfg.prompts.rag
            context = sample.aggregated_context if sample.aggregated_context else "No relevant evidence found."
            prompt = template.format(claim=sample.claim, context=context)
            
        elif sample.mode == "never_retrieve":
            template = self.cfg.prompts.parametric
            prompt = template.format(claim=sample.claim)

        elif sample.mode == "UQ-aware":
            # TODO: Implement uncertainty-aware logic to choose between RAG and parametric templates based on sample.uncertainty_score
            pass
            
        else:
            raise ValueError(f"Unknown mode: {sample.mode}")

        # 2. Prepare Config (Map generic config to HF specific params)
        generation_config = {
            "temperature": self.cfg.llm.get("temperature", 0.1),
            "max_new_tokens": self.cfg.llm.get("max_new_tokens", 512), 
            "do_sample": self.cfg.llm.get("do_sample", False)
        }

        # 3. Generate
        # We assume llm_client.generate takes the raw prompt string
        response = self.llm_client.generate(prompt, generation_config)

        # 4. Record Metrics
        # Use the helper class because sample.metrics is a Pydantic object, not a dict
        usage = response.get("usage", {})
        MetricsRecorder.record_token_usage(
            sample,
            input_tokens=usage.get("input_tokens", 0),
            output_tokens=usage.get("output_tokens", 0)
        )

        # 5. Parse Response
        verdict, explanation = self._parse_response(response.get("content", ""))
        
        # 6. Update Sample
        sample.predicted_verdict = verdict
        sample.explanation = explanation

        # --- DEBUG PRINT: Show the Prompt ---
        if self.cfg.llm.debug:
            print("\n" + "="*40)
            print(f"[DEBUG] PROMPT for Claim {sample.id}:")
            print("-" * 40)
            print(prompt.strip())
        print("="*40 + "\n")
        print(f"[DEBUG] Response for Claim {sample.id}:")
        print(sample.predicted_verdict + ". " + sample.explanation)
        print("\n" + "="*40)
        # ------------------------------------

        return sample

    def _parse_response(self, text: str) -> tuple:
        """
        Robustly parses LLM response, handling Markdown code blocks.
        """
        clean_text = text.strip()
        
        # Fix: Strip Markdown Code Blocks if present (Common in Qwen/Llama)
        # Matches ```json {content} ``` or ``` {content} ```
        code_block_pattern = r"```(?:json)?\s*(.*?)\s*```"
        match = re.search(code_block_pattern, clean_text, re.DOTALL)
        if match:
            clean_text = match.group(1)

        verdict = "NOT ENOUGH INFO" # Default safety fallback
        explanation = "Parsing failed."

        try:
            # Try parsing as JSON
            data = json.loads(clean_text)
            verdict = data.get("verdict", verdict)
            explanation = data.get("explanation", explanation)
        except json.JSONDecodeError:
            # Fall back to regex extraction on the cleaned text
            # Look for "Verdict: Supported" pattern
            verdict_match = re.search(r'verdict["\']?\s*:\s*["\']?(\w+)', clean_text, re.IGNORECASE)
            explanation_match = re.search(r'explanation["\']?\s*:\s*["\']?(.+?)(?:["\']|$)', clean_text, re.IGNORECASE)

            if verdict_match:
                verdict = verdict_match.group(1)
            if explanation_match:
                explanation = explanation_match.group(1)

        # Normalize verdict to uppercase for consistency
        return verdict.upper(), explanation