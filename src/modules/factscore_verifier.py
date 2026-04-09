import os
import multiprocessing
from typing import Dict, Any, List

from .abstract_components import PipelineComponent
from src.utils.metrics import MetricsRecorder
from src.data_models import Document, FactCheckSample

# Force vLLM to use spawn for multiprocessing workers
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"

class FactScoreVerifier(PipelineComponent):
    """Verifies atomic facts independently and aggregates a final label."""

    def __init__(self, llm_client, retriever, cfg, max_tokens=4096):
        self.llm_client = llm_client
        self.retriever = retriever  
        self.cfg = cfg
        self.max_tokens = max_tokens
        
        # Get Tokenizer directly from the backend
        _, self.tokenizer = self.llm_client.get_backend_objects()
        
        # 1. Dynamically resolve dataset labels based on Hydra config
        dataset_name = self.cfg.data.get("dataset_name", "").lower()
        self.is_scifact = "scifact" in dataset_name
        
        if self.is_scifact:
            self.label_true = "SUPPORT"
            self.label_false = "CONTRADICT"
            self.label_other = "NOT ENOUGH INFO"
        else:
            self.label_true = "True"
            self.label_false = "False"
            self.label_other = "Conflicting"

        # 2. FActScore faithful prompt structure injected with dynamic labels
        self.prompt_template = self.cfg.data.get("atomic_baseline_prompt", "")

    def process(self, sample: "FactCheckSample") -> "FactCheckSample":
        facts_to_verify = sample.atomic_facts if sample.atomic_facts else [sample.claim]
        fact_results = []
        
        # Accumulator for raw documents across all atomic facts
        all_accumulated_docs = [] 
        
        # Handle Gold Retriever Exception
        is_gold = type(self.retriever).__name__ == "GoldRetriever"
        if is_gold and not sample.retrieved_evidence:
            self.retriever.process(sample)
        
        # Fact-Level Retrieval & Verification Loop
        for atom in facts_to_verify:
            
            # Targeted micro-retrieval
            if is_gold:
                evidence_chunks = sample.retrieved_evidence
            else:
                evidence_chunks = self.retriever._retrieve(atom)
                MetricsRecorder.record_retrieval_call(sample)
                # Store the raw Document objects for the final JSONL output
                all_accumulated_docs.extend(evidence_chunks)

            # print(f"Verifying atomic fact: {atom}")
            # print(f"Evidence: {evidence_chunks}")   
            
            # Extract text using your specific Document model properties
            context_blocks = []
            for chunk in evidence_chunks:
                title = "Article"
                if hasattr(chunk, 'title') and chunk.title:
                    title = chunk.title
                text = chunk.content if hasattr(chunk, 'content') else str(chunk)
                context_blocks.append(f"Title: {title}\nText: {text}\n")
            
            context = "\n".join(context_blocks)
            
            # --- Enforce Context Token Limit ---
            if hasattr(self, 'tokenizer') and self.tokenizer:
                tokens = self.tokenizer.encode(context, add_special_tokens=False)
                if len(tokens) > self.max_tokens:
                    truncated_tokens = tokens[:self.max_tokens]
                    truncated_text = self.tokenizer.decode(truncated_tokens, skip_special_tokens=True)
                    
                    # Try to slice at the last sentence end
                    last_punctuation = max(truncated_text.rfind('.'), truncated_text.rfind('?'), truncated_text.rfind('!'))
                    if last_punctuation != -1:
                        context = truncated_text[:last_punctuation + 1]
                    else:
                        last_space = truncated_text.rfind(' ')
                        context = truncated_text[:last_space] if last_space != -1 else truncated_text
            else:
                char_limit = self.max_tokens * 4 
                if len(context) > char_limit:
                    truncated = context[:char_limit]
                    last_punctuation = max(truncated.rfind('.'), truncated.rfind('?'), truncated.rfind('!'))
                    
                    if last_punctuation != -1:
                        context = truncated[:last_punctuation + 1]
                    else:
                        last_space = truncated.rfind(' ')
                        context = truncated[:last_space] if last_space != -1 else truncated
            # -----------------------------------
            
            # Inject the context, atom, and the correct dataset labels
            prompt = self.prompt_template.format(
                context=context.strip(), 
                claim=atom,
            )
            
            generation_config = {
                "max_new_tokens": 256, 
            }
            
            response = self.llm_client.generate(prompt, generation_config)
            
            # Accumulate Metrics
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

            # print("="*50)
            # print(f"Verdict: {verdict}")
            # print("="*50)
            
        sample.atomic_verdicts = fact_results
        
        # Deduplicate accumulated documents and save to the main sample state
        if not is_gold and all_accumulated_docs:
            seen_ids = set()
            unique_docs = []
            for doc in all_accumulated_docs:
                if doc.source_id not in seen_ids:
                    seen_ids.add(doc.source_id)
                    unique_docs.append(doc)
            sample.retrieved_evidence = unique_docs
        
        # Aggregate final label using dynamic attributes
        final_label = self._aggregate_results(fact_results)

        # print("="*50)
        # print(f"Final VERDICT: {final_label}")
        # print("="*50)
        
        sample.predicted_verdict = final_label
        
        return sample

    def _parse_verdict_output(self, output: str) -> str:
        """Extracts the specific dynamic decision from the LLM."""
        output_upper = output.upper()
        
        # Check against the dynamic labels determined in __init__
        if self.label_false.upper() in output_upper:
            return self.label_false
        elif self.label_true.upper() in output_upper:
            return self.label_true
        else:
            return self.label_other

    def _aggregate_results(self, fact_results: list) -> str:
        """Translates atomic verdicts into a final discrete label."""
        verdicts = [res["verdict"] for res in fact_results]

        if len(verdicts) <= 1:
            return verdicts[0]
        else:
            support_count = verdicts.count(self.label_true)
            contradict_count = verdicts.count(self.label_false)
            
            # Strict Aggregation Rules based on dynamic labels
            if contradict_count > 0:
                label = self.label_false
            elif support_count == len(verdicts):
                label = self.label_true
            else:
                label = self.label_other
                
            return label