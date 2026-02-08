import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from tenacity import retry, stop_after_attempt, wait_fixed
import logging

logger = logging.getLogger(__name__)

class LocalLLMClient:
    def __init__(self, model_name: str, device: str = "cuda"):
        self.device = device
        self.model_name = model_name
        
        print(f"Initializing Local LLM: {model_name} on {device}...")
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name, 
                torch_dtype="auto", 
                device_map=device
            )
        except Exception as e:
            logger.error(f"Failed to load model {model_name}: {e}")
            raise

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
            
            # 3. Extract Config Params (FIXED: Use .get() instead of dot notation)
            max_new_tokens = config.get("max_new_tokens", 512)
            temperature = config.get("temperature", 0.1)
            do_sample = config.get("do_sample", False)

            # 4. Inference
            with torch.no_grad():
                generated_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    temperature=temperature,
                    do_sample=do_sample
                )

            # 5. Decode Output (Slice to remove input tokens)
            # The model returns [input_tokens + new_tokens], we only want new_tokens
            output_ids = generated_ids[0][input_len:]
            decoded_output = self.tokenizer.decode(output_ids, skip_special_tokens=True)
            
            # 6. Return Structured Response
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