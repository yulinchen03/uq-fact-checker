import json
from collections import Counter

# Adjust path if necessary
file_path = "results/RQ1/quantemp/always_retrieve/results_val.jsonl"

preds = []
with open(file_path, 'r') as f:
    for line in f:
        try:
            data = json.loads(line)
            # Grab the raw prediction
            pred = data.get("predicted_verdict", "MISSING").strip()
            preds.append(pred)
        except:
            continue

print("--- Raw Prediction Distribution ---")
# This prints the count of every unique prediction string
for label, count in Counter(preds).most_common():
    print(f"{label}: {count}")