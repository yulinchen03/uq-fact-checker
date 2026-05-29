# Efficient LLM Fact-checking With Uncertainty Quantification

**Author**: Yulin Chen

This repository contains the codebase and experiment code for the UQ-based RAG fact-checking system presented in our paper "Efficient LLM Fact-checking With Uncertainty Quantification" that dynamically decides when to rely on a Large Language Model's (LLM) parametric knowledge and when to trigger external retrieval based on uncertainty quantification (UQ).

## Architecture

The system evaluates claims using several distinct modes:
- **Parametric (0% RAG)**: Answers claims using solely the LLM's internal knowledge without any retrieval.
- **Always Retrieve (100% RAG)**: Always retrieves external evidence (vector database) for every claim.
- **Granular Verification**: Decomposes complex claims into atomic facts and verifies each independently using retrieval.
- **UQ-Aware**: Generates a parametric answer, measures the uncertainty of that generation (using metrics like Mean Token Entropy, Max Sequence Probability, etc.), and triggers retrieval only if uncertainty exceeds a calibrated threshold.
- **UQ Decompose**: Combines UQ-aware selective retrieval with granular decomposition to isolate uncertainty at the atomic fact level. **(Note: This was tested during development, but not used for our final analysis)**

The core pipeline utilizes:
- [**vLLM**](https://vllm.ai/) for high-throughput LLM inference.
- [**lm-polygraph**](https://github.com/IINemo/lm-polygraph) for out-of-the-box uncertainty quantification methods.
- [**ChromaDB**](https://docs.trychroma.com/) & [**SPLADE**](https://huggingface.co/naver/splade-cocondenser-ensembledistil) for hybrid vector/sparse retrieval.
- [**Hydra**](https://hydra.cc/docs/intro/) for flexible configuration management.

## Project Structure

- `src/modules/` - Core components of the pipeline (`retriever.py`, `llm_client.py`, `verifier.py`, `uq_verifier.py`, `granular_verifier.py`, etc.).
- `src/utils/` - Helpers for data loading, threshold calibration, and metrics logging.
- `scripts/analysis/` - Evaluation scripts to generate tables and plots (`analyze_run.py`, `plot_results.py`, etc.).
- `config/` - Hydra configuration files. You can update the default run configs inside this folder.
- `data/` - Stores SciFact and QuanTemp datasets, and vector databases.
- `run_results/` & `results_dump/` - Generated output files and summaries.

## Getting Started

### Prerequisites

Ensure you have a modern Python environment (Python 3.10+ recommended). We recommend using `uv` for fast dependency management.

```bash
# Install dependencies using uv
uv sync
# Install the specific version of transformers and sentence-transformers to avoid errors
uv pip install transformers==4.57.6 sentence-transformers==5.2.3 numpy==1.26.4 torch==2.10.0+cu130
```
Make sure to install the cuda version of torch for your system.

Set up your `.env` file with necessary API keys:
```
OPENAI_API_KEY=your_key_here
```

### Data Preparation

You can use `data_prep/create_subset.py` to make a stratified subset of the current datasets for faster testing and development:

```bash
python data_prep/create_subset.py
```

To initialize and populate the hybrid vector databases (ChromaDB + SPLADE) for retrieval using the dataset corpus files, run:

```bash
python src/utils/populate_db_hybrid.py
```

### Execution

The main entry point for running the pipeline is `scripts/run.py`.

```bash
# Run interactively (will prompt for dataset, mode, etc.)
python scripts/run.py

# Run in headless batch mode using Hydra configuration
python scripts/run.py data=scifact mode=uq_aware output_format=label_only check_logic=True
```

### Batch Execution (SLURM)

To execute experiments across multiple models and splits automatically:
1. Customize `scripts/utils/generate_job_array.py` to manipulate the specific models, datasets, and modes you want to run.
2. Generate the job array files in the `job_arrays/` directory:
   ```bash
   python scripts/utils/generate_job_array.py
   ```
3. Once the codebase is transferred to the cluster according to the instructions in the [HPC Migration Guide](hpc_migration_guide.md), navigate to the project folder on the cluster and start the batch run using the provided Slurm scripts as follows:
```bash
./start_run_scifact.sh
or
./start_run_quantemp.sh
or
./start_run_openai.sh
 ```

## Analysis and Calibration

- **Calibration**: Computes the optimal AUROC threshold on the validation set for UQ methods.
  ```bash
  python src/utils/calibrate_threshold.py
  ```
- **Analysis**: Evaluates the predictions and generates summary JSONs.
  ```bash
  python scripts/analysis/analyze_run.py
  ```
- **Visualization**: Generates detailed results tables and visualizations.
  ```bash
  python scripts/visualization/plot_results.py
  ```

## High Performance Computing (HPC)

For large-scale evaluation on clusters like DAIC, please refer to the [HPC Migration Guide](hpc_migration_guide.md) for instructions on using Apptainer, building `.sif` images, and caching HuggingFace models for offline execution.

### Downloading HuggingFace Models on the Cluster

Since compute nodes often lack internet access and HuggingFace is set to offline mode (`HF_HUB_OFFLINE=1`), you must cache your models on the shared network drive beforehand.

1. Open `download_models.slurm` and uncomment or add the `snapshot_download("model_name")` line for the models you need.
2. Submit the download job from the cluster login node:
   ```bash
   sbatch download_models.slurm
   ```