#!/bin/bash
#SBATCH --job-name=calib
#SBATCH --partition=insy,general
#SBATCH --qos=short
#SBATCH --time=4:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=32768
#SBATCH --gres=gpu:a40:1
#SBATCH --output=logs/calib_%A_%a.out
#SBATCH --error=logs/calib_%A_%a.err
#SBATCH --mail-type=BEGIN,END

PROJECT="/tudelft.net/staff-umbrella/YC Thesis Drive/Thesis-Project"
CONTAINER="/tudelft.net/staff-umbrella/YC Thesis Drive/apptainer/thesis_base.sif"
HF_CACHE="/tudelft.net/staff-umbrella/YC Thesis Drive/Thesis-Project/.hf_cache"

mkdir -p "${PROJECT}/tmp"
mkdir -p "${PROJECT}/logs"

TASK_CACHE="${PROJECT}/.global_cache/task_${SLURM_ARRAY_TASK_ID}"
LOCAL_CACHE="/tmp/torchinductor_${SLURM_ARRAY_TASK_ID}"
mkdir -p "${TASK_CACHE}"
mkdir -p "${LOCAL_CACHE}"

# --- ORPHAN STATE PREVENTION: Graceful Teardown Trap ---
cleanup() {
    echo -e "\n🛑 Caught exit signal or script ended. Executing graceful teardown..."
    
    # 1. Kill all child processes attached to this script (Apptainer -> vLLM)
    pkill -TERM -P $$
    
    # 2. Clean up local and global caches
    echo "🧹 Removing isolated cache folders..."
    rm -rf "${TASK_CACHE}"
    rm -rf "${LOCAL_CACHE}"
    
    echo "✅ Teardown complete. Exiting safely."
}
# Bind the cleanup function to trigger on success, crash, or SLURM cancel
trap cleanup EXIT INT TERM SIGINT SIGTERM
# -------------------------------------------------------

# Read the specific line from the CALIBRATION array
ARGS=$(sed -n "${SLURM_ARRAY_TASK_ID}p" "${PROJECT}/job_arrays/jobs_array_calib_scifact.txt")

DATASET=$(echo $ARGS | awk -F'--dataset ' '{print $2}' | awk '{print $1}')
MODEL=$(echo $ARGS | awk -F'--model ' '{print $2}' | awk '{print $1}')
SEED=$(echo $ARGS | awk -F'--seed ' '{print $2}' | awk '{print $1}')

echo "=========================================================="
echo "🚀 Calibration Array Task ID: $SLURM_ARRAY_TASK_ID"
echo "⚙️  Executing: $ARGS"
echo "🎯 Extracted Target -> Dataset: $DATASET | Model: $MODEL | Seed: $SEED"
echo "📁 Using Isolated Cache: ${TASK_CACHE}"
echo "=========================================================="

apptainer exec --nv -C \
    --bind "${PROJECT}:/workspace" \
    --bind "${HF_CACHE}:/hf_cache" \
    --pwd /workspace \
    --env HF_HOME="/hf_cache" \
    --env HF_HUB_OFFLINE=1 \
    --env TMPDIR="/workspace/tmp" \
    --env XDG_CACHE_HOME="/workspace/.global_cache/task_${SLURM_ARRAY_TASK_ID}" \
    --env PYTHONPATH=/workspace \
    "${CONTAINER}" \
    bash -c "source /workspace/.venv/bin/activate && \
             python /workspace/scripts/batch_run.py $ARGS && \
             echo -e '\n==========================================================' && \
             echo '📊 Generating/Updating Markdown Summary...' && \
             echo '==========================================================' && \
             python /workspace/src/utils/summarize_calibrations.py --dataset $DATASET --model $MODEL --seed $SEED"