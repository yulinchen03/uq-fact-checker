import os
import torch
from pathlib import Path
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# UQ imports
from lm_polygraph.utils.model import WhiteboxModel
from lm_polygraph.estimators import SemanticEntropy, MeanTokenEntropy
from lm_polygraph.utils.manager import estimate_uncertainty

CURRENT_SCRIPT_DIR = Path(__file__).resolve().parent

PROJECT_ROOT = CURRENT_SCRIPT_DIR.parent.parent

DEFAULT_DB_PATH = PROJECT_ROOT / "chroma_db_semantic"

class RAG:
    def __init__(self, model_id="Qwen/Qwen2.5-3B-Instruct", db_path=None):
        """
        Initializes the RAG system.
        - Loads the LLM and Tokenizer (Heavy operation, run once).
        - Connects to the Vector Database.
        
        Args:
            model_id: HuggingFace model ID.
            db_path: (Optional) Path to vector DB. Defaults to PROJECT_ROOT/chroma_db_semantic
        """
        # Use the calculated default if no path is provided
        self.db_path = str(db_path) if db_path else str(DEFAULT_DB_PATH)
        self.model_id = model_id
        
        print(f"Initializing LocalRAG with model: {model_id}...")
        print(f"Connecting to Vector DB at: {self.db_path}")
        
        # 1. Setup Embedding Model (Must match the one used for indexing)
        self.embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        
        # 2. Connect to Vector DB
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"Vector database not found at {self.db_path}. Please run vector_db.py first.")
            
        self.db = Chroma(persist_directory=self.db_path, embedding_function=self.embedding_model)
        self.retriever = self.db.as_retriever(search_kwargs={"k": 3})

        # 3. Load LLM
        print("Loading LLM ...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            torch_dtype="auto",
            trust_remote_code=True
        )

        print("Initializing Uncertainty Estimator...")
        self.whitebox_model = WhiteboxModel(
            self.model, 
            self.tokenizer, 
            model_path=model_id
        )

        self.estimator = SemanticEntropy()

        # Define terminators for ChatML format to stop generation cleanly
        self.terminators = [
            self.tokenizer.eos_token_id,
            self.tokenizer.convert_tokens_to_ids("<|endoftext|>"),
            self.tokenizer.convert_tokens_to_ids("<|im_end|>")
        ]

        # Create Pipeline
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=512,
            temperature=0.1,
            repetition_penalty=1.1,
            return_full_text=False,
            eos_token_id=self.terminators,
            do_sample=True
        )
        
        self.llm = HuggingFacePipeline(pipeline=self.pipe)
        
        # 4. Define Prompt Template (ChatML)
        self.template = """<|im_start|>system
You are a helpful assistant. Answer the question strictly based on the context provided. If the answer is not in the context, say "I don't know".<|im_end|>
<|im_start|>user
Context:
{context}

Question: 
{question}<|im_end|>
<|im_start|>assistant
"""

        self.prompt = ChatPromptTemplate.from_template(self.template)
        print("RAG System Ready.")

    def _format_docs(self, docs):
        """Helper to join retrieved documents."""
        return "\n\n".join([doc.page_content for doc in docs])

    def ask(self, query):
        """
        Public method to query the RAG system.
        """
        print("-" * 80)
        print(f"Thinking about: '{query}'...")
        print("-" * 80)
        
        rag_chain = (
            {"context": self.retriever | self._format_docs, "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
        
        return rag_chain.invoke(query)
    
    # def ask(self, query):
    #     print(f"Thinking about: '{query}'...")
        
    #     # Step 1: Retrieve
    #     docs = self.retriever.invoke(query)
    #     context_text = self._format_docs(docs)
        
    #     # DEBUG: Print what the LLM actually sees
    #     print(f"\n[DEBUG] RETRIEVED CONTEXT:\n{context_text}\n" + "-"*20)
        
    #     # Step 2: Generate
    #     # (Re-create the chain here manually to pass the pre-fetched context)
    #     response = (
    #         self.prompt 
    #         | self.llm 
    #         | StrOutputParser()
    #     ).invoke({"context": context_text, "question": query})
        
    #     return response

    def ask_with_uncertainty(self, query):
        """
        RAG query with Uncertainty Estimation.
        Uses lm-polygraph to calculate confidence score.
        """
        print("-" * 80)
        print(f"Thinking (with uncertainty check) about: '{query}'...")
        
        # 1. Manually Retrieve Context
        docs = self.retriever.invoke(query)
        context_text = self._format_docs(docs)
        
        # 2. Manually Format Prompt (Polygraph expects a single string)
        full_input_text = self.template.format(context=context_text, question=query)

        # 3. Estimate Uncertainty
        result = estimate_uncertainty(
            self.whitebox_model, 
            self.estimator, 
            input_text=full_input_text
        )

        # 4. Extract Answer and Score
        answer = result.generation_text
        # Clean up output if needed (sometimes Polygraph returns list of strings)
        if isinstance(answer, list):
            answer = answer[0]

        return answer, result.uncertainty

if __name__ == "__main__":
    rag = RAG()
    
    # Ask questions
    response = rag.ask("What distinct department did the 47th president establish?")
    print("\nANSWER:", response)