import os
import sys
import json
import random
import time
import hydra
from pathlib import Path
from tqdm import tqdm
from omegaconf import DictConfig
from transformers import AutoTokenizer

import torch
import numpy as np

from dotenv import load_dotenv
load_dotenv()

# Prevent memory fragmentation
os.environ["PYTORCH_ALLOC_CONF"] = "expandable_segments:True"

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from src.utils.loader import LocalDataLoader
from src.modules.uq_verifier import UQVerifier
from transformers import set_seed
from vllm import LLM, SamplingParams
from vllm.sampling_params import StructuredOutputsParams
from lm_polygraph.model_adapters import WhiteboxModelvLLM
from lm_polygraph.utils.generation_parameters import GenerationParameters

original_generate = LLM.generate

def silent_generate(self, *args, **kwargs):
    kwargs["use_tqdm"] = False
    return original_generate(self, *args, **kwargs)

LLM.generate = silent_generate

def lock_random_seeds(seed: int = 42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    set_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="Run UQ scores generation")
    parser.add_argument("--dataset", type=str, default=None, help="Override dataset name")
    parser.add_argument("--split", type=str, default=None, help="Override split name")
    parser.add_argument("--model", type=str, default=None, help="Override model name")
    
    parser.add_argument("--check_logic", action="store_true", help="Enable the Logical Contradiction check")
    parser.add_argument("--output_format", type=str, choices=["full_response", "label_only"], default="label_only", help="Format of the LLM generation")
    parser.add_argument("--logic_eval_method", type=str, choices=["discrete", "probabilistic"], default="discrete", help="Evaluation method for the logical contradiction")

    return parser.parse_known_args()

