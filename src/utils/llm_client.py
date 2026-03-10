import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, StoppingCriteria, StoppingCriteriaList
from tenacity import retry, stop_after_attempt, wait_fixed
import logging

logger = logging.getLogger(__name__)

class StopStringCriteria(StoppingCriteria):
    def __init__(self, tokenizer, stop_strings: list[str], input_len: int):
        self.tokenizer = tokenizer
        self.stop_strings = stop_strings
        self.input_len = input_len # Keep track of where the prompt ends

    def __call__(self, input_ids, scores, **kwargs):
        # Slice the tensor to ONLY look at newly generated tokens
        generated_ids = input_ids[0][self.input_len:]
        
        # If it hasn't generated anything yet, keep going
        if len(generated_ids) == 0:
            return False
            
        # Decode only the last few generated tokens
        decoded_text = self.tokenizer.decode(generated_ids[-10:], skip_special_tokens=False)
        for stop_str in self.stop_strings:
            if stop_str in decoded_text:
                return True
        return False

class LocalLLMClient:
    def __init__(self, model_name: str, device: str = "cuda"):
        self.device = device
        self.model_name = model_name
        
        print(f"Initializing Local LLM: {model_name} on device {self.device} with INT8 quantization...")
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            
            # --- convert to fp8 ---
            quantization_config = BitsAndBytesConfig(
                load_in_8bit=True,
                llm_int8_threshold=6.0, 
                llm_int8_has_fp16_weight=False,
            )
            
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name, 
                device_map="auto",
                quantization_config=quantization_config,
                torch_dtype=torch.float16,
                trust_remote_code=True
            )
            self.model.generation_config.temperature = None
            self.model.generation_config.top_p = None
            self.model.generation_config.top_k = None
            self.model.generation_config.do_sample = False
            print("✅ Model successfully loaded in INT8.")
            # -------------------------
            
        except Exception as e:
            logger.error(f"Failed to load model {model_name}: {e}")
            raise

    def get_backend_objects(self):
        return self.model, self.tokenizer

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def generate(self, prompt_text: str, config: dict) -> dict:
        """
        Generates text using the local model.
        Args:
            prompt_text: The input prompt.
            config: Dictionary containing generation parameters.
        """
        try:
            # 1. Format Input (Chat Template)
            messages = [{"role": "user", "content": prompt_text}]
            text = self.tokenizer.apply_chat_template(
                messages, 
                tokenize=False, 
                add_generation_prompt=True
            )
            
            # 2. Tokenize
            inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
            input_len = inputs.input_ids.shape[1]
            
            # 3. Extract Config Params
            max_new_tokens = config.get("max_new_tokens", 1024) 
            do_sample = config.get("do_sample", False)

            # Only stop on the actual End-Of-Sequence token
            stop_strings = ["<|im_end|>"]
            stopping_criteria = StoppingCriteriaList([StopStringCriteria(self.tokenizer, stop_strings, input_len)])

            # 4. Inference
            with torch.no_grad():
                generated_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    do_sample=do_sample,
                    stopping_criteria=stopping_criteria,
                    pad_token_id=self.tokenizer.eos_token_id,
                    eos_token_id=self.tokenizer.eos_token_id # Added this for native safety!
                )

            # 4. Inference
            with torch.no_grad():
                generated_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    stopping_criteria=stopping_criteria,          # Inject the stopper
                    pad_token_id=self.tokenizer.eos_token_id      # Best practice for HF generate
                )

            # 5. Decode Output (Slice to remove input tokens)
            output_ids = generated_ids[0][input_len:]
            decoded_output = self.tokenizer.decode(output_ids, skip_special_tokens=True)
            
            # 6. Clean up any trailing backticks if the stopper caught it mid-generation
            decoded_output = decoded_output.replace("```json", "").replace("```", "").strip()

            # 7. Return Structured Response
            return {
                "content": decoded_output,
                "usage": {
                    "input_tokens": int(input_len),
                    "output_tokens": len(output_ids)
                }
            }

        except Exception as e:
            logger.error(f"Error generating text: {e}")
            raise