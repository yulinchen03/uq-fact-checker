# DAIC HPC Cluster Migration & Operation Manual

This guide provides step-by-step instructions for migrating the thesis project codebase to the DAIC High-Performance Computing cluster, running jobs interactively or via SLURM, and transferring results back.

## 1. Building and Transferring to DAIC

Before running on the cluster, you need to build the Apptainer `.sif` image locally and then transfer both the codebase and the image.

### Build the Apptainer Image
The repository includes a `thesis_base.def` file that defines the container environment. Build the image locally using:
```bash
apptainer build thesis_base.sif thesis_base.def
```

### Transfer Project Codebase
Use `rsync` from your local machine to sync the repository to the cluster, excluding unnecessary files and caches:
```bash
rsync -avz --progress --no-perms --no-owner --no-group \
    --exclude='.venv' --exclude='outputs' --exclude='.git' \
    --exclude='QuanTemp' --exclude='visualizations' \
    --exclude='results_dump' \
    --exclude='data/vector_db' --exclude='data/quantemp/corpus.json' \
    --exclude='data/scifact/cross_validation' \
    --exclude='results'  --exclude='openai_results' \
    --exclude='__pycache__' --exclude='src/__pycache__' \
    --exclude='thesis_base.def' --exclude='thesis_base.sif' \
    --exclude='.gitignore' --exclude='README.md' \
    --exclude='hpc_migration_guide.md' --exclude='pyproject.toml' --exclude='uv.lock' --exclude='run_results/' \
    /path/to/local/project/ \
    <username>@<cluster_address>:<path_to_project_root>/
```

### Transfer and Deploy the Apptainer Image
Transfer the pre-built Apptainer image to the cluster using `scp`:
```bash
scp thesis_base.sif <username>@<cluster_address>:<path_to_project_root>/apptainer/
```
*Note: Once transferred, this `.sif` file is "deployed" as your complete, isolated runtime environment. You will reference its path whenever launching interactive sessions or SLURM batch jobs (as shown in the following sections).*

---

## 2. Accessing the DAIC Cluster

1. SSH into DAIC:
   ```bash
   ssh <username>@<cluster_address>
   ```
2. Navigate to the project directory:
   ```bash
   cd "<path_to_project_root>"
   ```

---

## 3. Interactive Run (For Debugging)

For debugging and short tests, start an interactive SLURM session and enter the Apptainer shell.

### Step 1: Request an Interactive Node
```bash
sinteractive --partition=general,insy --qos=medium --time=12:00:00 --cpus-per-task=4 --mem=32768 --gres=gpu:1
```

### Step 2: Launch Apptainer Shell
Once the interactive node is allocated, start the container:
```bash
apptainer shell --nv -C \
    --bind "<path_to_project_root>/workspace" \
    --bind "<path_to_project_root>/.hf_cache:/hf_cache" \
    --pwd /workspace \
    --env HF_HOME="/hf_cache" \
    --env HF_HUB_OFFLINE=1 \
    --env TMPDIR="/workspace/.tmp" \
    --env UV_CACHE_DIR="/workspace/.uv_cache" \
    --env-file "<path_to_project_root>/.env" \
    --env PYTHONPATH=/workspace \
    "<path_to_project_root>/apptainer/thesis_base.sif"
```

### Optional: Add Missing Dependencies via `uv`
If you need to install missing packages while inside the interactive Apptainer shell:
```bash
export PATH="/workspace/.local/bin:$PATH"
source /workspace/.venv/bin/activate
uv pip install <your-missing-dependency>
```

---

## 4. Slurm Batch Run (Automated)

For long-running evaluation scripts, submit jobs to the SLURM queue.

1. **Create a SLURM script** (e.g., `name.slurm`).
2. **Submit the job**:
   ```bash
   sbatch name.slurm
   ```
3. **Check job status**:
   ```bash
   squeue -u <username>
   ```
4. **View live logs**:
   Logs are typically saved in the `logs/` directory.
   ```bash
   tail -f logs/<JOB_NAME>_<JOB_ID>_<TASK_ID>.out
   ```
5. **Cancel a job** (if necessary):
   ```bash
   scancel <job_id>
   ```

---

## 5. Transferring Results Back to Local

After experiments finish, transfer the results directory back to your local machine:
```bash
scp -r <username>@<cluster_address>:"<path_to_project_root>/run_results" /path/to/local/project/
```
