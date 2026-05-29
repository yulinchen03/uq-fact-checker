#!/bin/bash
#SBATCH --job-name=eval
#SBATCH --partition=insy,general
#SBATCH --qos=short
#SBATCH --time=4:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=32768
#SBATCH --gres=gpu:a40:1
#SBATCH --output=logs/eval_%A_%a.out
#SBATCH --error=logs/eval_%A_%a.err
#SBATCH --mail-type=BEGIN,END

PROJECT="/tudelft.net/staff-umbrella/YC Thesis Drive/Thesis-Project"
CONTAINER="/tudelft.net/staff-umbrella/YC Thesis Drive/apptainer/thesis_base.sif"
HF_CACHE="/tudelft.net/staff-umbrella/YC Thesis Drive/Thesis-Project/.hf_cache"

# --- Load environment variables (API keys, etc.) from .env ---
if [ -f "${PROJECT}/.env" ]; then
    set -a
    source "${PROJECT}/.env"
    set +a
    echo "✅ Loaded .env from ${PROJECT}/.env"
else
    echo "⚠️  WARNING: .env file not found at ${PROJECT}/.env — API keys may be missing!"
fi

mkdir -p "${PROJECT}/logs"

# --- Create a unique cache folder for THIS specific evaluation task! ---
TASK_CACHE="${PROJECT}/.global_cache/eval_job_${SLURM_ARRAY_JOB_ID}_task_${SLURM_ARRAY_TASK_ID}"
mkdir -p "${TASK_CACHE}"

# --- ORPHAN STATE PREVENTION: Graceful Teardown Trap ---
cleanup() {
    echo -e "\n🛑 Caught exit signal or script ended. Executing graceful teardown..."
    
    # 1. Kill all child processes attached to this script (Apptainer -> vLLM)
    pkill -TERM -P $$
    
    # 2. Clean up global caches (SLURM handles $TMPDIR automatically, but we clear XDG)
    echo "🧹 Removing isolated cache folders..."
    rm -rf "${TASK_CACHE}"
    
    # 3. Clean up the SLURM scratch copy of ChromaDB
    echo "🧹 Removing scratch Vector DB..."
    rm -rf "${TMPDIR}/vector_db_${SLURM_ARRAY_TASK_ID}"
    
    echo "✅ Teardown complete. Exiting safely."
}
# Bind the cleanup function to trigger on success, crash, or SLURM cancel
trap cleanup EXIT INT TERM SIGINT SIGTERM
# -------------------------------------------------------

# Read the specific line from the EVALUATION array
ARGS=$(sed -n "${SLURM_ARRAY_TASK_ID}p" "${PROJECT}/job_arrays/jobs_array_eval_openai.txt")

echo "=========================================================="
echo "🚀 Evaluation Array Task ID: $SLURM_ARRAY_TASK_ID"
echo "⚙️  Executing: $ARGS"
echo "📁 Using Isolated Cache: ${TASK_CACHE}"
echo "=========================================================="

apptainer exec --nv -C \
    --bind "${PROJECT}:/workspace" \
    --bind "${HF_CACHE}:/hf_cache" \
    --bind "${TMPDIR}:${TMPDIR}" \
    --pwd /workspace \
    --env HF_HOME="/hf_cache" \
    --env HF_HUB_OFFLINE=1 \
    --env XDG_CACHE_HOME="/workspace/.global_cache/eval_task_${SLURM_ARRAY_TASK_ID}" \
    --env PYTHONPATH=/workspace \
    --env OPENAI_API_KEY="${OPENAI_API_KEY}" \
    --env DASHSCOPE_API_KEY="${DASHSCOPE_API_KEY}" \
    "${CONTAINER}" \
    bash -c "source /workspace/.venv/bin/activate && \
             export DB_DEST=\"${TMPDIR}/vector_db_${SLURM_ARRAY_TASK_ID}\" && \
             echo \"📂 Copying ChromaDB to SLURM local scratch at \${DB_DEST}...\" && \
             rm -rf \"\${DB_DEST}\" && \
             cp -r /workspace/data/vector_db \"\${DB_DEST}\" && \
             echo '🚀 Starting Evaluation...' && \
             python /workspace/scripts/batch_run.py $ARGS retriever.db_path=\"\${DB_DEST}\" && \
             echo '⏳ Pausing for 10 seconds to flush VRAM...' && \
             sleep 10"

# --- PROGRESS LOGGING ---
# Appends the SLURM job ID and arguments to progress.txt upon job completion.
printf '{"job_id": "%s", "array_task_id": "%s", "args": "%s"}\n' "${SLURM_JOB_ID}" "${SLURM_ARRAY_TASK_ID}" "${ARGS}" >> "${PROJECT}/progress.txt"