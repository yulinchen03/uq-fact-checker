import json
import glob
from pathlib import Path

def get_best_model_examples(dataset, split="test"):
    search_path = f'/home/yulinchen/Desktop/Thesis-Project/results_dump/final/{dataset}/*/uq_aware/Ensemble/results_{split}_label_only_logic_discrete.jsonl'
    files = glob.glob(search_path)
    
    if not files:
        # Fallback to val if test doesn't exist (e.g. scifact calibration)
        search_path = f'/home/yulinchen/Desktop/Thesis-Project/results_dump/final/{dataset}/*/uq_aware/Ensemble/results_val_label_only_logic_discrete.jsonl'
        files = glob.glob(search_path)
        if not files:
            return None, None, None
            
    best_file = None
    best_scenarios = None
    
    for file_path in files:
        s1, s2, s3, s4 = [], [], [], []
        with open(file_path, 'r') as f:
            for line in f:
                d = json.loads(line)
                gold = d.get('gold_label', '')
                parametric = d.get('parametric_verdict', '')
                predicted = d.get('predicted_verdict', '')
                flagged = d.get('uq_flagged', False)
                
                if "NOT ENOUGH INFO" in [gold, parametric, predicted] or "Conflicting" in [gold, parametric, predicted]:
                    continue
                
                if parametric != gold and flagged and predicted == gold: s1.append(d)
                elif parametric == gold and not flagged and predicted == gold: s2.append(d)
                elif parametric != gold and not flagged: s3.append(d)
                elif parametric == gold and flagged and predicted != gold: s4.append(d)

        if s1 and s2 and s3 and s4:
            best_file = file_path
            best_scenarios = (s1, s2, s3, s4)
            break
            
    if not best_file:
        best_file = files[0]
        s1, s2, s3, s4 = [], [], [], []
        with open(best_file, 'r') as f:
            for line in f:
                d = json.loads(line)
                gold = d.get('gold_label', '')
                parametric = d.get('parametric_verdict', '')
                predicted = d.get('predicted_verdict', '')
                flagged = d.get('uq_flagged', False)
                if "NOT ENOUGH INFO" in [gold, parametric, predicted] or "Conflicting" in [gold, parametric, predicted]: continue
                if parametric != gold and flagged and predicted == gold: s1.append(d)
                elif parametric == gold and not flagged and predicted == gold: s2.append(d)
                elif parametric != gold and not flagged: s3.append(d)
                elif parametric == gold and flagged and predicted != gold: s4.append(d)
        best_scenarios = (s1, s2, s3, s4)

    model_name = Path(best_file).parents[2].name
    threshold = "N/A"
    t_files = glob.glob(f'/home/yulinchen/Desktop/Thesis-Project/results_dump/final/{dataset}/{model_name}/calibration/optimal_thresholds_*_label_only_logic_discrete.json')
    if t_files:
        with open(t_files[0], 'r') as tf:
            t_data = json.load(tf)
            th = t_data.get('Ensemble', {}).get('optimal_threshold', 'N/A')
            if isinstance(th, float): threshold = f"{th:.4f}"
            
    return best_scenarios, threshold, dataset.capitalize()

def format_latex_example(ex, threshold, dataset_name):
    if not ex:
        return f"\\textbf{{[{dataset_name}]}} No example found.\\\\\n"
    
    claim = ex.get('claim', '').replace('&', '\\&').replace('%', '\\%').strip('"')
    gold = ex.get('gold_label', '').upper()
    param = ex.get('parametric_verdict', '').upper()
    pred = ex.get('predicted_verdict', '').upper()
    score = ex.get('uq_scores', {}).get('Ensemble', 'N/A')
    if isinstance(score, float): score = f"{score:.4f}"
    
    param_correct = "\\textit{Correct}" if param == gold else "\\textit{Incorrect}"
    pred_correct = "\\textit{Correct}" if pred == gold else "\\textit{Incorrect}"
    
    flagged = ex.get('uq_flagged', False)
    flag_str = f"($> {threshold}$ Threshold $\\rightarrow$ \\textbf{{Flagged}})" if flagged else f"($\\le {threshold}$ Threshold $\\rightarrow$ \\textbf{{Skipped}})"
    
    return f"""\\textbf{{[{dataset_name}]}} {claim} \\\\
\\textbf{{Gold Label:}} \\textsc{{{gold}}} \\hfill \\textbf{{Initial Prediction:}} \\textsc{{{param}}} ({param_correct}) \\\\
\\textbf{{Ensemble UQ Score:}} {score} {flag_str} \\\\
\\textbf{{Final Prediction:}} \\textsc{{{pred}}} ({pred_correct}) \\\\
"""

def generate_latex():
    sf_scenarios, sf_thresh, sf_name = get_best_model_examples("scifact")
    qt_scenarios, qt_thresh, qt_name = get_best_model_examples("quantemp", split="test")

    latex_out = """\\begin{table*}[h!]
\\small
\\centering
\\caption{Example workflows showcasing the Uncertainty-Aware RAG pipeline's behavior across different scenarios. The Ensemble UQ Score determines whether the parametric prediction is trusted or if the claim is flagged for evidence retrieval (RAG). Examples are drawn from both SciFact and QuanTemp datasets.}
\\renewcommand{\\arraystretch}{1.2}
\\begin{tabular}{p{0.95\\linewidth}}
\\toprule
"""
    scenarios = [
        ("Scenario 1: Incorrect Parametric Verdict $\\rightarrow$ Flagged $\\rightarrow$ Corrected", 0),
        ("Scenario 2: Correct Parametric Verdict $\\rightarrow$ Skipped $\\rightarrow$ Correct Verdict Retained", 1),
        ("Scenario 3: Incorrect Parametric Verdict $\\rightarrow$ Skipped $\\rightarrow$ Uncorrected", 2),
        ("Scenario 4: Correct Parametric Verdict $\\rightarrow$ Flagged $\\rightarrow$ Verdict Becomes Incorrect", 3),
    ]

    for title, idx in scenarios:
        latex_out += f"\\rowcolor{{gray!10}} \\multicolumn{{1}}{{c}}{{\\textbf{{{title}}}}} \\\\\n\\midrule\n"
        
        # SciFact Example
        ex_sf = sf_scenarios[idx][0] if sf_scenarios and sf_scenarios[idx] else None
        latex_out += format_latex_example(ex_sf, sf_thresh, "SciFact")
        
        latex_out += "\\hdashline\n"
        
        # QuanTemp Example
        ex_qt = qt_scenarios[idx][0] if qt_scenarios and qt_scenarios[idx] else None
        latex_out += format_latex_example(ex_qt, qt_thresh, "QuanTemp")
        
        if idx < 3:
            latex_out += "\\midrule\n"
            
    latex_out += """\\bottomrule
\\end{tabular}
\\label{tab:pipeline_examples_combined}
\\end{table*}
"""
    
    out_path = '/home/yulinchen/Desktop/Thesis-Project/appendix_examples_combined.tex'
    with open(out_path, 'w') as f:
        f.write(latex_out)
    print(f"LaTeX successfully written to {out_path}!")

if __name__ == "__main__":
    generate_latex()
