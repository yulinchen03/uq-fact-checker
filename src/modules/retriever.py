import os
import pickle
import chromadb
import torch
import numpy as np
import logging
from typing import List, Tuple, Dict, Optional
from collections import defaultdict
from sentence_transformers import SentenceTransformer

from src.data_models import Document
from src.modules.abstract_components import PipelineComponent
from src.utils.metrics import MetricsRecorder
from src.utils.sparse_encoder import SpladeEncoder

from transformers import AutoTokenizer, is_torch_npu_available, AutoModelForMaskedLM
from vllm import LLM, SamplingParams
from vllm.distributed.parallel_state import destroy_model_parallel
import gc

logger = logging.getLogger(__name__)

def get_model_alias(model_name: str) -> str:
    """Maps long HuggingFace repo IDs to clean, short aliases for file paths."""
    if not model_name: return "none"
    aliases = {
        "BAAI/bge-m3": "bge_m3",
        "Qwen/Qwen3-Embedding-0.6B": "qwen_06b",
        "Qwen/Qwen3-Embedding-4B": "qwen_4b",
        "Qwen/Qwen3-Embedding-8B": "qwen_8b",
        "naver/splade-cocondenser-ensembledistil": "splade",
    }
    if model_name in aliases: return aliases[model_name]
    return model_name.split("/")[-1].replace("-", "").replace(".", "").lower()[:12]

class BaseRetriever(PipelineComponent):
    """Abstract base class for retrievers."""
    def _retrieve(self, query: str) -> List[Document]:
        raise NotImplementedError


class DenseRetriever(BaseRetriever):
    """Retriever using standard dense vector databases (ChromaDB)."""
    def __init__(self, dataset_name: str, db_path: str, dense_model: str, sparse_model: str = "naver/splade-cocondenser-ensembledistil", top_k: int = 3, device: str = "cuda", debug: bool = False):
        self.top_k = top_k
        self.device = device
        self.debug = debug
        self.db_path = db_path

        safe_dense = get_model_alias(dense_model)
        is_bgem3 = "bge-m3" in dense_model.lower()
        
        if is_bgem3 or not sparse_model:
            combined_name = safe_dense
        else:
            safe_sparse = get_model_alias(sparse_model)
            combined_name = f"{safe_dense}_{safe_sparse}"
            
        self.db_path = os.path.join(self.db_path, f"{dataset_name}_{combined_name}")
        self.collection_name = f"{dataset_name}_{combined_name}_docs"
        
        safe_repo_name = "models--" + dense_model.replace("/", "--")
        snapshot_dir = f"/hf_cache/hub/{safe_repo_name}/snapshots"
        
        try:
            hash_folder = os.listdir(snapshot_dir)[0]
            local_model_path = os.path.join(snapshot_dir, hash_folder)
        except Exception:
            local_model_path = dense_model

        logger.info(f"Loading Retriever: {dense_model} on {device}...")
        self.encoder = SentenceTransformer(local_model_path, device=device, trust_remote_code=True, model_kwargs={"dtype": torch.bfloat16})
        self.client = chromadb.PersistentClient(path=self.db_path)
        
        try:
            self.collection = self.client.get_collection(self.collection_name)
        except Exception as e:
            logger.error(f"Error loading collection '{self.collection_name}': {e}")
            raise

    def _retrieve(self, query: str) -> List[Document]:
        self.encoder.max_seq_length = 512
        
        query_embedding = self.encoder.encode(
            [query], 
            convert_to_tensor=False,
            normalize_embeddings=True
        )[0].tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=self.top_k
        )

        documents = []
        ids = results.get("ids", [[]])[0]
        docs = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        for i in range(len(ids)):
            meta = metadatas[i] if metadatas and i < len(metadatas) else {}
            real_source_id = meta.get("source_id", ids[i].split("_chunk")[0])
            
            doc = Document(
                chunk_id=ids[i],
                source_id=str(real_source_id),
                content=docs[i],
                score=distances[i] if i < len(distances) else 0.0,
                metadata=meta
            )
            documents.append(doc)
            
        return documents
    
    def process(self, sample):
        all_results = []
        queries = sample.search_queries if sample.search_queries else [sample.claim]
        
        for query in queries:
            results = self._retrieve(query)
            all_results.extend(results)
            MetricsRecorder.record_retrieval_call(sample)
        
        seen = set()
        unique_results = []
        for doc in all_results:
            cid = getattr(doc, 'chunk_id', doc.source_id)
            if cid not in seen:
                seen.add(cid)
                unique_results.append(doc)

        sample.retrieved_evidence = unique_results

        return sample