def main():
    args, unknown = parse_args()
    from hydra import compose, initialize_config_dir
    initialize_config_dir(config_dir=str(project_root / "config"), version_base=None)
    if args.dataset and not any(arg.startswith("data=") for arg in unknown):
        unknown.append(f"data={args.dataset}")
        
    cfg = compose(config_name="config", overrides=unknown)

    if "AUTO_CONFIG" in os.environ:
        auto_cfg = json.loads(os.environ["AUTO_CONFIG"])
        if "dataset" in auto_cfg: cfg.data.dataset_name = auto_cfg["dataset"]
        if "calibration_split" in auto_cfg: cfg.data.split = auto_cfg["calibration_split"]
            
    if args.dataset: cfg.data.dataset_name = args.dataset
    if args.split: cfg.data.split = args.split
    if args.model: cfg.llm.model_name = args.model

    lock_random_seeds(42)
    device = cfg.llm.device
    dataset_name = cfg.data.dataset_name
    split = cfg.data.split
    full_model_name = cfg.llm.model_name
    model_name = full_model_name.split("/")[-1]

    if args.check_logic:
        logic_str = f"logic_{args.logic_eval_method}"
    else:
        logic_str = "logic_OFF"

    base_out_dir = project_root / "run_results" / dataset_name / model_name / "calibration"
    base_out_dir.mkdir(parents=True, exist_ok=True)
    out_file = base_out_dir / f"uq_scores_{split}_{args.output_format}_{logic_str}.jsonl"

    print(f"\n🚀 Initializing LLM for Joint Calibration: {cfg.llm.model_name} on {device}")
    print(f"⚙️  Settings: Format=[{args.output_format}], Logical Contradiction Check=[{'ON (' + args.logic_eval_method + ')' if args.check_logic else 'OFF'}]")
    
    llm_engine = LLM(
        model=full_model_name,
        gpu_memory_utilization=0.75,
        max_model_len=4096,
        trust_remote_code=True,
        quantization="bitsandbytes",
        load_format="bitsandbytes",
        enforce_eager=True
    )

    # Shared generation config
    GEN_TEMPERATURE = 0.5 if cfg.uncertainty.method == "SemanticEntropy" else 0.0
    GEN_STOP_TOKENS = ["<|im_end|>", "<|eot_id|>", "```", "<|im_start|>", "<|start_header_id|>"]

    if args.output_format == "label_only":
        allowed_labels = ["True", "False", "Conflicting"] if dataset_name.lower() == "quantemp" else ["SUPPORT", "CONTRADICT", "NOT ENOUGH INFO"]
        generator_params = SamplingParams(
            temperature=GEN_TEMPERATURE,
            max_tokens=5, 
            logprobs=10,
            stop=GEN_STOP_TOKENS,
            structured_outputs=StructuredOutputsParams(choice=allowed_labels)
        )
        parametric_prompt = cfg.prompts.parametric_short
    else:
        generator_params = SamplingParams(
            temperature=GEN_TEMPERATURE,
            max_tokens=256,
            logprobs=10,
            stop=GEN_STOP_TOKENS
        )
        parametric_prompt = cfg.prompts.parametric_long

    tokenizer = llm_engine.get_tokenizer()
    if getattr(tokenizer, "eos_token", None) is None and getattr(tokenizer, "eos_token_id", None) is not None:
        tokenizer.eos_token = tokenizer.decode(tokenizer.eos_token_id)

    # GenerationParameters must mirror SamplingParams because WhiteboxModelvLLM.__init__
    # overwrites sampling_params fields (temperature, top_k, top_p, stop) with these values.
    gen_parameters = GenerationParameters(
        temperature=GEN_TEMPERATURE,
        stop_strings=GEN_STOP_TOKENS,
    )
    whitebox_model = WhiteboxModelvLLM(llm_engine, sampling_params=generator_params, generation_parameters=gen_parameters)
    whitebox_model.supports_logprobs = True

    # mistral does not support vllm tokenizer
    if "Mistral" in tokenizer.__class__.__name__:
        # Force-load the standard HuggingFace tokenizer
        hf_tokenizer = AutoTokenizer.from_pretrained(full_model_name)
        
        # Ensure pad token exists
        if getattr(hf_tokenizer, "pad_token", None) is None:
            if getattr(hf_tokenizer, "eos_token", None):
                hf_tokenizer.pad_token = hf_tokenizer.eos_token
            else:
                hf_tokenizer.pad_token = hf_tokenizer.decode(hf_tokenizer.eos_token_id)
                
        # Swap it out inside the whitebox adapter
        whitebox_model.tokenizer = hf_tokenizer

    loader = LocalDataLoader(data_root=str(project_root / "data"))
    dataset_items = loader.load(dataset_name=dataset_name, split=split, mode="always_retrieve")

    print(f"🎯 Output File: {out_file.relative_to(project_root)}")
    open(out_file, 'w').close()

    estimators = [
        "MaximumSequenceProbability",
        "Perplexity",
        "MeanTokenEntropy",
    ]
    
    uq_engine = UQVerifier(model=whitebox_model, estimator_name=estimators)
    from src.modules.ace import AdversarialConsistencyEvaluator
    ace = AdversarialConsistencyEvaluator(model=whitebox_model)

    print(f"🔄 Starting UQ metric generation across {len(dataset_items)} claims...")
    
    with open(out_file, "a") as f_out:
        for item in tqdm(dataset_items, desc="Generating Joint Methods UQ Scores"):
            try:
                # 1. Evaluate original claim (Universal call)
                final_clean, uq_scores, verdict, _, _, _, _ = uq_engine.verify_claim(
                    claim=item.claim,
                    prompt_template=parametric_prompt,
                    dataset_name=dataset_name,
                    output_format=args.output_format
                )

                # 2. Evaluate negated claim (ACE)
                if args.check_logic:
                    logic_score, extra_p, extra_r, extra_calls = ace.check_logical_contradiction(
                        uq_verifier=uq_engine,
                        claim=item.claim,
                        original_verdict=verdict,
                        original_uq_scores=uq_scores,
                        parametric_prompt=parametric_prompt,
                        dataset_name=dataset_name,
                        eval_method=args.logic_eval_method,
                        output_format=args.output_format
                    )
                    uq_scores["LogicalContradiction"] = logic_score

                result_record = {
                    "id": item.id,
                    "gold_label": item.gold_label,
                    "parametric_verdict": verdict,
                    "parametric_response": final_clean,
                    "uq_scores": uq_scores
                }
                
                f_out.write(json.dumps(result_record) + "\n")
                f_out.flush()

            except Exception as e:
                print(f"Error processing claim {item.id}: {e}")
                error_record = {
                    "id": item.id,
                    "gold_label": item.gold_label,
                    "parametric_verdict": "ERROR",
                    "parametric_response": str(e),
                    "uq_scores": {est: float('inf') for est in estimators}
                }
                f_out.write(json.dumps(error_record) + "\n")
                f_out.flush()

    print(f"\n✅ All joint UQ Calibration points gathered at: {out_file.relative_to(project_root)}\n")

    print("🧹 Cleaning up vLLM engine and releasing VRAM...")
    del uq_engine
    del whitebox_model
    del llm_engine

    import gc
    gc.collect()

    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    try:
        from vllm.distributed.parallel_state import destroy_model_parallel
        destroy_model_parallel()
    except Exception:
        pass
        
    print("✨ VRAM successfully released. Exiting cleanly.")
    os._exit(0)

if __name__ == "__main__":
    main()