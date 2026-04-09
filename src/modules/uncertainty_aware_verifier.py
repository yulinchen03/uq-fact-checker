from abc import ABC, abstractmethod
import logging
import numpy as np
import lm_polygraph.estimators as estimators
from lm_polygraph.stat_calculators.greedy_probs import GreedyProbsCalculator
from lm_polygraph.stat_calculators.entropy import EntropyCalculator
from lm_polygraph.stat_calculators.stat_calculator import StatCalculator
from vllm import SamplingParams


def get_safe_logger():
    l = logging.getLogger(__name__)
    if not l.handlers:
        logging.basicConfig(level=logging.INFO)
    return l


logger = get_safe_logger()

# Estimators that require greedy_log_likelihoods directly
LOGPROB_METRICS = [
    "Perplexity", 
    "MaximumSequenceProbability",
    "MeanPointwiseMutualInformation",
    "MeanConditionalPointwiseMutualInformation"
]

# Estimators that require a pre-computed entropy stat
ENTROPY_METRICS = [
    "MeanTokenEntropy", 
    "MeanConditionalPointwiseMutualInformation" # CPMI explicitly requires stats["entropy"]
]

# Estimators that require unconditioned LM probabilities (P(x))
PMI_METRICS = [
    "MeanPointwiseMutualInformation",
    "MeanConditionalPointwiseMutualInformation"
]


class VLLMGreedyLMProbsCalculator(StatCalculator):
    """
    Custom Calculator for LM-Polygraph that calculates unconditioned sequence 
    probabilities (P(x)) using the vLLM engine, bypassing the HuggingFace dependency.
    """
    
    @staticmethod
    def meta_info():
        # Returns: (stats provided, stats depended upon)
        return (["greedy_lm_log_likelihoods"], ["greedy_tokens"])

    def __init__(self):
        super().__init__()

    def __call__(self, dependencies, texts, model, max_new_tokens=100, **kwargs):
        # model is WhiteboxModelvLLM, model.model is the vLLM engine
        llm = model.model
        greedy_tokens = dependencies.get("greedy_tokens", [])
        
        # Edge case: Empty generation
        if not greedy_tokens or not greedy_tokens[0]:
            return {"greedy_lm_log_likelihoods": [[0.0]]}
        
        # Configure vLLM to score the generated sequence as if it were a prompt
        sampling_params = SamplingParams(
            prompt_logprobs=1, 
            max_tokens=1, 
            temperature=0.0
        )
        
        # vLLM 0.6.0+ removes the 'prompt_token_ids' kwarg. 
        # Tokens must now be passed as a list of dictionaries to the first positional argument.
        vllm_inputs = [{"prompt_token_ids": tokens} for tokens in greedy_tokens]
        
        # Pass the generated token IDs directly to vLLM
        outputs = llm.generate(
            vllm_inputs, 
            sampling_params=sampling_params, 
            use_tqdm=False
        )
        
        lm_log_likelihoods = []
        for i, out in enumerate(outputs):
            seq_logprobs = []
            p_logprobs = out.prompt_logprobs
            
            for j, token_id in enumerate(greedy_tokens[i]):
                if j == 0 or p_logprobs[j] is None:
                    # First token has no prior context, logprob is effectively 0.0
                    seq_logprobs.append(0.0)
                else:
                    # Extract the logprob for the specific token at position j
                    if token_id in p_logprobs[j]:
                        val = p_logprobs[j][token_id]
                        # Account for different vLLM versions (Logprob object vs raw float)
                        logp = val.logprob if hasattr(val, "logprob") else val
                        seq_logprobs.append(logp)
                    else:
                        seq_logprobs.append(-100.0) # Safe fallback
                        
            lm_log_likelihoods.append(seq_logprobs)
            
        return {"greedy_lm_log_likelihoods": lm_log_likelihoods}


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
            estimator_name: Name of the lm-polygraph estimator class to use.
        """
        self.model = model
        self.estimator_name = estimator_name

        # 1. Base Calculator (Always needed)
        self.greedy_calculator = GreedyProbsCalculator(
            output_attentions=False,
            output_hidden_states=False,
        )
        
        # 2. Conditional Calculators
        if self.estimator_name in ENTROPY_METRICS:
            self.entropy_calculator = EntropyCalculator()
            
        if self.estimator_name in PMI_METRICS:
            # Use our custom vLLM calculator instead of the broken default one!
            self.pmi_calculator = VLLMGreedyLMProbsCalculator()

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
            if self.estimator_name in LOGPROB_METRICS:
                if "greedy_log_likelihoods" not in model_outputs:
                    if hasattr(self.model, "supports_logprobs") and self.model.supports_logprobs:
                        for alt_key in ["logprobs", "last_logprobs", "greedy_log_probs", "greedy_logprobs", "greedy_log_likelihoods"]:
                            if alt_key in model_outputs:
                                model_outputs["greedy_log_likelihoods"] = model_outputs[alt_key]
                                model_outputs["greedy_log_probs"] = model_outputs[alt_key] 
                                break
                
                if "greedy_log_likelihoods" not in model_outputs:
                    logger.warning(f"greedy_log_likelihoods missing for estimator '{self.estimator_name}'.")
                    return self._fallback_error("Missing greedy_log_likelihoods")

            # Step 3: Compute explicitly defined supplemental stats
            if self.estimator_name in ENTROPY_METRICS:
                entropy_results = self.entropy_calculator(model_outputs, texts=texts, model=self.model)
                model_outputs.update(entropy_results)
                
            if self.estimator_name in PMI_METRICS:
                pmi_results = self.pmi_calculator(model_outputs, texts=texts, model=self.model)
                model_outputs.update(pmi_results)

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