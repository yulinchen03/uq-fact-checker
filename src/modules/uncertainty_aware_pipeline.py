import json
import logging
import os

from lm_polygraph.utils.model import WhiteboxModel
from lm_polygraph.utils.generation_parameters import GenerationParameters
from src.utils.metrics import MetricsRecorder
from .abstract_components import PipelineComponent
from .uncertainty_aware_verifier import LMPolygraphWrapper
from src.data_models import FactCheckSample


class UncertaintyAwarePipeline(PipelineComponent):
    def __init__(self, cfg, retriever, aggregator, rag_verifier, model=None, tokenizer=None):
        self.cfg = cfg

        # pad input and outputs
        if tokenizer.pad_token_id is None:
                tokenizer.pad_token = tokenizer.eos_token
                tokenizer.pad_token_id = tokenizer.eos_token_id

        # Initialize lm-polygraph using the SHARED objects
        if model and tokenizer:
            max_tokens = getattr(cfg.llm, "max_new_tokens", 1024)
            
            gen_params = GenerationParameters(
                temperature=None,
                do_sample=False,
                max_new_tokens=max_tokens,
                stop_strings=["<|im_end|>"]
            )
            
            self.whitebox_model = WhiteboxModel(
                model=model,
                tokenizer=tokenizer,
                model_path=cfg.llm.model_name,
                generation_parameters=gen_params
            )
        
        self.retriever = retriever
        self.aggregator = aggregator
        self.rag_verifier = rag_verifier

        # UQ Engine (Parametric)
        self.uq_engine = LMPolygraphWrapper(
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
        # --- STEP 1: Parametric Generation + UQ ---
        full_prompt = self.parametric_prompt.format(claim=sample.claim)
        
        # Get text and score concurrently from LM-Polygraph
        response, score = self.uq_engine.estimate(full_prompt)

        if hasattr(self, 'whitebox_model') and self.whitebox_model.tokenizer:
            prompt_tokens = len(self.whitebox_model.tokenizer.encode(full_prompt))
            # Handle cases where the response might be empty safely
            response_tokens = len(self.whitebox_model.tokenizer.encode(response)) if response else 0
            
            # Record the tokens consumed during the UQ pass
            MetricsRecorder.record_token_usage(
                sample,
                input_tokens=prompt_tokens,
                output_tokens=response_tokens
            )
        
        # Store State
        sample.uncertainty_score = score
        sample.parametric_response = response
        sample.parametric_verdict = self._parse_verdict(response)

        print(f"Uncertainty score: {score}, threshold: {self.threshold}")

        # --- STEP 2: Decision ---
        # If calibration_mode is ON, we effectively force retrieval to log data
        is_uncertain = score >= self.threshold
        should_retrieve = is_uncertain or self.calibration_mode

        print(f"Retrieve?: {should_retrieve}")

        if not should_retrieve:
            # [CASE A: CONFIDENT] 
            sample.predicted_verdict = sample.parametric_verdict
            
            # Attempt to parse the actual explanation from the LLM's JSON output
            try:
                # Clean markdown formatting if the model still outputs it
                clean_response = response.strip().strip("`").removeprefix("json").strip()
                parsed_json = json.loads(clean_response)
                sample.explanation = parsed_json.get("explanation", "No explanation provided by model.")
            except json.JSONDecodeError:
                sample.explanation = f"Failed to parse explanation. Raw output: {response}"
                
            sample.retrieval_triggered = False
            return sample

        # --- STEP 3: The "Typical One Pass RAG" (Only if Uncertain) ---
        sample.retrieval_triggered = True
        
        # A. Retrieve
        sample = self.retriever.process(sample)
        
        # B. Aggregate Context
        sample = self.aggregator.process(sample)
        
        # C. Verify (RAG)
        # The rag_verifier uses the RAG prompt (configured in build_pipeline)
        sample = self.rag_verifier.process(sample)
        
        # D. Save RAG result separately
        sample.rag_prediction = sample.predicted_verdict 
        
        # E. Calibration Logic
        # If we are calibrating, we save BOTH verdicts but flag the explanation
        if self.calibration_mode:
            sample.explanation = (
                f"[CALIBRATION] Score: {score:.4f} | "
                f"Para: {sample.parametric_verdict} | RAG: {sample.rag_prediction}"
            )
            # Default to RAG verdict for the final output file
            sample.predicted_verdict = sample.rag_prediction 

        return sample
    
    def _parse_verdict(self, text):
        """
        Dynamically routes to the correct parser based on the active dataset.
        """
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