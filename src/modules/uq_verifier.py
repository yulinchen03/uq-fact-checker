from abc import ABC, abstractmethod
import logging
import numpy as np
import lm_polygraph.estimators as estimators
from lm_polygraph.estimators import Estimator
from lm_polygraph.stat_calculators.greedy_probs import GreedyProbsCalculator
from lm_polygraph.stat_calculators.entropy import EntropyCalculator
from lm_polygraph.stat_calculators.stat_calculator import StatCalculator
from lm_polygraph.stat_calculators.sample import SamplingGenerationCalculator
from lm_polygraph.stat_calculators.cross_encoder_similarity import CrossEncoderSimilarityMatrixCalculator
from lm_polygraph.stat_calculators.semantic_matrix import SemanticMatrixCalculator
from lm_polygraph.stat_calculators.semantic_classes import SemanticClassesCalculator
from lm_polygraph.utils.deberta import Deberta
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
    "MeanConditionalPointwiseMutualInformation",
    "RenyiNeg"
]

# Estimators that require a pre-computed entropy stat
ENTROPY_METRICS = [
    "MeanTokenEntropy",
    "MeanConditionalPointwiseMutualInformation"
]

# Estimators that require unconditioned LM probabilities P(x)
PMI_METRICS = [
    "MeanPointwiseMutualInformation",
    "MeanConditionalPointwiseMutualInformation"
]


class VLLMGreedyLMProbsCalculator(StatCalculator):
    """Computes unconditioned LM log-likelihoods via vLLM prompt_logprobs for PMI/CPMI."""

    @staticmethod
    def meta_info():
        return (["greedy_lm_log_likelihoods"], ["greedy_tokens"])

    def __init__(self):
        super().__init__()

    def __call__(self, dependencies, texts, model, max_new_tokens=100, **kwargs):
        llm = model.model
        tokenizer = llm.get_tokenizer()
        greedy_tokens = dependencies.get("greedy_tokens", [])

        if not greedy_tokens or not greedy_tokens[0]:
            return {"greedy_lm_log_likelihoods": [[0.0]]}

        sampling_params = SamplingParams(
            prompt_logprobs=1,
            max_tokens=1,
            temperature=0.5
        )

        bos_id = tokenizer.bos_token_id if tokenizer.bos_token_id is not None else tokenizer.eos_token_id
        vllm_inputs = [{"prompt_token_ids": [bos_id] + tokens} for tokens in greedy_tokens]

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
                target_logprob_dict = p_logprobs[j + 1]

                if p_logprobs[j] is None:
                    seq_logprobs.append(0.0)
                else:
                    if token_id in target_logprob_dict:
                        val = target_logprob_dict[token_id]
                        logp = val.logprob if hasattr(val, "logprob") else val
                        seq_logprobs.append(logp)
                    else:
                        seq_logprobs.append(-100.0)

            lm_log_likelihoods.append(seq_logprobs)

        return {"greedy_lm_log_likelihoods": lm_log_likelihoods}


class UQEstimator(ABC):
    @abstractmethod
    def estimate(self, full_prompt: str):
        pass


