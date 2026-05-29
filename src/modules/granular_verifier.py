import os
import multiprocessing
import json
import re
from typing import Dict, Any, List

from .abstract_components import PipelineComponent
from src.utils.metrics import MetricsRecorder
from src.data_models import Document, FactCheckSample

os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"

class GranularVerifier(PipelineComponent):
    """Verifies atomic facts independently and aggregates a final label."""

    def __init__(self, llm_client, retriever, cfg, max_tokens=4096):
        self.llm_client = llm_client
        self.retriever = retriever  
        self.cfg = cfg
        self.max_tokens = max_tokens
        
        self.output_format = cfg.get("output_format", "label_only")
        
        _, self.tokenizer = self.llm_client.get_backend_objects()
        
        self.dataset_name = self.cfg.data.get("dataset_name", "").lower()
        self.is_scifact = "scifact" in self.dataset_name
        
        if self.is_scifact:
            self.label_true = "SUPPORT"
            self.label_false = "CONTRADICT"
            self.label_other = "NOT ENOUGH INFO"
        else:
            self.label_true = "True"
            self.label_false = "False"
            self.label_other = "Conflicting"

        if self.output_format == "label_only":
            self.prompt_template = self.cfg.prompts.get("rag_short", "")
        else:
            self.prompt_template = self.cfg.prompts.get("rag_long", "")

    def process(self, sample: "FactCheckSample") -> "FactCheckSample":
        facts_to_verify = sample.atomic_facts if sample.atomic_facts else [sample.claim]
        fact_results = []
        
        all_accumulated_docs = [] 
        
        is_gold = type(self.retriever).__name__ == "GoldRetriever"
        if is_gold and not sample.retrieved_evidence:
            self.retriever.process(sample)
        
        for atom in facts_to_verify:
            if is_gold:
                evidence_chunks = sample.retrieved_evidence
            else:
                evidence_chunks = self.retriever._retrieve(atom)
                MetricsRecorder.record_retrieval_call(sample)
                all_accumulated_docs.extend(evidence_chunks)
            
            grouped_evidence = {}
            for chunk in evidence_chunks:
                sid = getattr(chunk, 'source_id', "unknown")
                if sid not in grouped_evidence:
                    grouped_evidence[sid] = chunk.content
                else:
                    raw_content = chunk.content.split("Content: ", 1)[-1] if "Content: " in chunk.content else chunk.content
                    grouped_evidence[sid] += f"\n[...] {raw_content}"
            
            context_blocks = list(grouped_evidence.values())
            context = "\n\n---\n\n".join(context_blocks)
            
            prompt = self.prompt_template.format(
                context=context.strip() if context_blocks else "No relevant evidence found.", 
                claim=atom,
            ).replace("```json", "").strip()
            
            if self.output_format == "label_only":
                if not prompt.endswith("Verdict:"):
                    prompt += "\nVerdict:"
                max_tokens = 5
            else:
                prompt += "\n```json\n"
                max_tokens = self.cfg.llm.get("max_new_tokens", 256)

            generation_config = {
                "max_new_tokens": max_tokens, 
                "output_format": self.output_format,
                "dataset": self.dataset_name
            }
            
            response = self.llm_client.generate(prompt, generation_config)
            
            usage = response.get("usage", {})
            MetricsRecorder.record_token_usage(
                sample,
                input_tokens=usage.get("input_tokens", 0),
                output_tokens=usage.get("output_tokens", 0),
                step="generation"
            )
            MetricsRecorder.record_llm_call(sample)
            
            content = response.get("content", "")
            verdict = self._parse_verdict_output(content)
            fact_results.append({
                "atom": atom,
                "verdict": verdict,
                "raw_output": content,
                "evidence": context_blocks
            })
            
        sample.atomic_verdicts = fact_results
        
        if not is_gold and all_accumulated_docs:
            seen_ids = set()
            unique_docs = []
            for doc in all_accumulated_docs:
                cid = getattr(doc, 'chunk_id', doc.source_id)
                if cid not in seen_ids:
                    seen_ids.add(cid)
                    unique_docs.append(doc)
            sample.retrieved_evidence = unique_docs
        
        final_label = self._aggregate_results(fact_results)
        sample.predicted_verdict = final_label
        
        return sample

    def _parse_verdict_output(self, output: str) -> str:
        clean_text = output.strip().replace("```json", "").replace("```", "").strip()
        verdict_str = clean_text
        
        match = re.search(r'(\{.*\})', clean_text, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group(1))
                verdict_str = data.get("verdict", verdict_str)
            except json.JSONDecodeError:
                pass
        elif self.output_format == "full_response":
            verdict_match = re.search(r'"?verdict"?\s*:\s*"?([A-Za-z_]+)"?', clean_text, re.IGNORECASE)
            if verdict_match:
                verdict_str = verdict_match.group(1)

        output_upper = str(verdict_str).upper()
        
        if self.label_false.upper() in output_upper:
            return self.label_false
        elif self.label_true.upper() in output_upper:
            return self.label_true
        else:
            return self.label_other

    def _aggregate_results(self, fact_results: list) -> str:
        """Majority-vote aggregation with a 2/3 supermajority threshold."""
        verdicts = [res["verdict"] for res in fact_results]

        if not verdicts:
            return self.label_other

        if len(verdicts) <= 1 or len(set(verdicts)) == 1:
            return verdicts[0]

        filtered_verdicts = [v for v in verdicts if v != self.label_other]
        true_ratio = filtered_verdicts.count(self.label_true) / len(filtered_verdicts) if filtered_verdicts else 0

        if true_ratio >= 2/3:
            return self.label_true
        elif true_ratio < 1/3:
            return self.label_false
        else:
            return self.label_other