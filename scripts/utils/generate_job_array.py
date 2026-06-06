import os
from pathlib import Path

SEEDS = [42, 1, 2]
MODELS = [
    "Qwen/Qwen3-4B-Instruct-2507",
    "mistralai/Mistral-7B-Instruct-v0.3",
    "meta-llama/Llama-3.1-8B-Instruct",
    # "google/gemma-3-12b-it",
    # "Qwen/Qwen3-30B-A3B-Instruct-2507"
    # "gpt-5.4-mini-2026-03-17",
    # "gpt-5.4-nano-2026-03-17",
    # "qwen3.6-max-preview",
    # "qwen3.6-plus"
]

OPENAI_MODELS = [
    "gpt-5.4-mini-2026-03-17",
    "gpt-5.4-nano-2026-03-17",
    "qwen3.6-max-preview",
    "qwen3.6-plus"
]

DATASETS = [
    {"name": "scifact", "calib_split": "train", "test_split": "val"},
    {"name": "quantemp", "calib_split": "val", "test_split": "test"}
]

UQ_METHODS = [
    "Perplexity",
    "MaximumSequenceProbability",
    "MeanTokenEntropy",
    "LogicalContradiction",
    "Ensemble"
]

UQ_MODES = [
    "uq_aware", 
    # "uq_decompose"
]

BASELINES = [
    "never_retrieve",
    "always_retrieve",
    "granular"
]

OPENAI_BASELINES = [
    "openai_never_retrieve",
    "openai_always_retrieve"
]

OUTPUT_FORMATS = [
    # "--output_format full_response",
    "--output_format label_only"
]

# Define whether to include ACE
LOGIC_STATES = [
    {"args": "--logic_eval_method discrete --check_logic", "logic_on": True},
    {"args": "", "logic_on": False}
]

# --- API overrides for models that require a custom base URL / key env var ---
MODEL_API_OVERRIDES = {
    "qwen3.6": {
        "api_base_url": "https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
        "api_key_env": "DASHSCOPE_API_KEY",
    },
}


def get_model_overrides(model: str) -> str:
    """Return Hydra override string for models that need a custom API endpoint.

    Checks the lowercase model name against the prefixes in MODEL_API_OVERRIDES.
    Returns an empty string for models that use the default OpenAI endpoint.
    """
    model_lower = model.lower()
    for prefix, overrides in MODEL_API_OVERRIDES.items():
        if model_lower.startswith(prefix):
            base_url = overrides["api_base_url"]
            key_env = overrides["api_key_env"]
            return (
                f' llm.api_base_url="{base_url}"'
                f' llm.api_key_env="{key_env}"'
            )
    return ""


def main():
    project_root = Path(__file__).resolve().parents[2]
    job_arrays_dir = project_root / "job_arrays"
    job_arrays_dir.mkdir(exist_ok=True)
    
    calib_commands = {ds["name"]: [] for ds in DATASETS}
    eval_commands = {ds["name"]: [] for ds in DATASETS}
    openai_eval_commands = []
    
    has_openai_models = any(m in OPENAI_MODELS for m in MODELS)

    for seed in SEEDS:
        for model in MODELS:
            api_overrides = get_model_overrides(model)
            is_openai_model = model in OPENAI_MODELS

            for ds in DATASETS:
                dataset_name = ds["name"]
                calib_split = ds["calib_split"]
                test_split = ds["test_split"]

                if is_openai_model:
                    for mode in OPENAI_BASELINES:
                        cmd_eval = (f"--run_type evaluate --dataset {dataset_name} "
                                    f"--model {model} --mode {mode} --test_split {test_split} "
                                    f"--seed {seed} "
                                    f"{OUTPUT_FORMATS[0]}{api_overrides}").strip()
                        openai_eval_commands.append(cmd_eval)
                    continue  # Closed-source models don't support UQ, so skip the rest

                # 1. Generate Baseline Evaluation Jobs
                for mode in BASELINES:
                    cmd_eval = (f"--run_type evaluate --dataset {dataset_name} "
                                f"--model {model} --mode {mode} --test_split {test_split} "
                                f"--seed {seed} "
                                f"{OUTPUT_FORMATS[0]}{api_overrides}").strip()
                    eval_commands[dataset_name].append(cmd_eval)
                    if has_openai_models:
                        openai_eval_commands.append(cmd_eval)

                # 2. Generate UQ & Calibration Jobs for BOTH Logic States
                for logic in LOGIC_STATES:
                    logic_args = logic["args"]
                    is_logic_on = logic["logic_on"]

                    for fmt in OUTPUT_FORMATS:
                        cmd_calib = (f"--run_type calibrate --dataset {dataset_name} "
                                     f"--calibration_split {calib_split} --model {model} "
                                     f"--seed {seed} "
                                     f"{fmt} {logic_args}{api_overrides}").strip()
                        calib_commands[dataset_name].append(cmd_calib)

                    # UQ Evaluation Jobs
                    for uq in UQ_METHODS:

                        # LogicalContradiction requires logic to be ON
                        if uq == "LogicalContradiction" and not is_logic_on:
                            continue

                        # When logic is OFF, only run Ensemble as a comparison baseline.
                        if not is_logic_on and uq != "Ensemble":
                            continue

                        for mode in UQ_MODES:
                            cmd_eval = (f"--run_type evaluate --dataset {dataset_name} "
                                        f"--model {model} --mode {mode} --test_split {test_split} "
                                        f"--uq_method {uq} --calibrated_split {calib_split} "
                                        f"--seed {seed} "
                                        f"{OUTPUT_FORMATS[0]} {logic_args}{api_overrides}").strip()
                            eval_commands[dataset_name].append(cmd_eval)

    for dataset_name in calib_commands.keys():
        if calib_commands[dataset_name]:
            calib_file = job_arrays_dir / f"jobs_array_calib_{dataset_name}.txt"
            with open(calib_file, "w") as f:
                for c in calib_commands[dataset_name]: f.write(c + "\n")
            print(f"✅ Generated {len(calib_commands[dataset_name])} calibration jobs for {dataset_name}.")
                
        if eval_commands[dataset_name]:
            eval_file = job_arrays_dir / f"jobs_array_eval_{dataset_name}.txt"
            with open(eval_file, "w") as f:
                for c in eval_commands[dataset_name]: f.write(c + "\n")
            print(f"✅ Generated {len(eval_commands[dataset_name])} evaluation jobs for {dataset_name}.")

    if openai_eval_commands:
        openai_eval_file = job_arrays_dir / "jobs_array_eval_openai.txt"
        with open(openai_eval_file, "w") as f:
            for c in openai_eval_commands: f.write(c + "\n")
        print(f"✅ Generated {len(openai_eval_commands)} evaluation jobs for OpenAI models in {openai_eval_file.name}.")

if __name__ == "__main__":
    main()