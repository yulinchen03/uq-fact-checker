from functools import partial
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, StoppingCriteria, StoppingCriteriaList
from tenacity import retry, stop_after_attempt, wait_fixed
import logging
from vllm import LLM, SamplingParams

logger = logging.getLogger(__name__)

class LocalLLMClient:
    def __init__(self, model_name: str, device: str = "cuda"):
        self.device = device
        self.model_name = model_name
        
    #     print(f"Initializing Local LLM: {model_name} on device {self.device} with INT8 quantization...")
    #     try:
    #         self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            
    #         # --- convert to fp8 ---
    #         quantization_config = BitsAndBytesConfig(
    #             load_in_8bit=True,
    #             llm_int8_threshold=6.0, 
    #             llm_int8_has_fp16_weight=False,
    #         )
            
    #         self.model = AutoModelForCausalLM.from_pretrained(
    #             model_name, 
    #             device_map="auto",
    #             quantization_config=quantization_config,
    #             torch_dtype=torch.float16,
    #             trust_remote_code=True
    #         )
    #         self.model.generation_config.temperature = None
    #         self.model.generation_config.top_p = None
    #         self.model.generation_config.top_k = None
    #         self.model.generation_config.do_sample = False
    #         print("✅ Model successfully loaded in INT8.")
    #         # -------------------------
            
    #     except Exception as e:
    #         logger.error(f"Failed to load model {model_name}: {e}")
    #         raise

    # def get_backend_objects(self):
    #     return self.model, self.tokenizer

        print(f"Initializing vLLM Engine: {model_name}...")
        try:
            # Initialize the shared vLLM engine.
            self.llm = LLM(
                model=model_name,
                gpu_memory_utilization=0.4,
                max_model_len=2500,
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
                stop=["<|im_end|>"]
            )

            # 3. Inference
            outputs = self.llm.generate([text], sampling_params)
            
            # 4. Extract Output
            output = outputs[0]
            decoded_output = output.outputs[0].text.strip()
            
            # Clean up trailing backticks
            decoded_output = decoded_output.replace("```json", "").replace("```", "").strip()

            # 5. Return Structured Response
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

    # def generate(self, prompt_text: str, config: dict) -> dict:
    #     """
    #     Generates text using the local model.
    #     Args:
    #         prompt_text: The input prompt.
    #         config: Dictionary containing generation parameters.
    #     """
    #     try:
    #         # 1. Format Input (Chat Template)
    #         messages = [{"role": "user", "content": prompt_text}]
    #         text = self.tokenizer.apply_chat_template(
    #             messages, 
    #             tokenize=False, 
    #             add_generation_prompt=True
    #         )
            
    #         # 2. Tokenize
    #         inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
    #         input_len = inputs.input_ids.shape[1]
            
    #         # 3. Extract Config Params
    #         max_new_tokens = config.get("max_new_tokens", 1024) 
    #         do_sample = config.get("do_sample", False)

    #         # Only stop on the actual End-Of-Sequence token
    #         terminators = [
    #             self.tokenizer.eos_token_id,
    #             self.tokenizer.convert_tokens_to_ids("<|im_end|>")
    #         ]

    #         # 4. Inference
    #         with torch.no_grad():
    #             generated_ids = self.model.generate(
    #                 **inputs,
    #                 max_new_tokens=max_new_tokens,
    #                 do_sample=do_sample,
    #                 pad_token_id=self.tokenizer.eos_token_id,
    #                 eos_token_id=terminators
    #             )

    #         # 5. Decode Output (Slice to remove input tokens)
    #         output_ids = generated_ids[0][input_len:]
    #         decoded_output = self.tokenizer.decode(output_ids, skip_special_tokens=True)
            
    #         # 6. Clean up any trailing backticks if the stopper caught it mid-generation
    #         decoded_output = decoded_output.replace("```json", "").replace("```", "").strip()

    #         # 7. Return Structured Response
    #         return {
    #             "content": decoded_output,
    #             "usage": {
    #                 "input_tokens": int(input_len),
    #                 "output_tokens": len(output_ids)
    #             }
    #         }

    #     except Exception as e:
    #         logger.error(f"Error generating text: {e}")
    #         raise