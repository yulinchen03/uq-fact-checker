from functools import partial
import torch
from transformers import AutoTokenizer
from tenacity import retry, stop_after_attempt, wait_fixed
import logging
from vllm import LLM, SamplingParams
from vllm.sampling_params import StructuredOutputsParams
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
            self.llm = LLM(
                model=model_name,
                gpu_memory_utilization=0.47, # ~21gb vram, 30b model in 4 bit needs ~15gb + overhead + kv cache
                max_model_len=4096,
                trust_remote_code=True,
                quantization="bitsandbytes",
                load_format="bitsandbytes",
                enforce_eager=True
            )
            
            self.llm.generate = partial(self.llm.generate, use_tqdm=False)
            self.tokenizer = self.llm.get_tokenizer()
            print("✅ vLLM Engine successfully loaded.")
            
        except Exception as e:
            logger.error(f"Failed to load vLLM model {model_name}: {e}")
            raise

    def get_backend_objects(self):
        return self.llm, self.tokenizer

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def generate(self, prompt_text: str, config: dict) -> dict:
        try:
            suffix = ""
            if prompt_text.endswith("\nVerdict:"):
                prompt_text = prompt_text[:-9].strip()
                suffix = "\nVerdict:"
            elif prompt_text.endswith("\n```json\n"):
                prompt_text = prompt_text[:-9].strip()
                suffix = "\n```json\n"

            messages = [{"role": "user", "content": prompt_text}]
            
            try:
                text = self.tokenizer.apply_chat_template(
                    messages, 
                    tokenize=False, 
                    add_generation_prompt=True
                )
            except ValueError:
                text = prompt_text + "\n\n"
                
            text += suffix
            
            max_new_tokens = config.get("max_new_tokens", 1024) 
            output_format = config.get("output_format", "full_response")
            dataset_name = config.get("dataset", "scifact")

            if output_format == "label_only":
                allowed_labels = ["True", "False", "Conflicting"] if "quantemp" in dataset_name.lower() else ["SUPPORT", "CONTRADICT", "NOT ENOUGH INFO"]
                sampling_params = SamplingParams(
                    temperature=0.5, 
                    max_tokens=5, 
                    stop=["<|im_end|>", "<|eot_id|>", "```", "<|im_start|>", "<|start_header_id|>"],
                    structured_outputs=StructuredOutputsParams(choice=allowed_labels)
                )
            else:
                sampling_params = SamplingParams(
                    temperature=0.5, 
                    max_tokens=max_new_tokens,
                    stop=["<|im_end|>", "<|eot_id|>", "<|im_start|>", "<|start_header_id|>"]
                )

            outputs = self.llm.generate([text], sampling_params)
            
            output = outputs[0]
            decoded_output = output.outputs[0].text.strip()
            decoded_output = decoded_output.replace("```json", "").replace("```", "").strip()

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
                temperature=0.5,
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
    def __init__(self, model_name: str = "gpt-5.4-nano-2026-03-17", api_key: str = None,
                 base_url: str = None, api_key_env: str = "OPENAI_API_KEY"):     
        self.model_name = model_name
        self.api_key = api_key or os.environ.get(api_key_env)
        
        if not self.api_key or self.api_key in ("your_openai_api_key_here", "your_api_key_here"):
            raise ValueError(f"{api_key_env} environment variable is missing or placeholder.")
        
        try:
            provider = f" (via {base_url})" if base_url else ""
            print(f"Initializing OpenAI-Compatible Client: {model_name}{provider}...")
            self.client = OpenAI(api_key=self.api_key, base_url=base_url, timeout=60.0)
            self.base_url = base_url
            self.total_input_tokens = 0
            self.total_output_tokens = 0
            self.total_calls = 0
            print("✅ OpenAI-Compatible Client successfully loaded.")
        except Exception as e:
            logger.error(f"Failed to load OpenAI-compatible client: {e}")
            raise

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def generate(self, prompt_text: str, config: dict) -> dict:
        """
        Generates text using the OpenAI API.
        """
        try:
            # Suffix Handling
            # The verifier appends "\nVerdict:" or "\n```json\n" to prompts for
            # local text-completion style generation. For chat API models, we
            # strip these entirely — they are not needed in the chat format.
            if prompt_text.endswith("\nVerdict:"):
                prompt_text = prompt_text[:-9].strip()
            elif prompt_text.endswith("\n```json\n"):
                prompt_text = prompt_text[:-9].strip()

            max_new_tokens = config.get("max_new_tokens", 4096)
            output_format = config.get("output_format", "full_response")
            
            messages = []
            
            if output_format == "label_only":
                # System message enforces strict label-only output, since
                # API models lack the constrained decoding used by LocalLLMClient.
                dataset = config.get("dataset", "scifact")
                if "quantemp" in dataset.lower():
                    allowed = "True, False, or Conflicting"
                else:
                    allowed = "SUPPORT, CONTRADICT, or NOT ENOUGH INFO"
                    
                messages.append({
                    "role": "system",
                    "content": (
                        f"Respond with EXACTLY ONE label: {allowed}. "
                        "Do not include explanations, reasoning, formatting, "
                        "markdown, punctuation, or the word 'Verdict'. "
                        "Output only the raw label text."
                    )
                })
                max_new_tokens = 20  # "NOT ENOUGH INFO" ≈ 4 tokens
            else:
                # For full_response (JSON), ensure enough room for the response
                max_new_tokens = max(max_new_tokens, 256)
            
            messages.append({"role": "user", "content": prompt_text})
            
            # Only pass enable_thinking for non-OpenAI providers (e.g., Qwen
            # via DashScope) that support it. The standard OpenAI API rejects
            # this parameter with a 400 error.
            api_kwargs = dict(
                model=self.model_name,
                messages=messages,
                temperature=0.5,
                max_completion_tokens=max_new_tokens,
            )
            if self.base_url:
                api_kwargs["extra_body"] = {"enable_thinking": False}
            
            response = self.client.chat.completions.create(**api_kwargs)
            
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
                
            # Output Sanitation
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

            # Accumulate running totals
            self.total_input_tokens += input_tokens
            self.total_output_tokens += output_tokens
            self.total_calls += 1
            print(f"    [TOKEN USAGE] Call #{self.total_calls}: {input_tokens} in / {output_tokens} out | "
                  f"Running total: {self.total_input_tokens} in / {self.total_output_tokens} out "
                  f"({self.total_input_tokens + self.total_output_tokens} total)")

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
            
    def get_backend_objects(self):
        """Stub for API-based clients — no local model/tokenizer objects."""
        return None, None

    def close(self):
        """Print final token usage summary and clean up."""
        print(f"\n{'='*50}")
        print(f"  📊 OPENAI TOKEN USAGE SUMMARY")
        print(f"  Model:         {self.model_name}")
        print(f"  Total Calls:   {self.total_calls}")
        print(f"  Input Tokens:  {self.total_input_tokens:,}")
        print(f"  Output Tokens: {self.total_output_tokens:,}")
        print(f"  Total Tokens:  {self.total_input_tokens + self.total_output_tokens:,}")
        print(f"{'='*50}")