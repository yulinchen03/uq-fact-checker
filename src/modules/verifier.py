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

    def process(self, sample):
        # 1. Select Template
        if sample.mode == "always_retrieve" or sample.mode == "uq_aware":
            template = self.cfg.prompts.rag
            context = sample.aggregated_context if sample.aggregated_context else "No relevant evidence found."
            prompt = template.format(claim=sample.claim, context=context)
            
        elif sample.mode == "never_retrieve":
            template = self.cfg.prompts.parametric
            prompt = template.format(claim=sample.claim)
        
        else:
            raise ValueError(f"Unknown mode: {sample.mode}")

        # 2. Prepare Config (Map generic config to HF specific params)
        generation_config = {
            "max_new_tokens": self.cfg.llm.get("max_new_tokens", 1024), 
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

        if self.cfg.llm.debug:
            print("x"*100)
            print("raw response:")
            print(response)
            print("x"*100)

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
        Robustly parses LLM response by isolating the JSON dictionary.
        """
        clean_text = text.strip()
        
        verdict = "NOT ENOUGH INFO"
        explanation = "Parsing failed."

        # 1. Isolate the JSON block (everything from the first '{' to the last '}')
        # re.DOTALL ensures it reads across newlines!
        match = re.search(r'(\{.*\})', clean_text, re.DOTALL)
        
        if match:
            json_string = match.group(1)
            try:
                data = json.loads(json_string)
                verdict = data.get("verdict", verdict)
                explanation = data.get("explanation", explanation)
                return verdict.upper(), explanation
            except json.JSONDecodeError:
                pass
                
        # 2. Aggressive Regex Fallback (Upgraded to handle newlines and formatting quirks)
        verdict_match = re.search(r'"?verdict"?\s*:\s*"?([A-Za-z_]+)"?', clean_text, re.IGNORECASE)
        if verdict_match:
            verdict = verdict_match.group(1)
            
        # Matches "explanation": "..." capturing across newlines until the closing brace
        explanation_match = re.search(r'"?explanation"?\s*:\s*"?(.+?)(?:"\s*\}|"$)', clean_text, re.IGNORECASE | re.DOTALL)
        if explanation_match:
            explanation = explanation_match.group(1).strip()

        return verdict.upper(), explanation