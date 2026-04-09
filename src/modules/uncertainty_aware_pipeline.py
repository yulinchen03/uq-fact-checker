import logging
import json
import re

from lm_polygraph.model_adapters import WhiteboxModelvLLM
from vllm import SamplingParams
from src.utils.metrics import MetricsRecorder
from .abstract_components import PipelineComponent
from .uncertainty_aware_verifier import UQVerifier
from src.data_models import FactCheckSample


class UncertaintyAwarePipeline(PipelineComponent):
    def __init__(self, cfg, retriever, aggregator, rag_verifier, model=None, tokenizer=None):
        self.cfg = cfg
        self.tokenizer = tokenizer

        # Initialize lm-polygraph using vLLM adapter
        if model and tokenizer:
            max_tokens = getattr(cfg.llm, "max_new_tokens", 1024)
            
            # Use vLLM SamplingParams instead of GenerationParameters
            gen_params = SamplingParams(
                temperature=0.0,
                max_tokens=max_tokens,
                logprobs=5,
                # Added <|im_start|> and <|start_header_id|> to instantly kill roleplaying
                stop=["<|im_end|>", "<|eot_id|>", "```", "<|im_start|>", "<|start_header_id|>"]
            )
            
            # Pass the vLLM engine directly into WhiteboxModelvLLM
            self.whitebox_model = WhiteboxModelvLLM(
                model,
                sampling_params=gen_params
            )

            # --- HOTFIX FOR LM-POLYGRAPH VLLM BUG ---
            self.whitebox_model.supports_logprobs = True
            # ----------------------------------------
        
        self.retriever = retriever
        self.aggregator = aggregator
        self.rag_verifier = rag_verifier

        # UQ Engine (Parametric)
        self.uq_engine = UQVerifier(
            model=self.whitebox_model,
            estimator_name=cfg.uncertainty.method
        )
        
        # Prompts
        self.dataset = cfg.data.dataset_name.lower()
        self.parametric_prompt = cfg.prompts.parametric
        self.threshold = cfg.uncertainty.threshold
        self.calibration_mode = cfg.uncertainty.get("calibration_mode", False)

        self.verdict_parser = {
            "scifact": self._parse_scifact,
            "quantemp": self._parse_quantemp
        }

    def process(self, sample: FactCheckSample) -> FactCheckSample:
        # ===== STEP 1: Whole-Claim UQ Pass =====
        raw_response, score, parametric_verdict, parametric_explanation = self._run_uq_pass(sample)

        sample.uncertainty_score = score
        sample.parametric_response = raw_response
        sample.parametric_verdict = parametric_verdict

        # ===== Calibration Mode: UQ-only, skip everything else =====
        if self.calibration_mode:
            sample.predicted_verdict = parametric_verdict
            sample.explanation = parametric_explanation
            sample.decomp_triggered = False
            return sample

        # ===== STEP 2: Decision =====
        is_uncertain = score >= self.threshold

        if not is_uncertain:
            # [CONFIDENT] Return the parametric verdict directly
            sample.predicted_verdict = parametric_verdict
            sample.explanation = parametric_explanation
            sample.decomp_triggered = False
            return sample

        # ===== STEP 3: RAG Pass (Only if Uncertain) =====
        sample.decomp_triggered = True
        
        sample = self.retriever.process(sample)
        sample = self.aggregator.process(sample)
        
        # This will set sample.explanation to the newly generated RAG explanation
        sample = self.rag_verifier.process(sample) 
        
        sample.rag_prediction = sample.predicted_verdict 

        return sample

    # -------------------------------------------------------------------------
    # Internal Helpers
    # -------------------------------------------------------------------------

    def _run_uq_pass(self, sample: FactCheckSample):
        """Runs the claim through UQ verifier and parses the response."""
        clean_prompt = self.parametric_prompt.format(claim=sample.claim).replace("```json", "").strip()
        messages = [{"role": "user", "content": clean_prompt}]
        full_prompt = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        # Append the hanging JSON tag so the model is forced to close it
        full_prompt += "```json\n"

        raw_response, score = self.uq_engine.estimate(full_prompt)

        # lm-polygraph often returns the full sequence (prompt + generation)
        # Strip the prompt out to avoid double-counting tokens and JSON parse errors
        clean_response = raw_response
        if full_prompt in raw_response:
            clean_response = raw_response.replace(full_prompt, "", 1).strip()
        elif raw_response.startswith(full_prompt.strip()):
            clean_response = raw_response[len(full_prompt.strip()):].strip()

        if self.tokenizer:
            prompt_tokens = len(self.tokenizer.encode(full_prompt))
            response_tokens = len(self.tokenizer.encode(clean_response)) if clean_response else 0
            MetricsRecorder.record_token_usage(
                sample,
                input_tokens=prompt_tokens,
                output_tokens=response_tokens,
                step="uq"
            )
            MetricsRecorder.record_llm_call(sample)

        # Parse the response
        final_clean = clean_response.strip().replace("```json", "").replace("```", "").strip()

        # NON-GREEDY JSON Extraction to prevent multi-block merging
        json_target = final_clean
        json_match = re.search(r'(\{.*?\})', final_clean, re.DOTALL)
        if json_match:
            json_target = json_match.group(1)

        verdict = self._parse_verdict(json_target)

        try:
            parsed_json = json.loads(json_target)
            explanation = parsed_json.get("explanation", "No explanation could be extracted from the model response.")
            if "verdict" in parsed_json:
                verdict = self._parse_verdict(parsed_json["verdict"])
        except json.JSONDecodeError:
            explanation = f"Failed to parse explanation. Raw output: {final_clean}"

        return final_clean, score, verdict, explanation

    def _parse_verdict(self, text):
        strategy = self.verdict_parser.get(self.dataset)
        if strategy:
            return strategy(text)
        else:
            return "NOT ENOUGH INFO"

    def _parse_scifact(self, text):
        t = text.upper()
        if "SUPPORT" in t: return "SUPPORT"
        if "CONTRADICT" in t or "REFUTE" in t: return "CONTRADICT"
        return "NOT ENOUGH INFO"

    def _parse_quantemp(self, text):
        t = text.upper()
        if "FALSE" in t: return "False"
        if "TRUE" in t: return "True"
        if "CONFLICT" in t: return "Conflicting"
        return "Conflicting"