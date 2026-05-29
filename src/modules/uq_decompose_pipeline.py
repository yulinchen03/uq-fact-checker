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

class UQDecomposePipeline(PipelineComponent):
    def __init__(self, cfg, retriever, aggregator, rag_verifier, decomposer, model=None, tokenizer=None):
        self.cfg = cfg
        self.tokenizer = tokenizer
        self.model_name = cfg.llm.model_name
        self.output_format = cfg.get("output_format", "label_only")
        self.dataset = cfg.data.dataset_name.lower()

        if model and tokenizer:
            GEN_TEMPERATURE = 0.5 if cfg.uncertainty.method == "SemanticEntropy" else 0.0
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
        self.decomposer = decomposer

        self.primary_estimator = cfg.uncertainty.method
        self.threshold = cfg.uncertainty.threshold

        project_root = Path(__file__).resolve().parents[2]
        model_name = getattr(cfg.llm, "model_name", "").split("/")[-1]
        calib_split = cfg.data.get("calibrated_split", "val")

        check_logic = cfg.get("check_logic", False)
        logic_method = cfg.get("logic_eval_method", "")
        logic_suffix = f"_logic_{logic_method}" if check_logic and logic_method else ""

        model_bundle_filename = f"ensemble_model_bundle_{calib_split}_{self.output_format}{logic_suffix}.pkl"
        model_bundle_path = project_root / "run_results" / cfg.data.dataset_name / model_name / "calibration" / model_bundle_filename
        
        self.ensemble_bundle = None
        if model_bundle_path.exists():
            with open(model_bundle_path, "rb") as f:
                self.ensemble_bundle = pickle.load(f)

        if self.primary_estimator == "Ensemble":
            if not self.ensemble_bundle:
                raise ValueError(f"Ensemble selected but bundle not found at {model_bundle_path}")
            estimators = self.ensemble_bundle["features"]
            print(f"⚙️ Ensemble Active: Loading required features {estimators}")
        else:
            estimators = [self.primary_estimator]
            print(f"⚙️ Single Metric Active: Loading {estimators}")

        self.uq_engine = UQVerifier(model=self.whitebox_model, estimator_name=estimators)

        if "scifact" in self.dataset:
            self.label_true = "SUPPORT"
            self.label_false = "CONTRADICT"
            self.label_other = "NOT ENOUGH INFO"
        else:
            self.label_true = "True"
            self.label_false = "False"
            self.label_other = "Conflicting"

    def process(self, sample: FactCheckSample) -> FactCheckSample:
        prompt_template = self.cfg.prompts.parametric_short if self.output_format == "label_only" else self.cfg.prompts.parametric_long
            
        raw_response, uq_scores_dict, parametric_verdict, parametric_explanation, p_tokens, r_tokens, llm_calls = self.uq_engine.verify_claim(
            claim=sample.claim,
            prompt_template=prompt_template,
            dataset_name=self.dataset,
            output_format=self.output_format,
            primary_estimator=self.primary_estimator,
            ensemble_bundle=self.ensemble_bundle
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

        sample.uq_flagged = True
        sample = self.decomposer.process(sample)

        atom_results = []
        skip_atom_uq = len(sample.atomic_facts) == 1

        for atom in sample.atomic_facts:
            if skip_atom_uq:
                atom_verdict, atom_explanation, evidence_blocks = self._rag_verify_atom(sample, atom)
                atom_results.append({
                    "atom": atom, "verdict": atom_verdict, "raw_output": atom_explanation,
                    "uncertainty_score": float(score) if score is not None else None,
                    "uq_scores": uq_scores_dict, "rag_triggered": True, "evidence": evidence_blocks
                })
                continue

            atom_verdict, atom_explanation, atom_uq_scores = self._verify_atom(sample, atom, prompt_template)
            atom_score = atom_uq_scores.get(self.primary_estimator, float('inf'))
            atom_uncertain = atom_score >= self.threshold

            if atom_uncertain:
                atom_verdict, atom_explanation, evidence_blocks = self._rag_verify_atom(sample, atom)
                atom_results.append({
                    "atom": atom, "verdict": atom_verdict, "raw_output": atom_explanation,
                    "uncertainty_score": float(atom_score) if atom_score is not None else None,
                    "uq_scores": atom_uq_scores, "rag_triggered": True, "evidence": evidence_blocks
                })
            else:
                atom_results.append({
                    "atom": atom, "verdict": atom_verdict, "raw_output": atom_explanation,
                    "uncertainty_score": float(atom_score) if atom_score is not None else None,
                    "uq_scores": atom_uq_scores, "rag_triggered": False, "evidence": []
                })

        sample.atomic_verdicts = atom_results
        sample.predicted_verdict = self._aggregate_results(atom_results)
        sample.explanation = f"Aggregated from {len(atom_results)} atomic verdicts."

        return sample

    def _verify_atom(self, sample: FactCheckSample, atom: str, prompt_template: str):
        """Runs a single atomic claim through the UQ verifier."""
        raw_resp, atom_uq_scores, verdict, explanation, p_tokens, r_tokens, llm_calls = self.uq_engine.verify_claim(
            claim=atom,
            prompt_template=prompt_template,
            dataset_name=self.dataset,
            output_format=self.output_format,
            primary_estimator=self.primary_estimator,
            ensemble_bundle=self.ensemble_bundle
        )

        MetricsRecorder.record_token_usage(sample, input_tokens=p_tokens, output_tokens=r_tokens, step="uq")
        MetricsRecorder.record_llm_call(sample, count=llm_calls)

        return verdict, explanation, atom_uq_scores

    def _rag_verify_atom(self, sample: FactCheckSample, atom: str):
        is_gold = type(self.retriever).__name__ == "GoldRetriever"

        if is_gold:
            if not sample.retrieved_evidence:
                self.retriever.process(sample)
            evidence_chunks = sample.retrieved_evidence
        else:
            evidence_chunks = self.retriever._retrieve(atom)
            MetricsRecorder.record_retrieval_call(sample)

        temp_sample = FactCheckSample(
            id=sample.id,
            claim=atom,
            mode="uq_decompose"
        )
        temp_sample.retrieved_evidence = evidence_chunks

        temp_sample = self.aggregator.process(temp_sample)
        evidence_blocks = [chunk.content for chunk in evidence_chunks]

        temp_sample = self.rag_verifier.process(temp_sample)

        MetricsRecorder.record_token_usage(
            sample,
            input_tokens=temp_sample.metrics.gen_input_tokens,
            output_tokens=temp_sample.metrics.gen_output_tokens,
            step="generation"
        )
        MetricsRecorder.record_llm_call(sample)

        return temp_sample.predicted_verdict, temp_sample.explanation, evidence_blocks

    def _aggregate_results(self, fact_results: list) -> str:
        """Majority-vote aggregation with 2/3 supermajority threshold."""
        verdicts = [res["verdict"] for res in fact_results]

        if not verdicts:
            return self.label_other

        if len(verdicts) <= 1 or len(set(verdicts)) == 1:
            return verdicts[0]

        neutral_count = verdicts.count(self.label_other)
        true_count = verdicts.count(self.label_true)
        false_count = verdicts.count(self.label_false)
        
        if neutral_count >= (true_count + false_count):
            return self.label_other

        filtered_verdicts = [v for v in verdicts if v != self.label_other]

        true_ratio = true_count / len(filtered_verdicts)

        if true_ratio >= 2/3:
            return self.label_true
        elif true_ratio < 1/3:
            return self.label_false
        else:
            return self.label_other