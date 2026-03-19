import logging
import json
import os

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
                logprobs=10, # CRITICAL: lm-polygraph needs logprobs to calculate UQ!
                stop=["<|im_end|>"]
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
        # Format the prompt using chat template
        messages = [{"role": "user", "content": self.parametric_prompt.format(claim=sample.claim)}]
        full_prompt = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        
        # Get text and score concurrently from LM-Polygraph
        response, score = self.uq_engine.estimate(full_prompt)

        if self.tokenizer:
            prompt_tokens = len(self.tokenizer.encode(full_prompt))
            response_tokens = len(self.tokenizer.encode(response)) if response else 0
            
            # Record the tokens consumed during the UQ pass
            MetricsRecorder.record_token_usage(
                sample,
                input_tokens=prompt_tokens,
                output_tokens=response_tokens
            )
        
        # Store State
        sample.uncertainty_score = score
        
        # Clean up JSON backticks if LM-Polygraph missed them
        clean_response = response.strip().replace("```json", "").replace("```", "").strip()
        sample.parametric_response = clean_response
        sample.parametric_verdict = self._parse_verdict(clean_response)
        
        # ALWAYS extract the parametric explanation, regardless of retrieval decision
        try:
            parsed_json = json.loads(clean_response)
            parametric_explanation = parsed_json.get("explanation", "No explanation provided by model.")
        except json.JSONDecodeError:
            parametric_explanation = f"Failed to parse explanation. Raw output: {clean_response}"

        # print(f"Uncertainty score: {score:.4f}, threshold: {self.threshold}")

        # --- STEP 2: Decision ---
        is_uncertain = score >= self.threshold
        should_retrieve = is_uncertain or self.calibration_mode

        if not should_retrieve:
            # [CASE A: CONFIDENT] 
            sample.predicted_verdict = sample.parametric_verdict
            sample.explanation = parametric_explanation
            sample.retrieval_triggered = False
            return sample

        # --- STEP 3: The "Typical One Pass RAG" (Only if Uncertain) ---
        sample.retrieval_triggered = True
        
        sample = self.retriever.process(sample)
        sample = self.aggregator.process(sample)
        
        # This will set sample.explanation to the newly generated RAG explanation
        sample = self.rag_verifier.process(sample) 
        
        sample.rag_prediction = sample.predicted_verdict 
        
        if self.calibration_mode:
            # APPEND the calibration info
            calibration_string = (
                f"\n\n[CALIBRATION INFO] Score: {score:.4f} | "
                f"Parametric Verdict: {sample.parametric_verdict} | RAG Verdict: {sample.rag_prediction}"
            )
            # Combine the LLM's explanation with the calibration debug string
            sample.explanation = str(sample.explanation) + calibration_string
            sample.predicted_verdict = sample.rag_prediction 

        return sample
    
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