# Migrating to DAIC HPC Cluster with Apptainer

## How It Works

Based on the [DAIC Apptainer tutorial](https://daic.tudelft.nl/tutorials/apptainer/), the workflow is:

1. **Write a `.def` file** — specifies base image + all your dependencies based on your exact [requirements_hpc.txt](file:///home/yulinchen/Desktop/Thesis-Project/requirements_hpc.txt).
2. **Build locally** → produces a `.sif` image (single portable file).
3. **Transfer** the `.sif` to DAIC via `scp`.
4. **Run on DAIC** with `apptainer exec --nv` + `--bind` mounts for your data/results.

> [!IMPORTANT]
> Your **code, data, and results stay OUTSIDE the container** (mounted at runtime). The container only holds the **runtime environment** (Python, CUDA, pip packages). This means you can update your scripts without rebuilding.

## Architecture & Offline HPC Adjustments

Compute nodes on HPC clusters often **do not have internet access**. Because your pipeline uses `vllm.LLM()` and `SentenceTransformer()` which try to download models from HuggingFace, we must ensure:
1. The models are downloaded **once** into a shared cache folder (e.g., from the login node, or locally and transferred).
2. The cache folder is **bind-mounted** into the container.
3. The environment variable `HF_HUB_OFFLINE=1` is set during batch runs to prevent timeout crashes when nodes try to phone home.

## Step 1: Create the Exact Requirements File

Create [requirements_hpc.txt](file:///home/yulinchen/Desktop/Thesis-Project/requirements_hpc.txt) in your repo root (this matches your `uv pip list` output). See the project root for the file.

## Step 2: Create the Definition File

Create `thesis_project.def` in your repo root:

```def
Bootstrap: docker
From: nvidia/cuda:12.4.0-devel-ubuntu22.04

%files
    requirements_hpc.txt /opt/thesis/requirements_hpc.txt

%post
    # System dependencies
    apt-get update && apt-get install -y \
        git curl build-essential \
        && apt-get clean && rm -rf /var/lib/apt/lists/*

    # Install uv (fast Python package manager)
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="/root/.local/bin:$PATH"

    cd /opt/thesis

    # Install exact Python dependencies using uv (it will fetch Python 3.12 automatically)
    uv venv /opt/thesis/.venv --python 3.12
    VIRTUAL_ENV=/opt/thesis/.venv uv pip install -r requirements_hpc.txt \
        --index-strategy unsafe-best-match \
        --extra-index-url https://download.pytorch.org/whl/cu124

    # Activate venv by default when container starts
    echo 'export PATH="/opt/thesis/.venv/bin:$PATH"' >> $APPTAINER_ENVIRONMENT
    echo 'export VIRTUAL_ENV="/opt/thesis/.venv"' >> $APPTAINER_ENVIRONMENT
    echo 'export PYTHONPATH="/workspace:$PYTHONPATH"' >> $APPTAINER_ENVIRONMENT

%runscript
    cd /workspace
    exec python "$@"
```

> [!WARNING]
> Verify the CUDA version matches what DAIC provides. Check with `nvidia-smi` on the cluster. The PyTorch wheel index URL (`cu124`) should also match. Currently your environment uses `cu130`, but `nvidia/cuda:12.4.0` is safer for enterprise clusters.

## Step 3: Build & Transfer

```bash
# On your local machine
apptainer build thesis_project.sif thesis_project.def

# Transfer image
scp thesis_project.sif yulinchen@login.daic.tudelft.nl:/tudelft.net/staff-umbrella/YC\ Thesis\ Drive/apptainer/

# Transfer project codebase
rsync -avz --progress --no-perms --no-owner --no-group \
    --exclude='.venv' --exclude='outputs' --exclude='.git' \
    --exclude='QuanTemp' --exclude='vis' --exclude='*oneshot_prompt.yaml' \
    --exclude='demo_risk_bound_calculation.py' --exclude='get_prediction_labels.py' --exclude='test_factscore.py' \
    --exclude='thesis_project.sif' --exclude='data/vector_db' \
    --exclude='data/scifact/cross_validation' --exclude='results' \
    --exclude='__pycache__' --exclude='src/demos' --exclude='src/notebooks' \ --exlcude='thesis_base.def' --exclude='thesis_base.sif' --exclude='src/SeSE' \
    --exclude='.gitignore' --exclude='LICENSE.txt' --exclude='README.md' \
    --exclude='hpc_migration_guide.md' --exclude='pyproject.toml' --exclude='uv.lock' \
    ~/Desktop/Thesis-Project/ \
    yulinchen@login.daic.tudelft.nl:/tudelft.net/staff-umbrella/YC\ Thesis\ Drive/Thesis-Project/
```

## Step 4: Download Models to Cache (Important for offline compute)

Before submitting batch jobs, you must populate the HuggingFace cache. SSH into the login node (which usually has internet) and run:

```bash
#!/bin/sh
#SBATCH --job-name=download-hf
#SBATCH --partition=general
#SBATCH --qos=short
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=8192
#SBATCH --output=logs/download_%j.out
#SBATCH --error=logs/download_%j.err

apptainer exec -C \
    --bind "/tudelft.net/staff-umbrella/YC Thesis Drive/Thesis-Project:/workspace" \
    --bind "/tudelft.net/staff-umbrella/YC Thesis Drive/.cache/huggingface:/hf_cache" \
    --env HF_HOME="/hf_cache" \
    "/tudelft.net/staff-umbrella/YC Thesis Drive/apptainer/thesis_project.sif" \
    python -c "from huggingface_hub import snapshot_download; snapshot_download('Qwen/Qwen3-4B-Instruct-2507'); snapshot_download('BAAI/bge-m3')"
```
*(Replace `gte-base-en-v1.5` with whatever embedding model you use in `retriever.py`)*

## Step 5: SLURM Batch Script

Create `run_batch.slurm`:

```bash
#!/bin/bash
#SBATCH --job-name=thesis-rq1
#SBATCH --partition=general,insy
#SBATCH --qos=long
#SBATCH --time=12:00:00
#SBATCH --gres=gpu:1
#SBATCH --mem=32768
#SBATCH --cpus-per-task=4
#SBATCH --output=logs/slurm-%j.out
#SBATCH --error=logs/slurm-%j.err

# Paths
CONTAINER="/tudelft.net/staff-umbrella/YC Thesis Drive/apptainer/thesis_project.sif"
PROJECT="/tudelft.net/staff-umbrella/YC Thesis Drive/Thesis-Project"
HF_CACHE="/tudelft.net/staff-umbrella/YC Thesis Drive/.cache/huggingface"

mkdir -p logs

# Run the batch experiment with HF_HUB_OFFLINE=1
apptainer exec --nv -C \
    --bind "${PROJECT}:/workspace" \
    --bind "${HF_CACHE}:/root/.cache/huggingface" \
    --env HF_HUB_OFFLINE=1 \
    --env-file "${PROJECT}/.env" \
    --env PYTHONPATH=/workspace \
    "${CONTAINER}" \
    python /workspace/batch_run_rq1.py
```

### Key fixes applied:
1. **`HF_HUB_OFFLINE=1`**: Prevents `vllm` and `SentenceTransformer` from attempting to connect to huggingface.co on compute nodes. They will strictly load from the bind-mounted `/root/.cache/huggingface`.
2. **[requirements_hpc.txt](file:///home/yulinchen/Desktop/Thesis-Project/requirements_hpc.txt)**: The `.def` file now entirely bypasses `pyproject.toml` and perfectly replicates your local working state.

## Step 6: Populating ChromaDB via Slurm

Because the `data/vector_db/` directory is massive (nearly 1GB), it is excluded from the `rsync` transfer. Instead of uploading gigabytes of SQLite files and potentially corrupting the database across OS architectures, we recreate the database natively on the cluster using a dedicated batch job.

The `src/utils/populate_db.py` script has been updated so that when ran non-interactively, it cleanly bypasses the `inquirer` prompt and reads the target dataset directly from Hydra configurations.

Create `populate_db.slurm`:

```bash
#!/bin/sh
#SBATCH --job-name=thesis-populate-db
#SBATCH --partition=general
#SBATCH --qos=short          # 'short' is for jobs 4 hours or less
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4    # DAIC requires even numbers
#SBATCH --mem=32768          # 32GB
#SBATCH --gres=gpu:1         # Request GPU on the general partition
#SBATCH --output=logs/populate_%j.out
#SBATCH --error=logs/populate_%j.err

CONTAINER="/tudelft.net/staff-umbrella/YC Thesis Drive/apptainer/thesis_project.sif"
PROJECT="/tudelft.net/staff-umbrella/YC Thesis Drive/Thesis-Project"
HF_CACHE="/tudelft.net/staff-umbrella/YC Thesis Drive/.cache/huggingface"

# Submit one job per dataset by changing +data=scifact to +data=quantemp
apptainer exec --nv -C \
    --bind "${PROJECT}:/workspace" \
    --bind "${HF_CACHE}:/hf_cache" \
    --env HF_HOME="/hf_cache" \
    --env HF_HUB_OFFLINE=1 \
    --env PYTHONPATH=/workspace \
    "${CONTAINER}" \
    python /workspace/src/utils/populate_db.py +data=scifact
```

Run this with `sbatch populate_db.slurm`. Once completed, you can repeat the process by changing `+data=scifact` to `+data=quantemp` to build the other database on the DAIC natively.