class UQVerifier(UQEstimator):
    def __init__(self, model, estimator_name):
        self.model = model

        if isinstance(estimator_name, list):
            self.estimator_names = estimator_name
            self.multi_mode = True
        else:
            self.estimator_names = [estimator_name]
            self.multi_mode = False

        self.greedy_calculator = GreedyProbsCalculator(
            output_attentions=False,
            output_hidden_states=False,
        )

        if any(name in ENTROPY_METRICS for name in self.estimator_names):
            self.entropy_calculator = EntropyCalculator()
        if any(name in PMI_METRICS for name in self.estimator_names):
            self.pmi_calculator = VLLMGreedyLMProbsCalculator()

        self.requires_nli = any(name in ["SemanticEntropy"] for name in self.estimator_names)
        self.requires_semantic = any(name in ["SemanticEntropy"] for name in self.estimator_names)

        if self.requires_nli:
            logger.info("Initializing Deberta NLI model for UQ Estimation...")
            device_str = self.model.device() if callable(getattr(self.model, 'device', None)) else 'cuda'
            self.nli_model = Deberta(device=device_str, batch_size=20)
            self.nli_model.setup()

        if self.requires_semantic:
            self.calc_samples = SamplingGenerationCalculator(samples_n=10)
            self.calc_cross_encoder = CrossEncoderSimilarityMatrixCalculator()
            self.calc_semantic_matrix = SemanticMatrixCalculator(nli_model=self.nli_model)
            self.calc_semantic_classes = SemanticClassesCalculator()

        self.estimators = []
        self.lm_polygraph_estimators = []

        for name in self.estimator_names:
            if name == "LogicalContradiction":
                continue

            self.lm_polygraph_estimators.append(name)
            try:
                estimator_class = getattr(estimators, name)
                if name == "SemanticEntropy":
                    self.estimators.append(estimator_class(class_probability_estimation="frequency"))
                else:
                    self.estimators.append(estimator_class())
                logger.info(f"Loaded UQ estimator: {name}")
            except AttributeError:
                available = [e for e in dir(estimators) if not e.startswith("__")]
                logger.error(f"Estimator '{name}' not found. Available estimators: {available}")
                raise

    def estimate(self, prompt: str):
        texts = [prompt]
        model_outputs = {"input_texts": texts}

        try:
            greedy_prob_results = self.greedy_calculator(model_outputs, texts=texts, model=self.model)
            model_outputs.update(greedy_prob_results)

            if getattr(self, "requires_semantic", False):
                model_outputs.update(self.calc_samples(model_outputs, texts=texts, model=self.model))
                model_outputs.update(self.calc_cross_encoder(model_outputs, texts=texts, model=self.model))
                model_outputs.update(self.calc_semantic_matrix(model_outputs, texts=texts, model=self.model))
                model_outputs.update(self.calc_semantic_classes(model_outputs, texts=texts, model=self.model))

            if any(name in LOGPROB_METRICS for name in self.estimator_names):
                if "greedy_log_likelihoods" not in model_outputs:
                    if hasattr(self.model, "supports_logprobs") and self.model.supports_logprobs:
                        for alt_key in ["logprobs", "last_logprobs", "greedy_log_probs", "greedy_logprobs", "greedy_log_likelihoods"]:
                            if alt_key in model_outputs:
                                model_outputs["greedy_log_likelihoods"] = model_outputs[alt_key]
                                model_outputs["greedy_log_probs"] = model_outputs[alt_key]
                                break
                    if "greedy_log_likelihoods" not in model_outputs:
                        return self._fallback_error("Missing greedy_log_likelihoods")

            if any(name in ENTROPY_METRICS for name in self.estimator_names):
                entropy_results = self.entropy_calculator(model_outputs, texts=texts, model=self.model)
                model_outputs.update(entropy_results)
            if any(name in PMI_METRICS for name in self.estimator_names):
                pmi_results = self.pmi_calculator(model_outputs, texts=texts, model=self.model)
                model_outputs.update(pmi_results)

            scores_dict = {}
            for name, estimator in zip(self.lm_polygraph_estimators, self.estimators):
                scores = estimator(model_outputs)

                val = float(scores[0] if isinstance(scores, (list, np.ndarray)) else scores)
                # Apply the true Perplexity conversion: exp(mean negative log-likelihood)
                if name == "Perplexity":
                    val = np.exp(val)
                scores_dict[name] = val

            if model_outputs.get("greedy_texts"):
                generated_text = model_outputs["greedy_texts"][0]
            else:
                tokenizer = self.model.model.get_tokenizer()
                token_ids = model_outputs.get("greedy_tokens", [[]])[0]
                generated_text = tokenizer.decode(token_ids, skip_special_tokens=True)

            if self.multi_mode:
                return generated_text.strip(), scores_dict
            else:
                fallback_name = self.lm_polygraph_estimators[0] if self.lm_polygraph_estimators else self.estimator_names[0]
                return generated_text.strip(), scores_dict.get(fallback_name, 0.0)

        except Exception as e:
            logger.error(f"UQ estimation failed: {e}", exc_info=True)
            return self._fallback_error(str(e))

    def _fallback_error(self, err_msg: str):
        fallback_json = f'{{"verdict": "NOT ENOUGH INFO", "explanation": "UQ Error: {err_msg}"}}'
        if self.multi_mode:
            return fallback_json, {name: float("inf") for name in self.lm_polygraph_estimators}
        else:
            return fallback_json, float("inf")



    def verify_claim(self, claim: str, prompt_template: str, dataset_name: str,
                     output_format: str, primary_estimator: str = None, ensemble_bundle: dict = None):
        """
        Universal verification method: formats prompt, generates with UQ, parses verdict.

        Returns:
            (response, uq_scores_dict, verdict, explanation, prompt_tokens, response_tokens, llm_calls)
        """
        import re, json

        llm_calls = 1

        clean_prompt = prompt_template.format(claim=claim).replace("```json", "").strip()
        tokenizer = self.model.model.get_tokenizer()
        messages = [{"role": "user", "content": clean_prompt}]
        try:
            full_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        except ValueError:
            full_prompt = clean_prompt

        if output_format == "label_only":
            if not full_prompt.endswith("Verdict:"):
                full_prompt += "\nVerdict:"
        else:
            full_prompt += "\n```json\n{"

        raw_response, uq_scores = self.estimate(full_prompt)

        if not isinstance(uq_scores, dict):
            uq_scores = {self.estimator_names[0]: uq_scores}

        clean_response = raw_response
        if full_prompt in raw_response:
            clean_response = raw_response.replace(full_prompt, "", 1).strip()
        elif raw_response.startswith(full_prompt.strip()):
            clean_response = raw_response[len(full_prompt.strip()):].strip()

        prompt_tokens = len(tokenizer.encode(full_prompt))
        response_tokens = len(tokenizer.encode(clean_response)) if clean_response else 0

        if output_format == "full_response":
            final_clean = "{" + clean_response.strip().replace("```json", "").replace("```", "").strip()
        else:
            final_clean = clean_response.strip().replace("```json", "").replace("```", "").strip()

        verdict_str = final_clean
        explanation = "Label only generation." if output_format == "label_only" else "Parsing failed."

        json_match = re.search(r'(\{.*?\})', final_clean, re.DOTALL)
        if json_match:
            try:
                data = json.loads(json_match.group(1))
                verdict_str = data.get("verdict", verdict_str)
                explanation = data.get("explanation", explanation)
            except json.JSONDecodeError:
                pass
        elif output_format == "full_response":
            v_match = re.search(r'"?verdict"?\s*:\s*"?([A-Za-z_]+)"?', final_clean, re.IGNORECASE)
            if v_match:
                verdict_str = v_match.group(1)
            e_match = re.search(r'"?explanation"?\s*:\s*"?(.+?)(?:"\s*\}|"$)', final_clean, re.IGNORECASE | re.DOTALL)
            if e_match:
                explanation = e_match.group(1).strip()

        t = str(verdict_str).upper()
        if "scifact" in dataset_name.lower():
            if "SUPPORT" in t:
                verdict = "SUPPORT"
            elif "CONTRADICT" in t or "REFUTE" in t:
                verdict = "CONTRADICT"
            else:
                verdict = "NOT ENOUGH INFO"
        else:
            if "FALSE" in t:
                verdict = "False"
            elif "TRUE" in t:
                verdict = "True"
            else:
                verdict = "Conflicting"

        is_primary = (primary_estimator == "LogicalContradiction")
        is_ensemble_feature = (primary_estimator == "Ensemble" and ensemble_bundle and "LogicalContradiction" in ensemble_bundle.get("features", []))

        if is_primary or is_ensemble_feature:
            from src.modules.ace import AdversarialConsistencyEvaluator
            ace_evaluator = AdversarialConsistencyEvaluator(self.model)
            logic_score, extra_p, extra_r, extra_calls = ace_evaluator.check_logical_contradiction(
                uq_verifier=self,
                claim=claim,
                original_verdict=verdict,
                original_uq_scores=uq_scores,
                parametric_prompt=prompt_template,
                dataset_name=dataset_name,
                eval_method="discrete", 
                output_format=output_format
            )
            uq_scores["LogicalContradiction"] = logic_score
            prompt_tokens += extra_p
            response_tokens += extra_r
            llm_calls += extra_calls

        if primary_estimator == "Ensemble" and ensemble_bundle: 
            features_list = ensemble_bundle.get("features", []) 
            
            feat = []
            max_finite_replacements = ensemble_bundle["max_finite_replacements"]
            for method in features_list:
                val = uq_scores.get(method)
                
                if val is None or np.isnan(val) or np.isinf(val):
                    feat.append(max_finite_replacements.get(method, 0.0))
                else:
                    feat.append(float(val))
            
            X = np.array([feat])
            X_scaled = ensemble_bundle["scaler"].transform(X)
            prob = ensemble_bundle["model"].predict_proba(X_scaled)[0, 1]
            uq_scores["Ensemble"] = float(prob)

        return final_clean, uq_scores, verdict, explanation, prompt_tokens, response_tokens, llm_calls