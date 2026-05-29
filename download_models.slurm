#!/bin/bash
#SBATCH --job-name=download-hf
#SBATCH --partition=general
#SBATCH --qos=short
#SBATCH --time=00:20:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=8192
#SBATCH --output=logs/download_%j.out
#SBATCH --error=logs/download_%j.err

# 1. Define absolute paths
PROJECT="/tudelft.net/staff-umbrella/YC Thesis Drive/Thesis-Project"
CONTAINER="/tudelft.net/staff-umbrella/YC Thesis Drive/apptainer/thesis_base.sif"

# 2. Ensure cache directories exist on the network drive
mkdir -p "${PROJECT}/.hf_cache"
mkdir -p "${PROJECT}/tmp"

# 3. Execute download using the virtual environment
apptainer exec -C \
    --bind "${PROJECT}:/workspace" \
    --pwd /workspace \
    --env HF_HOME="/workspace/.hf_cache" \
    --env TMPDIR="/workspace/tmp" \
    --env-file "${PROJECT}/.env" \
    "${CONTAINER}" \
    bash -c "source /workspace/.venv/bin/activate && python -c \"
from huggingface_hub import snapshot_download

# snapshot_download('Qwen/Qwen2.5-7B-Instruct')
# snapshot_download('Qwen/Qwen3-4B-Instruct-2507')
# snapshot_download('Qwen/Qwen3-30B-A3B-Instruct-2507')
snapshot_download('Qwen/Qwen3-8B')
# snapshot_download('Qwen/Qwen3.5-9B')
# snapshot_download('Qwen/Qwen3.5-27B')

# snapshot_download('google/gemma-3-4b-it')
# snapshot_download('google/gemma-3-12b-it')
# snapshot_download('google/gemma-4-31B-it')
# snapshot_download('google/gemma-4-26B-A4B-it')

# snapshot_download('meta-llama/Llama-3.1-8B-Instruct')
# snapshot_download('meta-llama/Llama-3.2-3B-Instruct')
# snapshot_download('meta-llama/Llama-3.1-8B')
# snapshot_download('meta-llama/Llama-3.2-3B')

# snapshot_download('mistralai/Mistral-7B-Instruct-v0.3')

# snapshot_download('BAAI/bge-m3')
# snapshot_download('Qwen/Qwen3-Embedding-0.6B')
# snapshot_download('Qwen/Qwen3-Embedding-4B')
# snapshot_download('Qwen/Qwen3-Embedding-8B')
# snapshot_download('Qwen/Qwen3-Reranker-0.6B')
# snapshot_download('Qwen/Qwen3-Reranker-4B')
# snapshot_download('Qwen/Qwen3-Reranker-8B')

# snapshot_download('naver/splade-cocondenser-ensembledistil')

# print('⏳ Downloading Deberta NLI model for Semantic Entropy...')
# snapshot_download('microsoft/deberta-large_mnli')
# print('⏳ Downloading RoBERTa Cross-Encoder...')
# snapshot_download('cross-encoder/stsb-roberta-large')
# print('✅ Download complete!')
\""
