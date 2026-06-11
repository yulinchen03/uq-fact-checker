import logging
import pickle
from pathlib import Path

from lm_polygraph.model_adapters import WhiteboxModelvLLM
from lm_polygraph.utils.generation_parameters import GenerationParameters
from vllm import SamplingParams
from vllm.sampling_params import StructuredOutputsParams
from src.utils.metrics import MetricsRecorder
from .abstract_components import PipelineComponent
from .uq_verifier import UQVerifier
from src.data_models import FactCheckSample
from transformers import AutoTokenizer

class UncertaintyAwarePipeline(PipelineComponent):
    def __init__(self, cfg, retriever, aggregator, rag_verifier, model=None, tokenizer=None):
        self.cfg = cfg
        self.tokenizer = tokenizer
        self.model_name = cfg.llm.model_name
        
        self.output_format = cfg.get("output_format", "label_only")
        self.dataset = cfg.data.dataset_name.lower()

        if model and tokenizer:
            GEN_TEMPERATURE = 0.3
            GEN_STOP_TOKENS = ["<|im_end|>", "<|eot_id|>", "```", "<|im_start|>", "<|start_header_id|>"]

            if self.output_format == "label_only":
                allowed_labels = ["True", "False", "Conflicting"] if "quantemp" in self.dataset else ["SUPPORT", "CONTRADICT", "NOT ENOUGH INFO"]
                gen_params = SamplingParams(
                    temperature=GEN_TEMPERATURE,
                    max_tokens=5,
                    logprobs=10,
                    stop=GEN_STOP_TOKENS,
                    structured_outputs=StructuredOutputsParams(choice=allowed_labels)
                )
            else:
                max_tokens = getattr(cfg.llm, "max_new_tokens", 256)
                gen_params = SamplingParams(
                    temperature=GEN_TEMPERATURE,
                    max_tokens=max_tokens,
                    logprobs=10,
                    stop=GEN_STOP_TOKENS
                )

            if getattr(self.tokenizer, "eos_token", None) is None and getattr(self.tokenizer, "eos_token_id", None) is not None:
                self.tokenizer.eos_token = self.tokenizer.decode(self.tokenizer.eos_token_id)
            
            # GenerationParameters must mirror SamplingParams because WhiteboxModelvLLM.__init__
            # overwrites sampling_params fields (temperature, top_k, top_p, stop) with these values.
            gen_parameters = GenerationParameters(
                temperature=GEN_TEMPERATURE,
                stop_strings=GEN_STOP_TOKENS,
            )
            self.whitebox_model = WhiteboxModelvLLM(model, sampling_params=gen_params, generation_parameters=gen_parameters)
            self.whitebox_model.supports_logprobs = True

            # Mistral does not support vLLM's tokenizer — force-load HuggingFace tokenizer
            if "Mistral" in tokenizer.__class__.__name__:
                hf_tokenizer = AutoTokenizer.from_pretrained(self.model_name)
                if getattr(hf_tokenizer, "pad_token", None) is None:
                    if getattr(hf_tokenizer, "eos_token", None):
                        hf_tokenizer.pad_token = hf_tokenizer.eos_token
                    else:
                        hf_tokenizer.pad_token = hf_tokenizer.decode(hf_tokenizer.eos_token_id)
                self.whitebox_model.tokenizer = hf_tokenizer
        
        self.retriever = retriever
        self.aggregator = aggregator
        self.rag_verifier = rag_verifier
        
        self.primary_estimator = cfg.uncertainty.method
        self.threshold = cfg.uncertainty.threshold

        project_root = Path(__file__).resolve().parents[2]
        model_name = getattr(cfg.llm, "model_name", "").split("/")[-1]
        calib_split = cfg.data.get("calibrated_split", "val")

        check_logic = cfg.get("check_logic", False)
        logic_method = cfg.get("logic_eval_method", "")
        logic_suffix = f"_logic_{logic_method}" if check_logic and logic_method else "_logic_OFF"

        model_bundle_filename = f"ensemble_model_bundle_{calib_split}_{self.output_format}{logic_suffix}.pkl"
        seed = cfg.get("seed", 42)
        model_bundle_path = project_root / "run_results" / f"seed_{seed}" / cfg.data.dataset_name / model_name / "calibration" / model_bundle_filename
        
        self.ensemble_model_bundle = None
        if model_bundle_path.exists():
            with open(model_bundle_path, "rb") as f:
                self.ensemble_model_bundle = pickle.load(f)

        if self.primary_estimator == "Ensemble":
            if not self.ensemble_model_bundle:
                raise ValueError(f"Ensemble selected but bundle not found at {model_bundle_path}")
            estimators = self.ensemble_model_bundle["features"]
            print(f"⚙️ Ensemble Active: Loading required features {estimators}")
        else:
            estimators = [self.primary_estimator]
            print(f"⚙️ Single Metric Active: Loading {estimators}")

        self.uq_engine = UQVerifier(model=self.whitebox_model, estimator_name=estimators)

    def process(self, sample: FactCheckSample) -> FactCheckSample:
        prompt_template = self.cfg.prompts.parametric_short if self.output_format == "label_only" else self.cfg.prompts.parametric_long
            
        raw_response, uq_scores_dict, parametric_verdict, parametric_explanation, p_tokens, r_tokens, llm_calls = self.uq_engine.verify_claim(
            claim=sample.claim,
            prompt_template=prompt_template,
            dataset_name=self.dataset,
            output_format=self.output_format,
            primary_estimator=self.primary_estimator,
            ensemble_bundle=self.ensemble_model_bundle
        )

        MetricsRecorder.record_token_usage(sample, input_tokens=p_tokens, output_tokens=r_tokens, step="uq")
        MetricsRecorder.record_llm_call(sample, count=llm_calls)

        score = uq_scores_dict.get(self.primary_estimator, float('inf'))

        sample.uq_scores = uq_scores_dict
        sample.uncertainty_score = float(score) if score is not None else None
        sample.parametric_response = raw_response
        sample.parametric_verdict = parametric_verdict

        is_uncertain = score >= self.threshold

        if not is_uncertain:
            sample.predicted_verdict = parametric_verdict
            sample.explanation = parametric_explanation
            sample.uq_flagged = False
            return sample

        print("Action: Uncertain -> Triggering RAG")
        sample.uq_flagged = True
        
        sample = self.retriever.process(sample)
        sample = self.aggregator.process(sample)
        sample = self.rag_verifier.process(sample)

        return sample