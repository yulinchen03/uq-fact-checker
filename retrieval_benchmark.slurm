#!/bin/bash
#SBATCH --job-name=thesis-benchmark
#SBATCH --partition=general,insy
#SBATCH --qos=medium          # 'short' is for jobs 4 hours or less
#SBATCH --time=7:00:00      # 8 hours should be plenty for the validation split
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4    # DAIC requires even numbers
#SBATCH --mem=65536          # 64GB RAM
#SBATCH --mail-type=BEGIN,END
#SBATCH --gres=gpu:a40:1            # Request 1 GPU of any type
#SBATCH --constraint=gpumem32   # Restrict to GPUs with ≥32 GB VRAM
#SBATCH --output=logs/benchmark_%j.out
#SBATCH --error=logs/benchmark_%j.err

tmpdir="/tmp/${USER}/${SLURM_JOBID}" # Create local temporary folder
mkdir --parents "$tmpdir"

function clean_up { # Cleanup temporary folder
    rm --recursive --force "$tmpdir" && echo "Clean up of $tmpdir completed successfully."
    exit
}
trap 'clean_up' EXIT

# 1. Define absolute paths
PROJECT="/tudelft.net/staff-umbrella/YC Thesis Drive/Thesis-Project"
CONTAINER="/tudelft.net/staff-umbrella/YC Thesis Drive/apptainer/thesis_base.sif"
HF_CACHE="/tudelft.net/staff-umbrella/YC Thesis Drive/Thesis-Project/.hf_cache"

# 2. Pre-create safe tmp directories
mkdir -p "${PROJECT}/tmp"
mkdir -p "${PROJECT}/.global_cache"
mkdir -p "${PROJECT}/logs"

# 3. Execute the master benchmark with virtual environment activation
echo "🚀 Starting Master Architecture Benchmark (41 Configurations)..."

apptainer exec --nv -C \
    --bind "${PROJECT}:/workspace" \
    --bind "${HF_CACHE}:/hf_cache" \
    --pwd /workspace \
    --env HF_HOME="/hf_cache" \
    --env HF_HUB_OFFLINE=1 \
    --env TMPDIR="/workspace/tmp" \
    --env XDG_CACHE_HOME="/workspace/.global_cache" \
    --env PYTHONPATH=/workspace \
    "${CONTAINER}" \
    bash -c "source /workspace/.venv/bin/activate && \
python /workspace/benchmark_retrieval.py \
    --dataset scifact \
    --split val \
    --top-k 1 2 3 \
    --save-results-folder retrieval_experiment"

echo "Benchmark job finished!"
