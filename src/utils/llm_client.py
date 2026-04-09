from functools import partial
import torch
from transformers import AutoTokenizer
from tenacity import retry, stop_after_attempt, wait_fixed
import logging
from vllm import LLM, SamplingParams
import os
from google import genai
from google.genai import types
from openai import OpenAI
import gc
from vllm.distributed.parallel_state import destroy_model_parallel, destroy_distributed_environment
        
logger = logging.getLogger(__name__)

class LocalLLMClient:
    def __init__(self, model_name: str, device: str = "cuda"):
        self.device = device
        self.model_name = model_name

        print(f"Initializing vLLM Engine: {model_name}...")
        try:
            # Initialize the shared vLLM engine.
            self.llm = LLM(
                model=model_name,
                gpu_memory_utilization=0.85,
                max_model_len=4096,
                trust_remote_code=True,
                quantization="bitsandbytes",
                load_format="bitsandbytes",
            )
            
            # Permanently bakes "use_tqdm=False" into this specific vLLM engine 
            # instance's generate method so lm-polygraph calls it silently.
            self.llm.generate = partial(self.llm.generate, use_tqdm=False)
            
            self.tokenizer = self.llm.get_tokenizer()
            print("✅ vLLM Engine successfully loaded.")
            
        except Exception as e:
            logger.error(f"Failed to load vLLM model {model_name}: {e}")
            raise

    def get_backend_objects(self):
        # We pass the vLLM engine itself to lm-polygraph, NOT the HF model!
        return self.llm, self.tokenizer

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def generate(self, prompt_text: str, config: dict) -> dict:
        """
        Generates text using the vLLM engine (used by your RAG verifier).
        """
        try:
            # 1. Format Input
            messages = [{"role": "user", "content": prompt_text}]
            text = self.tokenizer.apply_chat_template(
                messages, 
                tokenize=False, 
                add_generation_prompt=True
            )
            
            max_new_tokens = config.get("max_new_tokens", 1024) 

            # 2. Configure vLLM Sampling
            sampling_params = SamplingParams(
                temperature=0.0, # Greedy decoding
                max_tokens=max_new_tokens,
                stop=["<|im_end|>", "<|eot_id|>", "```"]
            )

            # 3. Inference
            outputs = self.llm.generate([text], sampling_params)
            
            # 4. Extract Output
            output = outputs[0]
            decoded_output = output.outputs[0].text.strip()
            
            # Clean up trailing backticks
            decoded_output = decoded_output.replace("```json", "").replace("```", "").strip()

            # 5. Return Structured Response (ready for your .jsonl storage)
            return {
                "content": decoded_output,
                "usage": {
                    "input_tokens": len(output.prompt_token_ids),
                    "output_tokens": len(output.outputs[0].token_ids)
                }
            }

        except Exception as e:
            logger.error(f"Error generating text via vLLM: {e}")
            raise

    def close(self):
        """Properly shuts down the vLLM engine and frees resources."""
        try:
            if hasattr(self, 'llm'):
                if hasattr(self.llm, 'llm_engine'):
                    del self.llm.llm_engine
                del self.llm
        except Exception:
            pass
            
        try:
            destroy_model_parallel()
            destroy_distributed_environment()
        except Exception:
            pass
            
        gc.collect()
        torch.cuda.empty_cache()


