import inspect
import json
from collections import Counter
import hydra
import lm_polygraph.estimators as estimators
import inquirer
from omegaconf import DictConfig

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
                      choices=['never_retrieve', 'always_retrieve', 'uq_aware', 'calibration']),

        inquirer.List('split',
                      message="Select the data split",
                      choices=['train', 'val', 'test']),
        
        inquirer.List('uq_method',
                      message="Select the UQ Method for this run",
                      choices=available_estimators,
                      ignore=lambda answers: answers['mode'] != 'uq_aware' and answers['mode'] != 'calibration'),
    ]

    return inquirer.prompt(questions)

@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg: DictConfig):
    config = get_config()
    dataset = config['dataset']
    mode = config['mode']
    split = config['split'] if 'split' in config else 'N/A'
    uq_method = config.get('uq_method', 'N/A')
    model_name = cfg.llm.model_name.split("/")[1]

    # Construct the path to the results file based on the selected configuration
    if mode == 'uq_aware':
        results_path = f"results/RQ1/{dataset}/{model_name}/{mode}/{uq_method}/results_{split}.jsonl"
    elif mode == 'calibration':
        results_path = f"results/RQ1/{dataset}/{model_name}/calibration/{uq_method}/results_val.jsonl"
    else:   
        results_path = f"results/RQ1/{dataset}/{model_name}/{mode}/results_{split}.jsonl"
    print(results_path)

    # Initialize counters
    gold_labels = Counter()
    predicted_verdicts = Counter()

    # Open and read the JSONL file
    with open(results_path, 'r') as file:
        for line in file:
            if line.strip(): # Skip empty lines
                data = json.loads(line)
                
                # Extract values, using .get() to avoid errors if a key is missing
                gold_labels[data.get('gold_label')] += 1
                predicted_verdicts[data.get('predicted_verdict')] += 1

    # Display the results
    print("--- Gold Labels ---")
    for label, count in gold_labels.items():
        print(f"{label}: {count}")

    print("\n--- Predicted Verdicts ---")
    for verdict, count in predicted_verdicts.items():
        print(f"{verdict}: {count}")

if __name__ == "__main__":
    main()