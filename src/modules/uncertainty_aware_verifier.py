from abc import ABC, abstractmethod
import logging
import lm_polygraph.estimators as estimators
from lm_polygraph.stat_calculators.greedy_probs import GreedyProbsCalculator
from lm_polygraph.stat_calculators.entropy import EntropyCalculator
import numpy as np


def get_safe_logger():
    l = logging.getLogger(__name__)
    if not l.handlers:
        logging.basicConfig(level=logging.INFO)
    return l


logger = get_safe_logger()

# Estimators that require greedy_log_probs directly
LOGPROB_METRICS = ["Perplexity", "MaximumSequenceProbability"]

# Estimators that require a pre-computed entropy stat
ENTROPY_METRICS = ["MeanTokenEntropy"]


class UQEstimator(ABC):
    """Abstract Base Class for any Uncertainty Method."""

    @abstractmethod
    def estimate(self, full_prompt: str):
        pass


class UQVerifier(UQEstimator):
    def __init__(self, model, estimator_name):
        """
        Initializes the UQ wrapper using lm-polygraph's low-level API.

        Args:
            model: WhiteboxModelvLLM instance.
            estimator_name: Name of the lm-polygraph estimator class to use,
                            e.g. "MeanTokenEntropy", "Perplexity".
        """
        self.model = model
        self.estimator_name = estimator_name

        self.greedy_calculator = GreedyProbsCalculator(
            output_attentions=False,
            output_hidden_states=False,
        )
        self.entropy_calculator = EntropyCalculator()

        try:
            estimator_class = getattr(estimators, self.estimator_name)
            self.estimator = estimator_class()
            logger.info(f"Loaded UQ estimator: {self.estimator_name}")
        except AttributeError:
            available = [e for e in dir(estimators) if not e.startswith("__")]
            logger.error(
                f"Estimator '{self.estimator_name}' not found. "
                f"Available estimators: {available}"
            )
            raise

    def estimate(self, prompt: str):
        """
        Runs the UQ pipeline for a single prompt.

        Returns:
            Tuple of (generated_text: str, uncertainty_score: float).
            On failure, returns a fallback JSON string and float('inf').
        """
        texts = [prompt]
        model_outputs = {"input_texts": texts}

        try:
            # Step 1: Compute greedy decoding stats (tokens, log probs, texts)
            greedy_prob_results = self.greedy_calculator(model_outputs, texts=texts, model=self.model)
            model_outputs.update(greedy_prob_results)

            # Step 2: Safety check — ensure log probs were populated for logprob-based metrics
            if self.estimator_name in LOGPROB_METRICS and "greedy_log_probs" not in model_outputs:
                logger.warning(f"greedy_log_probs missing for estimator '{self.estimator_name}'.")
                return self._fallback_error("Missing greedy_log_probs")

            # Step 3: Compute entropy stats if required by the estimator
            if self.estimator_name in ENTROPY_METRICS:
                entropy_results = self.entropy_calculator(model_outputs, texts=texts, model=self.model)
                model_outputs.update(entropy_results)

            # Step 4: Run the UQ estimator
            scores = self.estimator(model_outputs)
            score = scores[0] if isinstance(scores, (list, np.ndarray)) else scores

            # Step 5: Extract generated text
            if model_outputs.get("greedy_texts"):
                generated_text = model_outputs["greedy_texts"][0]
            else:
                # Fallback: decode token IDs manually via the vLLM tokenizer
                tokenizer = self.model.model.get_tokenizer()
                token_ids = model_outputs.get("greedy_tokens", [[]])[0]
                generated_text = tokenizer.decode(token_ids, skip_special_tokens=True)

            return generated_text.strip(), float(score)

        except Exception as e:
            logger.error(f"UQ estimation failed ({self.estimator_name}): {e}", exc_info=True)
            return self._fallback_error(str(e))

    def _fallback_error(self, err_msg: str):
        """Returns a safe fallback state when UQ estimation fails."""
        fallback_json = f'{{"verdict": "NOT ENOUGH INFO", "explanation": "UQ Error: {err_msg}"}}'
        return fallback_json, float("inf")


# -- Fallback implementation using standard HuggingFace Transformers instead of vLLM --
#
# from lm_polygraph.utils import estimate_uncertainty
#
# class LMPolygraphWrapper(UQEstimator):
#     def __init__(self, model, estimator_name="MaximumSequenceProbability"):
#         self.model = model
#         try:
#             estimator_class = getattr(estimators, estimator_name)
#             self.estimator = estimator_class()
#         except AttributeError:
#             raise ValueError(f"Estimator '{estimator_name}' is not supported.")
#         except TypeError as e:
#             logging.warning(f"Could not initialize {estimator_name} with default args: {e}")
#             raise
#
#     def estimate(self, full_prompt: str):
#         try:
#             result = estimate_uncertainty(self.model, self.estimator, input_text=full_prompt)
#         except Exception as e:
#             logging.warning(f"Error estimating uncertainty: {e}")
#             return "Error in estimation", float("inf")
#         return result.generation_text, float(result.uncertainty)