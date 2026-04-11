import logging
import json
import re

from lm_polygraph.model_adapters import WhiteboxModelvLLM
from vllm import SamplingParams
from src.utils.metrics import MetricsRecorder
from .abstract_components import PipelineComponent
from .uncertainty_aware_verifier import UQVerifier
from src.data_models import FactCheckSample


class UQDecomposePipeline(PipelineComponent):
    """
    Uncertainty-aware pipeline with atomic claim decomposition.
    
    Flow:
        1. Run full claim through UQ verifier for initial verdict + uncertainty score
        2. If confident (score < threshold) → return verdict directly
        3. If uncertain → decompose into atomic claims
        4. Verify each atomic claim with UQ verifier
        5. Atoms with high uncertainty → trigger per-atom RAG
        6. Aggregate all atomic verdicts into final label
    """

    def __init__(self, cfg, retriever, aggregator, rag_verifier, decomposer, model=None, tokenizer=None):
        self.cfg = cfg
        self.tokenizer = tokenizer

        # Initialize lm-polygraph using vLLM adapter
        if model and tokenizer:
            max_tokens = getattr(cfg.llm, "max_new_tokens", 1024)
            
            gen_params = SamplingParams(
                temperature=0.0,
                max_tokens=max_tokens,
                logprobs=5,
                stop=["<|im_end|>", "<|eot_id|>", "```", "<|im_start|>", "<|start_header_id|>"]
            )
            
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
        self.decomposer = decomposer

        # UQ Engine (Parametric)
        self.uq_engine = UQVerifier(
            model=self.whitebox_model,
            estimator_name=cfg.uncertainty.method
        )

        # Prompts and config
        self.dataset = cfg.data.dataset_name.lower()
        self.parametric_prompt = cfg.prompts.parametric
        self.threshold = cfg.uncertainty.threshold
        self.calibration_mode = cfg.uncertainty.get("calibration_mode", False)

        # Dataset-specific labels for aggregation
        if "scifact" in self.dataset:
            self.label_true = "SUPPORT"
            self.label_false = "CONTRADICT"
            self.label_other = "NOT ENOUGH INFO"
        else:
            self.label_true = "True"
            self.label_false = "False"
            self.label_other = "Conflicting"

        self.verdict_parser = {
            "scifact": self._parse_scifact,
            "quantemp": self._parse_quantemp
        }

    def process(self, sample: FactCheckSample) -> FactCheckSample:
        # ===== STEP 1: Whole-Claim UQ Pass =====
        raw_response, score, parametric_verdict, parametric_explanation = self._run_uq_pass(sample)

        sample.uncertainty_score = score
        sample.parametric_response = raw_response
        sample.parametric_verdict = parametric_verdict

        # ===== Calibration Mode: UQ-only, skip everything else =====
        if self.calibration_mode:
            sample.predicted_verdict = parametric_verdict
            sample.explanation = parametric_explanation
            sample.uq_flagged = False
            return sample

        # ===== STEP 2: Decision =====
        is_uncertain = score >= self.threshold

        if not is_uncertain:
            # [CONFIDENT] Return the parametric verdict directly
            sample.predicted_verdict = parametric_verdict
            sample.explanation = parametric_explanation
            sample.uq_flagged = False
            return sample

        # ===== STEP 3: Decompose into Atomic Claims =====
        sample.uq_flagged = True
        sample = self.decomposer.process(sample)

        # ===== STEP 4: Per-Atom UQ Verification =====
        atom_results = []

        # Optimization: if decomposition yielded only 1 atom (same as original claim),
        # skip per-atom UQ since we already know the claim is uncertain from Step 1.
        skip_atom_uq = len(sample.atomic_facts) == 1

        for atom in sample.atomic_facts:
            if skip_atom_uq:
                # Go directly to RAG — no point re-running UQ on the same claim
                atom_verdict, atom_explanation, evidence_blocks = self._rag_verify_atom(sample, atom)
                atom_results.append({
                    "atom": atom,
                    "verdict": atom_verdict,
                    "raw_output": atom_explanation,
                    "uncertainty_score": score,  # reuse whole-claim score
                    "rag_triggered": True,
                    "evidence": evidence_blocks
                })
                continue

            atom_verdict, atom_explanation, atom_score = self._verify_atom(sample, atom)

            atom_uncertain = atom_score >= self.threshold

            if atom_uncertain:
                # ===== STEP 5: Per-Atom RAG (only for uncertain atoms) =====
                atom_verdict, atom_explanation, evidence_blocks = self._rag_verify_atom(sample, atom)
                atom_results.append({
                    "atom": atom,
                    "verdict": atom_verdict,
                    "raw_output": atom_explanation,
                    "uncertainty_score": atom_score,
                    "rag_triggered": True,
                    "evidence": evidence_blocks
                })
            else:
                atom_results.append({
                    "atom": atom,
                    "verdict": atom_verdict,
                    "raw_output": atom_explanation,
                    "uncertainty_score": atom_score,
                    "rag_triggered": False,
                    "evidence": []
                })

        # ===== STEP 6: Aggregate =====
        sample.atomic_verdicts = atom_results
        final_label = self._aggregate_results(atom_results)
        sample.predicted_verdict = final_label
        sample.explanation = f"Aggregated from {len(atom_results)} atomic verdicts."

        return sample

    # -------------------------------------------------------------------------
    # Internal Helpers
    # -------------------------------------------------------------------------

    def _run_uq_pass(self, sample: FactCheckSample):
        """Runs the whole-claim through UQ verifier and parses the response."""
        clean_prompt = self.parametric_prompt.format(claim=sample.claim).replace("```json", "").strip()
        messages = [{"role": "user", "content": clean_prompt}]
        full_prompt = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        full_prompt += "```json\n"

        raw_response, score = self.uq_engine.estimate(full_prompt)

        # Strip prompt echo from response
        clean_response = raw_response
        if full_prompt in raw_response:
            clean_response = raw_response.replace(full_prompt, "", 1).strip()
        elif raw_response.startswith(full_prompt.strip()):
            clean_response = raw_response[len(full_prompt.strip()):].strip()

        if self.tokenizer:
            prompt_tokens = len(self.tokenizer.encode(full_prompt))
            response_tokens = len(self.tokenizer.encode(clean_response)) if clean_response else 0
            MetricsRecorder.record_token_usage(
                sample,
                input_tokens=prompt_tokens,
                output_tokens=response_tokens,
                step="uq"
            )
            MetricsRecorder.record_llm_call(sample)

        # Parse the response
        final_clean = clean_response.strip().replace("```json", "").replace("```", "").strip()

        json_target = final_clean
        json_match = re.search(r'(\{.*?\})', final_clean, re.DOTALL)
        if json_match:
            json_target = json_match.group(1)

        verdict = self._parse_verdict(json_target)

        try:
            parsed_json = json.loads(json_target)
            explanation = parsed_json.get("explanation", "No explanation could be extracted from the model response.")
            if "verdict" in parsed_json:
                verdict = self._parse_verdict(parsed_json["verdict"])
        except json.JSONDecodeError:
            explanation = f"Failed to parse explanation. Raw output: {final_clean}"

        return final_clean, score, verdict, explanation

    def _verify_atom(self, sample: FactCheckSample, atom: str):
        """Runs a single atomic claim through the UQ verifier (parametric only)."""
        clean_prompt = self.parametric_prompt.format(claim=atom).replace("```json", "").strip()
        messages = [{"role": "user", "content": clean_prompt}]
        full_prompt = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        full_prompt += "```json\n"

        raw_response, score = self.uq_engine.estimate(full_prompt)

        # Strip prompt echo
        clean_response = raw_response
        if full_prompt in raw_response:
            clean_response = raw_response.replace(full_prompt, "", 1).strip()
        elif raw_response.startswith(full_prompt.strip()):
            clean_response = raw_response[len(full_prompt.strip()):].strip()

        if self.tokenizer:
            prompt_tokens = len(self.tokenizer.encode(full_prompt))
            response_tokens = len(self.tokenizer.encode(clean_response)) if clean_response else 0
            MetricsRecorder.record_token_usage(
                sample,
                input_tokens=prompt_tokens,
                output_tokens=response_tokens,
                step="uq"
            )
            MetricsRecorder.record_llm_call(sample)

        # Parse
        final_clean = clean_response.strip().replace("```json", "").replace("```", "").strip()
        json_target = final_clean
        json_match = re.search(r'(\{.*?\})', final_clean, re.DOTALL)
        if json_match:
            json_target = json_match.group(1)

        verdict = self._parse_verdict(json_target)

        try:
            parsed_json = json.loads(json_target)
            explanation = parsed_json.get("explanation", "No explanation extracted.")
            if "verdict" in parsed_json:
                verdict = self._parse_verdict(parsed_json["verdict"])
        except json.JSONDecodeError:
            explanation = f"Failed to parse. Raw: {final_clean}"

        return verdict, explanation, score

    def _rag_verify_atom(self, sample: FactCheckSample, atom: str):
        """Retrieves evidence and re-verifies a single uncertain atom via RAG."""
        # Determine retriever type
        is_gold = type(self.retriever).__name__ == "GoldRetriever"

        if is_gold:
            # Gold retriever uses the full sample's evidence
            if not sample.retrieved_evidence:
                self.retriever.process(sample)
            evidence_chunks = sample.retrieved_evidence
        else:
            # Vector retriever: targeted micro-retrieval for this atom
            evidence_chunks = self.retriever._retrieve(atom)
            MetricsRecorder.record_retrieval_call(sample)

        # 1. Build a temporary sample to feed into the aggregator
        temp_sample = FactCheckSample(
            id=sample.id,
            claim=atom,
            mode="uq_decompose"
        )
        temp_sample.retrieved_evidence = evidence_chunks

        # 2. Let the EvidenceAggregator handle the smart merging & formatting!
        temp_sample = self.aggregator.process(temp_sample)
        
        # Track the raw blocks for logging/evaluation purposes
        evidence_blocks = [chunk.content for chunk in evidence_chunks]

        # 3. Run the RAG verifier on the perfectly formatted sample
        temp_sample = self.rag_verifier.process(temp_sample)

        # 4. Record metrics on the REAL sample
        MetricsRecorder.record_token_usage(
            sample,
            input_tokens=temp_sample.metrics.gen_input_tokens,
            output_tokens=temp_sample.metrics.gen_output_tokens,
            step="generation"
        )
        MetricsRecorder.record_llm_call(sample)

        return temp_sample.predicted_verdict, temp_sample.explanation, evidence_blocks

    # -------------------------------------------------------------------------
    # Verdict Parsing & Aggregation (shared with existing modules)
    # -------------------------------------------------------------------------

    def _parse_verdict(self, text):
        strategy = self.verdict_parser.get(self.dataset)
        if strategy:
            return strategy(text)
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

    def _aggregate_results(self, fact_results: list) -> str:
        """Translates atomic verdicts into a final discrete label (FActScore-style)."""
        verdicts = [res["verdict"] for res in fact_results]

        if len(verdicts) <= 1:
            return verdicts[0] if verdicts else self.label_other

        support_count = verdicts.count(self.label_true)
        contradict_count = verdicts.count(self.label_false)

        if contradict_count > 0:
            return self.label_false
        elif support_count == len(verdicts):
            return self.label_true
        else:
            return self.label_other