class GeminiLLMClient:
    def __init__(self, model_name: str = "gemini-2.5-flash", api_key: str = None):     
        self.model_name = model_name
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        
        if not self.api_key or self.api_key == "your_gemini_api_key_here":
            raise ValueError("GEMINI_API_KEY environment variable is missing or placeholder.")
        
        try:
            print(f"Initializing Gemini Client: {model_name}...")
            self.client = genai.Client()
            print("✅ Gemini Client successfully loaded.")
        except Exception as e:
            logger.error(f"Failed to load Gemini client: {e}")
            raise

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def generate(self, prompt_text: str, config: dict) -> dict:
        """
        Generates text using the Gemini API.
        """
        try:
            # We explicitly override the small `max_new_tokens` (256) intended for local vLLM 
            # because the genai API or the preview models appear to be treating it as 
            # max total tokens (prompt + output) or hitting a related limit bug.
            max_new_tokens = 4096 
            
            # Disable safety filters as medical/political claims often trigger false positives
            safety_settings = [
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                )
            ]
            
            generation_config = types.GenerateContentConfig(
                max_output_tokens=max_new_tokens,
                temperature=0.0,
                safety_settings=safety_settings
            )
            
            response = self.client.models.generate_content(
                model = self.model_name,
                contents = prompt_text,
                config=generation_config
            )
            
            # Extract finish reason to diagnose abrupt stops
            finish_reason = "UNKNOWN"
            if hasattr(response, "candidates") and response.candidates:
                finish_reason = response.candidates[0].finish_reason
            print(f"    [DEBUG-GEMINI] Finish Reason: {finish_reason}")
            
            try:
                decoded_output = response.text.strip()
                print(f"  -> [DEBUG] Raw LLM Output:\n{decoded_output}\n")
            except Exception:
                decoded_output = ""
                
            # Clean up trailing backticks
            decoded_output = decoded_output.replace("```json", "").replace("```", "").strip()

            input_tokens = 0
            output_tokens = 0
            if hasattr(response, "usage_metadata") and response.usage_metadata:
                if response.usage_metadata.prompt_token_count:
                    input_tokens = int(response.usage_metadata.prompt_token_count)
                if response.usage_metadata.candidates_token_count:
                    output_tokens = int(response.usage_metadata.candidates_token_count)

            return {
                "content": decoded_output,
                "usage": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens
                }
            }
        except Exception as e:
            logger.error(f"Error generating text via Gemini: {e}")
            raise


class OpenAILLMClient:
    def __init__(self, model_name: str = "gpt-5.4-nano-2026-03-17", api_key: str = None):     
        self.model_name = model_name
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        
        if not self.api_key or self.api_key == "your_openai_api_key_here":
            raise ValueError("OPENAI_API_KEY environment variable is missing or placeholder.")
        
        try:
            print(f"Initializing OpenAI Client: {model_name}...")
            self.client = OpenAI(timeout=20.0)
            print("✅ OpenAI Client successfully loaded.")
        except Exception as e:
            logger.error(f"Failed to load OpenAI client: {e}")
            raise

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def generate(self, prompt_text: str, config: dict) -> dict:
        """
        Generates text using the OpenAI API.
        """
        try:
            # We explicitly override small max_new_tokens just like the Gemini client
            max_new_tokens = config.get("max_new_tokens", 4096)
            temperature = config.get("temperature", 0.0)
            
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt_text}
                ],
                temperature=temperature,
                max_completion_tokens=max_new_tokens,
            )
            
            # Extract finish reason to diagnose abrupt stops (e.g., "stop" or "length")
            finish_reason = "UNKNOWN"
            if response.choices:
                finish_reason = response.choices[0].finish_reason
            print(f"    [DEBUG-OPENAI] Finish Reason: {finish_reason}")
            
            try:
                decoded_output = response.choices[0].message.content.strip()
                print(f"  -> [DEBUG] Raw LLM Output:\n{decoded_output}\n")
            except Exception:
                decoded_output = ""
                
            # --- Output Sanitation ---
            # OpenAI models commonly wrap structured outputs in markdown blocks.
            # This safely strips ```json, ```markdown, and the closing ```.
            if decoded_output.startswith("```"):
                lines = decoded_output.split("\n")
                if lines[0].startswith("```"):
                    lines = lines[1:]  # Drop the top line (e.g., ```json)
                if lines and lines[-1].startswith("```"):
                    lines = lines[:-1] # Drop the bottom line (```)
                decoded_output = "\n".join(lines).strip()
                
            # Extract token usage
            input_tokens = 0
            output_tokens = 0
            if response.usage:
                input_tokens = response.usage.prompt_tokens
                output_tokens = response.usage.completion_tokens

            return {
                "content": decoded_output,
                "usage": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens
                }
            }
        except Exception as e:
            logger.error(f"Error generating text via OpenAI: {e}")
            raise
            
    def close(self):
        """Cleanup method if your pipeline explicitly calls close()."""
        pass