class SkipRetriever(BaseRetriever):
    """No-operation retriever (Never Retrieve mode)."""
    def _retrieve(self, query: str) -> List[Document]:
        return []
    
    def process(self, sample):
        return sample
    

class GoldRetriever(BaseRetriever):
    """Retriever that exclusively returns the gold evidence for upper-bound testing."""
    def __init__(self, dataset_name: str, db_path: str = None, collection: str = None):
        self.dataset_name = dataset_name.lower()
        self.collection_name = collection
        
        if db_path and collection:
            logger.info(f"Loading Gold Retriever for {dataset_name} using DB: {db_path}")
            self.client = chromadb.PersistentClient(path=db_path)
            self.collection = self.client.get_collection(self.collection_name)
        else:
            self.collection = None
            logger.info(f"Loading Gold Retriever for {dataset_name} (Raw Text Fallback Mode)")

    def _retrieve(self, query: str) -> List[Document]:
        return []
        
    def process(self, sample):
        documents = []
        if not sample.gold_evidence:
            sample.retrieved_evidence = []
            return sample

        MetricsRecorder.record_retrieval_call(sample)

        if self.collection:
            gold_ids = [str(gid) for gid in sample.gold_evidence]
            results = self.collection.get(
                where={"source_id": {"$in": gold_ids}}
            )
            
            docs = results.get("documents", [])
            ids = results.get("ids", [])
            metadatas = results.get("metadatas", [])
            
            for i in range(len(ids)):
                meta = metadatas[i] if metadatas and i < len(metadatas) else {}
                real_source_id = meta.get("source_id", ids[i].split("_chunk")[0])
                
                documents.append(Document(
                    chunk_id=ids[i],
                    source_id=str(real_source_id),
                    content=docs[i],
                    score=1.0, 
                    metadata=meta
                ))
        else: # if no db_path and collection
            for i, text in enumerate(sample.gold_evidence):
                documents.append(Document(
                    chunk_id=f"gold_{sample.id}_chunk{i}",
                    source_id=f"gold_{sample.id}",
                    content=str(text),
                    score=1.0,
                    metadata={}
                ))
                
        sample.retrieved_evidence = documents
        return sample


# The Qwen3 reranker is a GENERATIVE model, not a standard cross-encoder.
# It must NOT be loaded with AutoModelForSequenceClassification or via the
# sentence-transformers CrossEncoder API — both will produce garbage scores.
#
# Correct scoring mechanism:
#   1. Format each (claim, doc) pair using the chat template below.
#   2. Run a forward pass and extract the logits of the LAST generated token.
#   3. Score = log P("yes") - log P("no") at that token position.
#
# The instruction field is critical for fact-checking tasks. The default
# instruction ("Given a web search query...") causes
# the model to penalize documents that REFUTE the claim. We override it with
# an instruction that explicitly asks for evidential relevance regardless of
# stance.
# ---------------------------------------------------------------------------

def _build_qwen3_reranker_prompt(instruction: str, query: str, doc: str) -> list:
    """
    Build the chat-template messages for a single (query, doc) pair.
    Must be formatted this way — raw string input will not work.
    """
    return [
        {
            "role": "system",
            "content": (
                "Judge whether the Document meets the requirements based on the "
                "Query and the Instruct provided. "
                "Note that the answer can only be \"yes\" or \"no\"."
            )
        },
        {
            "role": "user",
            "content": f"<Instruct>: {instruction}\n\n<Query>: {query}\n\n<Document>: {doc}"
        }
    ]


