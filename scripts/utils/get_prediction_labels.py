import inspect
import json
from collections import Counter
from pathlib import Path
import hydra
import lm_polygraph.estimators as estimators
import inquirer
from omegaconf import DictConfig

ROOT_DIR = Path(__file__).resolve().parents[2]

def get_config():

    available_estimators = [
        name for name, obj in inspect.getmembers(estimators, inspect.isclass)
    ]

    questions = [
        inquirer.List('dataset',
                      message="Select the dataset",
                      choices=['scifact', 'quantemp']),

        inquirer.List('mode',
                      message="Select the experimental mode",
                      choices=['never_retrieve', 'always_retrieve', 'uq_aware', 'uq_decompose', 'factscore', 'calibration']),

        inquirer.List('split',
                      message="Select the data split",
                      choices=['train', 'val', 'test']),
        
        inquirer.List('uq_method',
                      message="Select the UQ Method for this run",
                      choices=available_estimators,
                      ignore=lambda answers: answers['mode'] not in ('uq_aware', 'uq_decompose', 'calibration')),
    ]

    return inquirer.prompt(questions)


@hydra.main(version_base=None, config_path="../../config", config_name="config")
def main(cfg: DictConfig):
    config = get_config()
    if not config: 
        return
        
    dataset = config['dataset']
    mode = config['mode']
    split = config['split'] if 'split' in config else 'N/A'
    uq_method = config.get('uq_method', 'N/A')
    model_name = cfg.llm.model_name.split("/")[1]

    base_results = ROOT_DIR / "results" / "RQ1" / dataset / model_name
    
    if mode in ('uq_aware', 'uq_decompose'):
        results_path = base_results / mode / uq_method / f"results_{split}.jsonl"
    elif mode == 'calibration':
        results_path = base_results / "calibration" / uq_method / "results_val.jsonl"
    else:   
        results_path = base_results / mode / f"results_{split}.jsonl"
        
    # Print clean relative path for terminal readability
    rel_path = results_path.relative_to(ROOT_DIR) if results_path.is_relative_to(ROOT_DIR) else results_path
    print(f"\n📂 Reading from: {rel_path}")

    # Add a safety check before trying to open it
    if not results_path.exists():
        print(f"❌ Error: File not found. Make sure you have run the {mode} pipeline for {dataset} first!")
        return

    # Initialize counters
    gold_labels = Counter()
    predicted_verdicts = Counter()

    # Open and read the JSONL file
    with open(results_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip(): # Skip empty lines
                data = json.loads(line)
                
                # Extract values, using .get() to avoid errors if a key is missing
                gold_labels[data.get('gold_label')] += 1
                predicted_verdicts[data.get('predicted_verdict')] += 1

    # Display the results
    print("\n--- Gold Labels ---")
    for label, count in gold_labels.items():
        print(f"{label}: {count}")

    print("\n--- Predicted Verdicts ---")
    for verdict, count in predicted_verdicts.items():
        print(f"{verdict}: {count}")

if __name__ == "__main__":
    main()