import json
import random
from collections import Counter, defaultdict
from pathlib import Path
import inquirer

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"

def validate_float(answers, current):
    try:
        val = float(current)
        return 0.0 < val <= 1.0
    except ValueError:
        return False

def get_config():
    questions = [
        inquirer.List('dataset',
                      message="Select the dataset to evaluate",
                      choices=['scifact', 'quantemp']),

        inquirer.List('split',
                      message="Select the data split",
                      choices=['train', 'val', 'test']),

        inquirer.Text('portion',
                      message="Enter the target size of the subset (e.g., 0.1 for 10%)",
                      validate=validate_float,
                      default="0.1"),

        inquirer.Text('name', 
                        message="Enter a name for this subset", 
                        default="subset")
    ]
    return inquirer.prompt(questions)

def get_scifact_label(data: dict) -> str:
    """Extracts the gold label from a SciFact JSON object."""
    evidence = data.get("evidence", {})
    if not evidence:
        return "NOT ENOUGH INFO"
    
    for doc_id, evidences in evidence.items():
        for ev in evidences:
            if "label" in ev:
                return ev["label"]
    return "NOT ENOUGH INFO"

def get_quantemp_label(data: dict) -> str:
    """Extracts the label from a QuAnTemp JSON object."""
    return data.get("label", "UNKNOWN")

def stratify_data(data: list, label_extractor, portion: float) -> list:
    """Groups data by label and samples proportionally."""
    grouped_data = defaultdict(list)
    
    # 1. Group all items by their label
    for item in data:
        label = label_extractor(item)
        grouped_data[label].append(item)
    
    subset = []
    total_target = int(len(data) * portion)
    
    # 2. Sample proportionally from each group
    for label, items in grouped_data.items():
        label_target = int(total_target * (len(items) / len(data)))
        subset.extend(random.sample(items, min(label_target, len(items))))
    
    # 3. Shuffle the final subset so labels aren't clustered together
    random.shuffle(subset)
    return subset

def print_distribution_stats(original_data: list, subset_data: list, label_extractor):
    """Calculates and prints a side-by-side comparison of class distributions."""
    orig_counts = Counter([label_extractor(item) for item in original_data])
    sub_counts = Counter([label_extractor(item) for item in subset_data])
    
    orig_total = len(original_data)
    sub_total = len(subset_data)
    
    print("\n" + "="*55)
    print(f"{'CLASS DISTRIBUTION VERIFICATION':^55}")
    print("="*55)
    print(f"{'Label':<18} | {'Original':<15} | {'Subset':<15}")
    print("-" * 55)
    
    for label, count in orig_counts.most_common():
        orig_pct = (count / orig_total) * 100 if orig_total > 0 else 0
        sub_count = sub_counts.get(label, 0)
        sub_pct = (sub_count / sub_total) * 100 if sub_total > 0 else 0
        
        orig_str = f"{count} ({orig_pct:.1f}%)"
        sub_str = f"{sub_count} ({sub_pct:.1f}%)"
        
        print(f"{label:<18} | {orig_str:<15} | {sub_str:<15}")
        
    print("-" * 55)
    print(f"{'Total':<18} | {orig_total:<15} | {sub_total:<15}\n")

def create_subset():
    config = get_config()
    if not config: return
    
    dataset = config['dataset']
    split = config['split']
    portion = float(config['portion'])
    name = config['name']

    print(f"\nReading {dataset} {split} data...")
    dataset_dir = DATA_DIR / dataset

    if dataset == 'scifact':
        data = []
        input_path = dataset_dir / f"claims_{split}.jsonl"
        output_path = dataset_dir / f"claims_{split}_{name}.jsonl"
        
        with open(input_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    data.append(json.loads(line))
        
        subset = stratify_data(data, get_scifact_label, portion)
        print_distribution_stats(data, subset, get_scifact_label)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for item in subset:
                f.write(json.dumps(item) + '\n')
                
    else:  # quantemp
        input_path = dataset_dir / f"claims_{split}.json"
        
        # --- NEW: Flexible fallback to match loader.py ---
        if not input_path.exists() and (dataset_dir / f"claims_{split}.jsonl").exists():
            input_path = dataset_dir / f"claims_{split}.jsonl"
            
        output_path = dataset_dir / f"claims_{split}_{name}{input_path.suffix}"
        
        data = []
        if input_path.suffix == '.jsonl':
            with open(input_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        data.append(json.loads(line))
        else:
            with open(input_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            data = raw_data if isinstance(raw_data, list) else list(raw_data.values())
        
        subset = stratify_data(data, get_quantemp_label, portion)
        print_distribution_stats(data, subset, get_quantemp_label)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            if output_path.suffix == '.jsonl':
                for item in subset:
                    f.write(json.dumps(item) + '\n')
            else:
                json.dump(subset, f, indent=2)
    
    # Print relative path for a cleaner terminal output
    rel_path = output_path.relative_to(ROOT_DIR)
    print(f"✅ Stratified subset of {len(subset)} items created at {rel_path}")

if __name__ == "__main__":
    create_subset()