from abc import ABC, abstractmethod
import logging
from lm_polygraph.estimators import MaximumSequenceProbability, MeanTokenEntropy
from lm_polygraph.utils import estimate_uncertainty

logging.getLogger("lm_polygraph").setLevel(logging.WARNING)

class UQEstimator(ABC):
    """Abstract Base Class for any Uncertainty Method"""
    
    @abstractmethod
    def estimate(self, full_prompt: str):
        """
        Args:
            full_prompt (str): The complete input text (Instruction + Claim) 
                               that the model would see in a standard parametric run.
        Returns: 
            tuple(generation_text: str, uncertainty_score: float)
        """
        pass

class LMPolygraphWrapper(UQEstimator):
    def __init__(self, model, estimator_name="MaximumSequenceProbability"):
        # We assume 'model' here is the HuggingFace model object loaded in main.py
        # You might need to load the tokenizer here or pass it in if LM-Polygraph requires it separately
        self.model = model 
        
        # Load the specific estimator
        if estimator_name == "MaximumSequenceProbability":
            self.estimator = MaximumSequenceProbability()
        elif estimator_name == "MeanTokenEntropy":
            self.estimator = MeanTokenEntropy()

    def estimate(self, full_prompt: str):   
        # We pass the FULL PROMPT as input_text
        result = estimate_uncertainty(
            self.model, 
            self.estimator, 
            input_text=full_prompt 
        )
        
        # Return the generated text (response) and the calculated uncertainty
        return result.generation_text, float(result.uncertainty)