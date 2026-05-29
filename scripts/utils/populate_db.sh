#!/bin/bash
#SBATCH --job-name=pop_db
#SBATCH --partition=insy,general
#SBATCH --qos=short
#SBATCH --time=4:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32768
#SBATCH --gres=gpu:a40:1
#SBATCH --output=logs/pop_db_%j.out
#SBATCH --error=logs/pop_db_%j.err
#SBATCH --mail-type=BEGIN,END

# Default to scifact if no dataset argument is provided
DATASET=${1:-scifact}

PROJECT="/tudelft.net/staff-umbrella/YC Thesis Drive/Thesis-Project"
CONTAINER="/tudelft.net/staff-umbrella/YC Thesis Drive/apptainer/thesis_base.sif"
HF_CACHE="/tudelft.net/staff-umbrella/YC Thesis Drive/Thesis-Project/.hf_cache"

mkdir -p "${PROJECT}/tmp"
mkdir -p "${PROJECT}/logs"

echo "=========================================================="
echo "🚀 Populating DB for Dataset: $DATASET"
echo "=========================================================="

# HF_HUB_OFFLINE is set to 0 here to allow downloading embedding models 
# if they are not already in the cache.
apptainer exec --nv -C \
    --bind "${PROJECT}:/workspace" \
    --bind "${HF_CACHE}:/hf_cache" \
    --pwd /workspace \
    --env HF_HOME="/hf_cache" \
    --env HF_HUB_OFFLINE=0 \
    --env TMPDIR="/workspace/tmp" \
    --env PYTHONPATH=/workspace \
    "${CONTAINER}" \
    bash -c "source /workspace/.venv/bin/activate && \
             python -m src.utils.populate_db_hybrid data=$DATASET"
