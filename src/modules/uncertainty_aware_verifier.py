from abc import ABC, abstractmethod
import logging
import lm_polygraph.estimators as estimators
from lm_polygraph.utils import estimate_uncertainty

logging.getLogger("lm_polygraph").setLevel(logging.WARNING)

class UQEstimator(ABC):
    """Abstract Base Class for any Uncertainty Method"""
    
    @abstractmethod
    def estimate(self, full_prompt: str):
        pass

class LMPolygraphWrapper(UQEstimator):
    def __init__(self, model, estimator_name="MaximumSequenceProbability"):
        self.model = model 
        
        # Dynamically fetch and instantiate the estimator class based on the string name
        try:
            estimator_class = getattr(estimators, estimator_name)
            self.estimator = estimator_class()
        except AttributeError:
            raise ValueError(f"Estimator '{estimator_name}' is not supported by lm_polygraph.estimators.")
        except TypeError as e:
            # Catch estimators that strictly require initialization arguments (like Rouge scores)
            logging.warning(f"Could not initialize {estimator_name} with default arguments: {e}")
            raise

    def estimate(self, full_prompt: str):   
        try:
            result = estimate_uncertainty(
                    self.model, 
                    self.estimator, 
                    input_text=full_prompt 
                )
            
        except Exception as e:
            logging.warning(f"Error in estimating uncertainty: {e}")
            return "Error in estimation", float('inf')

        return result.generation_text, float(result.uncertainty)
    