class QwenReranker:
    """
    Wrapper around Qwen3-Reranker-0.6B (or any Qwen3-Reranker variant).

    Scores are derived from the yes/no token logits at the final generation
    step — NOT from a classification head. Loading this model as a standard
    CrossEncoder will produce random/inverted rankings.

    Args:
        model_name:  HuggingFace model id, e.g. "Qwen/Qwen3-Reranker-0.6B"
        instruction: Task-specific instruction injected into every prompt.
                     Overriding the default web-search instruction is essential
                     for fact-checking, where contradicting evidence is relevant.
        device:      "cuda" or "cpu"
        max_length:  Token budget per (query, doc) pair (model max is 32 768).
    """

    INSTRUCTION = (
        "Given a claim, retrieve passages that contain relevant evidence for "
        "verifying the claim. A passage is relevant whether it supports OR "
        "contradicts the claim — stance does not affect relevance."
    )

    def __init__(
        self,
        model_name: str = "Qwen/Qwen3-Reranker-0.6B",
        instruction: Optional[str] = None,
        device: str = "cuda",
        max_length: int = 2048,
    ):
        self.device = device
        self.max_length = max_length
        self.instruction = instruction if instruction is not None else self.INSTRUCTION

        logger.info(f"Loading Qwen3 reranker: {model_name} on {device}...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")
        self.model = LLM(model=model_name, 
                            enable_prefix_caching=True, 
                            gpu_memory_utilization=0.22, # ~10gb VRAM, 4b model in bf16 needs ~8gb + kv cache
                            max_model_len=self.max_length,
                            trust_remote_code=True,
                            # quantization="bitsandbytes", # quantization disabled to preserve accuracy
                            # load_format="bitsandbytes",
                            enforce_eager=True)

        # Resolve the token ids for "yes" and "no" once at init time.
        # The model scores = log P(yes_token) - log P(no_token) at the last position.
        self.token_true_id  = self.tokenizer.convert_tokens_to_ids("yes")
        self.token_false_id = self.tokenizer.convert_tokens_to_ids("no")

        # Suffix that primes the model to emit a yes/no token next.
        # The chat template ends with <|im_start|>assistant\n; we append
        # the suffix AFTER applying the template so the model "sees" it
        # as the beginning of its own turn.
        self._suffix = "<|im_start|>assistant\n<think>\n\n</think>\n\n"
        self._suffix_ids = self.tokenizer.encode(self._suffix, add_special_tokens=False)

        logger.info("✅ Qwen3 reranker loaded.")

    def rerank(self, query: str, documents: List[Document]) -> List[Document]:
        """
        Rerank `documents` by evidential relevance to `query`.
        Returns the list sorted by descending reranker score (score attribute updated in-place).
        """
        if not documents:
            return documents
        
        batch_prompts = []
        for doc in documents:
            messages = _build_qwen3_reranker_prompt(self.instruction, query, doc.content)

            # Apply the HuggingFace chat template (no generation prompt —
            # we append the suffix manually to control the token budget).
            input_ids = self.tokenizer.apply_chat_template(
                messages,
                tokenize=True,
                add_generation_prompt=False,
                enable_thinking=False,   # disable chain-of-thought for speed
            )

            # Append suffix, then truncate to max_length from the LEFT
            # (preserve the end of the document rather than the beginning).
            input_ids = (input_ids + self._suffix_ids)[-self.max_length:]
            batch_prompts.append({"prompt_token_ids": input_ids})

        # Ask for top 20 logprobs to ensure we capture the probabilities of 'yes' and 'no'
        sampling_params = SamplingParams(max_tokens=1, temperature=0.3, logprobs=20)
        
        outputs = self.model.generate(batch_prompts, sampling_params=sampling_params, use_tqdm=False)

        scores = []
        for out in outputs:
            # logprobs[0] is a dict of {token_id: Logprob_object} for the first generated token
            first_token_logprobs = out.outputs[0].logprobs[0]
            
            true_obj = first_token_logprobs.get(self.token_true_id)
            false_obj = first_token_logprobs.get(self.token_false_id)
            
            # vLLM returns Logprob objects which have a .logprob attribute. Fallback to -100 if not in top 20
            tl = getattr(true_obj, "logprob", -100.0) if true_obj else -100.0
            fl = getattr(false_obj, "logprob", -100.0) if false_obj else -100.0
            
            score = tl - fl
            scores.append(score)

        # Update document scores and sort descending
        for doc, score in zip(documents, scores):
            doc.score = score

        return sorted(documents, key=lambda d: d.score, reverse=True)


