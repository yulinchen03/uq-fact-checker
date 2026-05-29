#!/bin/bash
set -e

# 1. Count jobs
NUM_EVAL=$(wc -l < job_arrays/jobs_array_eval_openai.txt)

# 2. Submit Evaluation Array
echo "⏳ Submitting Evaluation Array Job..."
ARRAY_ID=$(sbatch --parsable --array=1-$NUM_EVAL scripts/utils/submit_eval_jobs_openai.sh)
echo "✅ Evaluation Array Queued with ID: $ARRAY_ID"

echo ""
echo "🎉 All jobs deployed! Check 'squeue -u <your_username>' to monitor."