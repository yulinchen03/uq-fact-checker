#!/bin/bash
set -e

# 1. Count jobs
NUM_CALIB=$(wc -l < job_arrays/jobs_array_calib_scifact.txt)
NUM_EVAL=$(wc -l < job_arrays/jobs_array_eval_scifact.txt)

if [ "$NUM_CALIB" -eq 0 ] || [ "$NUM_EVAL" -eq 0 ]; then
    echo "❌ Error: One of the array files is empty. Aborting."
    exit 1
fi
echo "📋 Found $NUM_CALIB calibration jobs and $NUM_EVAL evaluation jobs."

# 2. Submit Calibration Array
# echo "⏳ Submitting Calibration Array Job..."
# CALIB_ID=$(sbatch --parsable --array=1-$NUM_CALIB scripts/utils/submit_calib_jobs_scifact.sh)
# echo "✅ Calibration Array Queued with ID: $CALIB_ID"

# 3. Submit Evaluation Array with Dependency
echo "⏳ Submitting Evaluation Array Job..."
# ARRAY_ID=$(sbatch --parsable --dependency=afterok:$CALIB_ID --array=1-$NUM_EVAL scripts/utils/submit_eval_jobs_scifact.sh)
ARRAY_ID=$(sbatch --parsable --array=1-$NUM_EVAL scripts/utils/submit_eval_jobs_scifact.sh)
echo "✅ Evaluation Array Queued with ID: $ARRAY_ID (Waiting for $CALIB_ID to finish)"

echo ""
echo "🎉 All jobs deployed! Check 'squeue -u <your_username>' to monitor."