# HybridRetriever (dense + sparse -> RRF -> Qwen3 reranker)

class HybridRetriever(BaseRetriever):
    def __init__(
        self,
        dataset_name: str,
        db_path: str,
        model_type: str = "qwen-splade", 
        top_k_retrieve: int = 100,
        top_k_rerank: int = 50,
        top_k_final: int = 3,
        rrf_k: int = 60,
        alpha: float = 0.5,
        device: str = "cuda",
        debug: bool = False,
        use_reranker: bool = True,
        reranker_model: str = "Qwen/Qwen3-Reranker-0.6B",
        reranker_instruction: Optional[str] = None,
        reranker_max_length: int = 4096,
        dense_model: str = "Qwen/Qwen3-Embedding-0.6B",
        dense_instruction: str = "Retrieve documents that provide explicit evidence to either support or completely refute this claim: ",
        sparse_model: str = "naver/splade-cocondenser-ensembledistil"
    ):
        self.top_k_retrieve = top_k_retrieve
        self.top_k_rerank = top_k_rerank
        self.top_k_final = top_k_final
        self.rrf_k = rrf_k
        self.alpha = alpha
        self.device = device
        self.debug = debug
        self.model_type = model_type
        self.dense_instruction = dense_instruction
        self.use_reranker = use_reranker
        self.db_path = db_path

        # Dynamic Path Generation
        safe_dense = get_model_alias(dense_model)
        is_bgem3 = "bge-m3" in dense_model.lower()
        
        if is_bgem3:
            combined_name = safe_dense
        else:
            safe_sparse = get_model_alias(sparse_model)
            combined_name = f"{safe_dense}_{safe_sparse}"
            
        self.db_path = os.path.join(self.db_path, f"{dataset_name}_{combined_name}")
        self.collection_name = f"{dataset_name}_{combined_name}_docs"
        sparse_index_path = os.path.join(self.db_path, "sparse_index.pkl")

        # 1. Load Encoding Engine
        if self.model_type == "bgem3":
            from FlagEmbedding import BGEM3FlagModel
            logger.info(f"Loading Unified Encoder (BGE-M3) on {device}...")
            self.encoder = BGEM3FlagModel("BAAI/bge-m3", use_fp16=(device == "cuda"))
        elif self.model_type == "qwen-splade":
            logger.info(f"Loading Decoupled Dense Encoder ({dense_model}) on {device}...")
            self.dense_encoder = SentenceTransformer(dense_model, device=device, trust_remote_code=True, model_kwargs={"dtype": torch.bfloat16})
            logger.info(f"Loading Decoupled Sparse Encoder ({sparse_model}) on {device}...")
            self.sparse_encoder = SpladeEncoder(sparse_model, device=device)
        else:
            raise ValueError(f"Unknown model_type: {self.model_type}")

        # 2. Initialize Chroma & Pickled Indexes
        logger.info(f"Connecting to ChromaDB at {self.db_path}...")
        self.client = chromadb.PersistentClient(path=self.db_path)
        try:
            self.collection = self.client.get_collection(self.collection_name)
        except Exception as e:
            logger.error(f"Error loading collection: {e}")
            raise
        
        logger.info(f"Loading sparse index from {sparse_index_path}...")
        with open(sparse_index_path, 'rb') as f:
            self.inverted_index = pickle.load(f)
        logger.info(f"✅ Sparse index loaded: {len(self.inverted_index)} unique tokens")

        # 3. Initialize Reranker
        if self.use_reranker:
            self.reranker = QwenReranker(
                model_name=reranker_model,
                instruction=reranker_instruction,
                device=device,
                max_length=reranker_max_length,
            )
        else:
            self.reranker = None
            logger.info("ℹ️ Reranker disabled — running RRF-only mode.")

        logger.info("✅ HybridRetriever initialized.")

    # Internal retrieval helpers

    def _get_dense_results(self, query_dense_vec: list) -> List[Tuple[str, float]]:
        results = self.collection.query(
            query_embeddings=[query_dense_vec],
            n_results=self.top_k_retrieve
        )
        ids = results.get("ids", [[]])[0]
        distances = results.get("distances", [[]])[0]
        return list(zip(ids, distances))
    
    def _get_sparse_results(self, query_lexical_weights: Dict[int, float]) -> List[Tuple[str, float]]:
        chunk_scores = defaultdict(float)
        for token_id, query_weight in query_lexical_weights.items():
            tok_str = str(token_id)
            tok_int = int(token_id) if tok_str.isdigit() else None
            
            target_key = None
            if tok_str in self.inverted_index:
                target_key = tok_str
            elif tok_int is not None and tok_int in self.inverted_index:
                target_key = tok_int
                
            if target_key is not None:
                for chunk_id, chunk_weight in self.inverted_index[target_key].items():
                    chunk_scores[str(chunk_id)] += query_weight * chunk_weight
        
        sorted_chunks = sorted(chunk_scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_chunks[:self.top_k_retrieve]
    
    def _rrf_fusion(
        self,
        dense_results: List[Tuple[str, float]],
        sparse_results: List[Tuple[str, float]]
    ) -> List[Tuple[str, float]]:
        """Weighted Reciprocal Rank Fusion → sorted (chunk_id, rrf_score) list."""
        rrf_scores = defaultdict(float)
        
        for rank, (chunk_id, _) in enumerate(dense_results, start=1):
            rrf_scores[chunk_id] += self.alpha * (1.0 / (self.rrf_k + rank))
            
        for rank, (chunk_id, _) in enumerate(sparse_results, start=1):
            rrf_scores[chunk_id] += (1.0 - self.alpha) * (1.0 / (self.rrf_k + rank))
        
        return sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)


    def _retrieve(self, query: str, gold_ids: List[str] = None) -> List[Document]:
        
        if self.model_type == "bgem3":
            query_output = self.encoder.encode(
                [query], return_dense=True, return_sparse=True, return_colbert_vecs=False, batch_size=1
            )
            q_vec = np.array(query_output["dense_vecs"][0])
            query_dense = (q_vec / np.linalg.norm(q_vec)).tolist()
            query_sparse = query_output["lexical_weights"][0]
        else:
            # Qwen3 Dense + SPLADE Sparse
            if self.dense_instruction:
                full_query = f"Instruct: {self.dense_instruction}\nQuery: {query}"
            else:
                full_query = query
            
            # Explicitly cap max_length for the dense query just to be safe
            self.dense_encoder.max_seq_length = 512
            query_dense = self.dense_encoder.encode([full_query], normalize_embeddings=True)[0].tolist()
            
            # SPLADE encodes the raw query without the dense instruction
            query_sparse = self.sparse_encoder.encode([query], max_length=512)[0]
        
        dense_results  = self._get_dense_results(query_dense)
        sparse_results = self._get_sparse_results(query_sparse)
        
        if self.debug:
            logger.info("\n" + "="*50)
            logger.info(f"🔍 DIAGNOSTIC: Dense: {len(dense_results)} results | Sparse: {len(sparse_results)} results")
            logger.info(f"🔍 Gold IDs: {gold_ids}")
            if gold_ids:
                dense_found  = [doc for doc, _ in dense_results[:10]  if doc.split("_chunk")[0] in gold_ids]
                sparse_found = [doc for doc, _ in sparse_results[:10] if doc.split("_chunk")[0] in gold_ids]
                logger.info(f"🔍 Top 10 Dense: {dense_results[:10]}")
                logger.info(f"🔍 Top 10 Sparse: {sparse_results[:10]}")
                logger.info(f"🟢 GOLD IN DENSE TOP 10?  {'YES → '+str(dense_found)  if dense_found  else 'NO'}")
                logger.info(f"🟢 GOLD IN SPARSE TOP 10? {'YES → '+str(sparse_found) if sparse_found else 'NO'}")
            else:
                logger.info("⚪ NO GOLD EVIDENCE FOR THIS CLAIM")
            logger.info("="*50)
        
        fused_results = self._rrf_fusion(dense_results, sparse_results)

        if self.use_reranker and self.reranker is not None:
            candidate_pool = fused_results[:self.top_k_rerank]
        else:
            candidate_pool = fused_results[:self.top_k_final]

        if not candidate_pool:
            return []
        
        candidate_ids = [chunk_id for chunk_id, _ in candidate_pool]

        chroma_results = self.collection.get(
            ids=candidate_ids,
            include=["documents", "metadatas"]
        )
        
        id_to_text = {
            chunk_id: chroma_results["documents"][i]
            for i, chunk_id in enumerate(chroma_results["ids"])
        }
        id_to_meta = {
            chunk_id: (chroma_results["metadatas"][i] or {})
            for i, chunk_id in enumerate(chroma_results["ids"])
        }
        
        candidate_chunks = []
        for chunk_id, rrf_score in candidate_pool:
            if chunk_id in id_to_text:
                metadata = id_to_meta.get(chunk_id, {})
                # We extract the parent source_id from the metadata
                chunk_source_id = metadata.get("source_id", chunk_id.split("_chunk")[0])
                candidate_chunks.append(Document(
                    source_id=chunk_source_id,
                    chunk_id=chunk_id,
                    content=id_to_text[chunk_id],
                    score=float(rrf_score),
                    metadata=metadata
                ))

        if self.use_reranker and self.reranker is not None:
            if self.debug:
                pre_ids = [d.chunk_id for d in candidate_chunks]
                logger.info(f"🔄 Reranking {len(candidate_chunks)} candidates → top {self.top_k_final}")
                if gold_ids:
                    gold_in_pool = [d for d in candidate_chunks if d.source_id in gold_ids]
                    logger.info(f"🟢 GOLD IN RERANKER POOL? "
                                f"{'YES → '+str([d.chunk_id for d in gold_in_pool]) if gold_in_pool else 'NO'}")

            reranked = self.reranker.rerank(query, candidate_chunks)

            if self.debug and gold_ids:
                for rank, doc in enumerate(reranked, start=1):
                    if doc.source_id in gold_ids:
                        logger.info(f"🏆 GOLD doc rank after reranking: {rank}/{len(reranked)} "
                                    f"(score={doc.score:.4f})")

            candidate_chunks = reranked[:self.top_k_final]
        
        return candidate_chunks

    def process(self, sample):
        all_results = []
        queries = sample.search_queries if sample.search_queries else [sample.claim]
        gold_ids = [str(gid) for gid in sample.gold_evidence] if sample.gold_evidence else []
        
        for query in queries:
            results = self._retrieve(query, gold_ids=gold_ids)
            all_results.extend(results)
            MetricsRecorder.record_retrieval_call(sample)
        
        seen = set()
        unique_results = []
        for doc in all_results:
            cid = getattr(doc, 'chunk_id', doc.source_id)
            if cid not in seen:
                seen.add(cid)
                unique_results.append(doc)
        
        sample.retrieved_evidence = unique_results
        return sample
