import logging
import os

from transformers import AutoModelForCausalLM, AutoTokenizer
from lm_polygraph.utils.model import WhiteboxModel
import transformers
from .base import PipelineComponent
from .uq import LMPolygraphWrapper
from src.data_models import FactCheckSample


class UQAwareFlow(PipelineComponent):
    def __init__(self, cfg, retriever, aggregator, rag_verifier, model=None, tokenizer=None):
        self.cfg = cfg

        # Initialize lm-polygraph using the SHARED objects
        if model and tokenizer:
            self.whitebox_model = WhiteboxModel(
                model=model,
                tokenizer=tokenizer,
                model_path=cfg.llm.model_name
            )
        
        # Tools (Standard components passed in)
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
        
        # Store State
        sample.uncertainty_score = score
        sample.parametric_response = response
        sample.parametric_verdict = self._parse_verdict(response)

        # --- STEP 2: Decision ---
        # If calibration_mode is ON, we effectively force retrieval to log data
        is_uncertain = score >= self.threshold
        should_retrieve = is_uncertain or self.calibration_mode

        if not should_retrieve:
            # [CASE A: CONFIDENT] 
            # Stop here. Use parametric answer as final.
            sample.predicted_verdict = sample.parametric_verdict
            sample.explanation = f"Parametric Confidence (Score: {score:.4f})"
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