import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path
from sklearn.metrics import roc_curve, auc

def load_json(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def shorten_name(name, logic_flag):
    """Dynamically parses estimator names and logic flags for clean X-axis labels."""
    mapping = {
        "MaximumSequenceProbability": "MaxSeqProb",
        "MeanTokenEntropy": "MeanTokEnt",
        "MeanPointwiseMutualInformation": "MeanPMI",
        "MeanConditionalPointwiseMutualInformation": "MeanCPMI",
        "RenyiNeg": "RenyiNeg",
        "never_retrieve": "Parametric\n(0% RAG)",
        "always_retrieve": "Always\nRetrieve",
        "granular": "Granular",
        "Ensemble": "Ensemble"
    }
    
    base_name = name
    for key, short_val in mapping.items():
        if key in name:
            base_name = short_val
            break
            
    # Append logic states dynamically
    if logic_flag:
        base_name += "\n[Logic Check On]"
            
    return base_name

# ==========================================
# DATA EXTRACTION (SUMMARY & JSONL)
# ==========================================

def extract_experiment_data(base_dir):
    records = []
    base_path = Path(base_dir)
    
    if not base_path.exists():
        return records

    for filepath in base_path.rglob("*summary.json"):
        if "calib" in str(filepath).lower():
            continue

        data = load_json(filepath)
        if not data: continue
        
        mode = data.get('experiment_mode', 'unknown')
        
        if mode in ["uq_decompose", "uq_aware"]:
            method_raw = filepath.parent.name 
        else:
            method_raw = mode
            
        metrics = data.get('metrics', {})
        
        is_logic_on = data.get('logic_aware', False) or ('logic' in filepath.name.lower() and 'off' not in filepath.name.lower())
        
        records.append({
            'Method_Raw': method_raw,
            'Display_Name': shorten_name(method_raw, is_logic_on),
            'Mode': mode,
            'Logic_ON': is_logic_on,
            'Balanced_Accuracy': metrics.get('balanced_accuracy', 0.0),
            'AUROC': metrics.get('error_detection_auroc'),
            'Latency_Sec': metrics.get('avg_latency_seconds', 0.0),
            'LLM_Calls': metrics.get('avg_llm_calls', 0.0),
            'Retrieval_Calls': metrics.get('avg_retrieval_calls', 0.0),
            'Dec_Input': metrics.get('avg_decomp_input_tokens', 0),
            'Dec_Output': metrics.get('avg_decomp_output_tokens', 0),
            'UQ_Input': metrics.get('avg_uq_input_tokens', 0),
            'UQ_Output': metrics.get('avg_uq_output_tokens', 0),
            'Gen_Input': metrics.get('avg_gen_input_tokens', metrics.get('avg_input_tokens', 0)),
            'Gen_Output': metrics.get('avg_gen_output_tokens', metrics.get('avg_output_tokens', 0)),
        })
        
    def sort_key(r):
        if r['Mode'] == 'never_retrieve': return (0, "")
        if r['Mode'] in ['uq_decompose', 'uq_aware']: 
            base = r['Display_Name'].split('\n')[0]
            logic_val = 1 if r['Logic_ON'] else 0
            return (1, f"{base}_{logic_val}")
        if r['Mode'] == 'granular': return (2, "")
        if r['Mode'] == 'always_retrieve': return (3, "")
        return (4, "")
        
    records.sort(key=lambda x: (sort_key(x)[0], sort_key(x)[1], x['Balanced_Accuracy']))
    return records

def extract_uq_jsonl_data(base_dir):
    uq_data = {}
    base_path = Path(base_dir)
    
    for filepath in base_path.rglob("**/*.jsonl"):
        if "calib" in str(filepath).lower():
            continue

        method_raw = filepath.parent.name
        
        if method_raw in ["never_retrieve", "always_retrieve", "granular"]:
            continue

        is_logic_on = "logic_discrete" in filepath.name
            
        display_name = shorten_name(method_raw, is_logic_on)
        claims = []
        
        with open(filepath, 'r') as f:
            for line in f:
                try:
                    row = json.loads(line)
                    
                    if 'parametric_verdict' not in row and 'uncertainty_score' not in row:
                        continue
                        
                    gold = row.get('gold_label', '')
                    param = row.get('parametric_verdict', '')
                    final = row.get('predicted_verdict', '')
                    score = row.get('uncertainty_score', 0.0)
                    uq_flagged = row.get('uq_flagged', True) 
                    
                    if score == float('inf') or pd.isna(score):
                        score = 1000.0 
                        
                    claims.append({
                        'param_correct': gold == param,
                        'final_correct': gold == final,
                        'needs_rag': int(gold != param), 
                        'uq_flagged': uq_flagged,
                        'score': score
                    })
                except Exception:
                    continue
                    
        if claims:
            uq_data[display_name] = claims
            
    return uq_data

# ==========================================
# TABLE EXPORT (NEW)
# ==========================================

def extract_calibration_data(base_dir, dataset_name, model_name):
    """Extracts metrics specifically from the CALIBRATION_SUMMARY.md file."""
    calib_records = []
    md_path = Path(base_dir) / "calibration" / "CALIBRATION_SUMMARY.md"
    
    if not md_path.exists():
        print(f"  [Debug] Calibration summary MD not found at: {md_path}")
        return calib_records

    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"  [Error] Failed to read {md_path}: {e}")
        return calib_records

    in_table = False
    for line in lines:
        line = line.strip()
        
        # Detect start of table
        if line.startswith("| AUROC |"):
            in_table = True
            continue
        # Skip the separator row
        if in_table and line.startswith("|:---:|"):
            continue
        # Break out of table if we hit an empty line or non-table line
        if in_table and not line.startswith("|"):
            in_table = False
            continue
            
        if in_table and line.startswith("|"):
            # Split by pipe and remove empty strings from edges
            parts = [p.strip() for p in line.split("|")[1:-1]]
            
            if len(parts) >= 8:
                try:
                    auroc = float(parts[0])
                    config = parts[1].replace('`', '')
                    uq_method = parts[2]
                    threshold = float('inf') if parts[3] == 'inf' else float(parts[3])
                    
                    # Clean percentage string into a float (e.g., "17.5%" -> 0.175)
                    coverage_str = parts[4].replace('%', '')
                    coverage = float(coverage_str) / 100.0
                    
                    risk = float(parts[5])
                    tpr = float(parts[6])
                    tnr = float(parts[7])
                    
                    is_logic_on = "logic_discrete" in config
                    
                    calib_records.append({
                        'Model': model_name,
                        'Method': shorten_name(uq_method, is_logic_on).replace('\n', ' '),
                        'AUROC': auroc,
                        'Threshold': threshold,
                        'Coverage': coverage,
                        'Risk': risk,
                        'TPR': tpr,
                        'TNR': tnr
                    })
                except ValueError as e:
                    print(f"  [Debug] Failed to parse row: {line} -> Error: {e}")
                    
    print(f"  [Debug] Successfully extracted {len(calib_records)} calibration records from Markdown for {model_name}.")
    return calib_records

def export_summary_tables(records, tables_out_dir, dataset_name, model_name):
    """Generates CSV and Markdown score tables for paper reporting in a unified folder."""
    if not records:
        return None, None

    df = pd.DataFrame(records)
    
    # Calculate Total Tokens
    df['Total_Tokens'] = (df['Dec_Input'] + df['Dec_Output'] + 
                          df['UQ_Input'] + df['UQ_Output'] + 
                          df['Gen_Input'] + df['Gen_Output'])
    
    # Clean up Display Names for tables (remove newlines)
    df['Method'] = df['Display_Name'].apply(lambda x: x.replace('\n', ' '))

    # Format Flag Rate dynamically
    if 'Flag_Rate' in df.columns:
        df['Flag_Rate_Fmt'] = df['Flag_Rate'].apply(lambda x: f"{x * 100:.1f}%" if pd.notnull(x) else "N/A")
    else:
        df['Flag_Rate_Fmt'] = "N/A"

    # ---------------------------------------------------------
    # TABLE 1: UQ Performance (AUROC) & Flag Rate
    # ---------------------------------------------------------
    table1 = None
    uq_df = df[df['AUROC'].notnull()].copy()
    if not uq_df.empty:
        cols_table1 = ['Method', 'AUROC', 'Flag_Rate_Fmt']
        table1 = uq_df[cols_table1].rename(columns={'Flag_Rate_Fmt': 'Flag Rate'}).sort_values(by='AUROC', ascending=False)
        table1.insert(0, 'Model', model_name)
        table1.insert(0, 'Dataset', dataset_name)
        
        print("\n" + "="*60)
        print(f"TABLE 1: UQ Performance & Flag Rate | {dataset_name.capitalize()} | {model_name}")
        print("="*60)
        print(table1.drop(columns=['Dataset', 'Model']).to_markdown(index=False, floatfmt=".3f"))

    # ---------------------------------------------------------
    # TABLE 2: End-to-End Performance & Efficiency
    # ---------------------------------------------------------
    cols_to_keep = ['Method', 'Balanced_Accuracy', 'Flag_Rate_Fmt', 'Total_Tokens', 'LLM_Calls', 'Retrieval_Calls', 'Latency_Sec']
    table2 = df[cols_to_keep].copy()
    table2.rename(columns={'Flag_Rate_Fmt': 'Flag Rate'}, inplace=True)
    
    table2['Sort_Rank'] = df['Mode'].map({
        'never_retrieve': 0,
        'always_retrieve': 1,
        'granular': 2,
        'uq_aware': 3,
    })
    table2 = table2.sort_values(by=['Sort_Rank', 'Balanced_Accuracy'], ascending=[True, False]).drop(columns=['Sort_Rank'])
    
    # Formatting for aesthetics
    table2['Balanced_Accuracy'] = table2['Balanced_Accuracy'].apply(lambda x: f"{x:.3f}")
    table2['LLM_Calls'] = table2['LLM_Calls'].apply(lambda x: f"{x:.2f}")
    table2['Retrieval_Calls'] = table2['Retrieval_Calls'].apply(lambda x: f"{x:.2f}")
    table2['Latency_Sec'] = table2['Latency_Sec'].apply(lambda x: f"{x:.2f}s")
    
    table2.insert(0, 'Model', model_name)
    table2.insert(0, 'Dataset', dataset_name)

    print("\n" + "="*95)
    print(f"TABLE 2: End-to-End Performance & Efficiency | {dataset_name.capitalize()} | {model_name}")
    print("="*95)
    print(table2.drop(columns=['Dataset', 'Model']).to_markdown(index=False))
    print("\n")
    
    return table1, table2

def export_unified_calibration_table(all_calib_records, out_dir, dataset_name):
    """Generates a single unified calibration table across all models for the appendix."""
    if not all_calib_records:
        return

    df = pd.DataFrame(all_calib_records)
    
    # Drop rows without an AUROC score (e.g., baselines)
    df = df[df['AUROC'].notnull()].copy()
    
    # Sort logically by Model, then by AUROC descending
    df = df.sort_values(by=['Model', 'AUROC'], ascending=[True, False])
    
    # Format numbers for clean paper reading
    df['AUROC'] = df['AUROC'].apply(lambda x: f"{x:.3f}")
    df['Threshold'] = df['Threshold'].apply(lambda x: f"{x:.3f}" if isinstance(x, (int, float)) else x)
    df['Coverage'] = df['Coverage'].apply(lambda x: f"{x * 100:.1f}%" if x <= 1.0 else f"{x:.1f}%")
    df['Risk'] = df['Risk'].apply(lambda x: f"{x:.3f}")
    df['TPR'] = df['TPR'].apply(lambda x: f"{x:.3f}")
    df['TNR'] = df['TNR'].apply(lambda x: f"{x:.3f}")

    filename = f"Appendix_Calibration_Results_{dataset_name}.csv"
    df.to_csv(out_dir / filename, index=False)

    print("\n" + "="*90)
    print(f"APPENDIX TABLE: Unified Calibration Results | {dataset_name.capitalize()}")
    print("="*90)
    print(df.to_markdown(index=False))
    print("\n")


# ==========================================
# MASTER DASHBOARD PLOTS
# ==========================================

def plot_accuracy(ax, records):
    labels = [r['Display_Name'] for r in records]
    acc_vals = [r['Balanced_Accuracy'] for r in records]
    x = np.arange(len(labels))
    width = 0.6
    
    colors = []
    for r in records:
        if r['Mode'] == 'never_retrieve': colors.append('#e74c3c')
        elif r['Mode'] == 'always_retrieve': colors.append('#3498db')
        elif r['Mode'] == 'granular': colors.append('#9b59b6')
        else:
            colors.append('#27ae60' if r['Logic_ON'] else '#2ecc71')

    bars = ax.bar(x, acc_vals, width, color=colors, edgecolor='black')
    ax.bar_label(bars, fmt='%.3f', padding=3, fontsize=9, fontweight='bold', rotation=45)
    ax.set_ylabel('Balanced Accuracy (0.0 - 1.0)', fontsize=12, fontweight='bold')
    ax.set_title('Pipeline Balanced Accuracy Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=10)
    ax.set_ylim(0, 1.15)
        
    legend_elements = [
        mpatches.Patch(facecolor='#e74c3c', edgecolor='black', label='Parametric'),
        mpatches.Patch(facecolor='#2ecc71', edgecolor='black', label='UQ (Logic OFF)'),
        mpatches.Patch(facecolor='#27ae60', edgecolor='black', label='UQ (Logic ON)'),
        mpatches.Patch(facecolor='#9b59b6', edgecolor='black', label='Granular'),
        mpatches.Patch(facecolor='#3498db', edgecolor='black', label='Always Retrieve')
    ]
    ax.legend(handles=legend_elements, fontsize=10, loc="upper left")
    ax.grid(axis='y', linestyle='--', alpha=0.7)

def plot_tokens(ax, records):
    labels = [r['Display_Name'] for r in records]
    
    dec_in = np.array([r['Dec_Input'] for r in records])
    dec_out = np.array([r['Dec_Output'] for r in records])
    uq_in = np.array([r['UQ_Input'] for r in records])
    uq_out = np.array([r['UQ_Output'] for r in records])
    gen_in = np.array([r['Gen_Input'] for r in records])
    gen_out = np.array([r['Gen_Output'] for r in records])

    x = np.arange(len(labels))
    width = 0.65
    
    c_dec_in, c_dec_out = '#9b59b6', '#8e44ad' 
    c_uq_in, c_uq_out = '#FFC300', '#FF5733'   
    c_gen_in, c_gen_out = '#00C9A7', '#2C73D2' 
    
    p1 = ax.bar(x, dec_in, width, color=c_dec_in, edgecolor='black')
    p2 = ax.bar(x, dec_out, width, bottom=dec_in, color=c_dec_out, edgecolor='black')
    p3 = ax.bar(x, uq_in, width, bottom=dec_in+dec_out, color=c_uq_in, edgecolor='black')
    p4 = ax.bar(x, uq_out, width, bottom=dec_in+dec_out+uq_in, color=c_uq_out, edgecolor='black')
    p5 = ax.bar(x, gen_in, width, bottom=dec_in+dec_out+uq_in+uq_out, color=c_gen_in, edgecolor='black')
    p6 = ax.bar(x, gen_out, width, bottom=dec_in+dec_out+uq_in+uq_out+gen_in, color=c_gen_out, edgecolor='black')

    def label_fmt(val): return f"{int(val)}" if val > 30 else ""
    ax.bar_label(p1, label_type='center', fmt=label_fmt, fontsize=9, fontweight='bold', color='white')
    ax.bar_label(p2, label_type='center', fmt=label_fmt, fontsize=9, fontweight='bold', color='white')
    ax.bar_label(p3, label_type='center', fmt=label_fmt, fontsize=9, fontweight='bold', color='black')
    ax.bar_label(p4, label_type='center', fmt=label_fmt, fontsize=9, fontweight='bold', color='black')
    ax.bar_label(p5, label_type='center', fmt=label_fmt, fontsize=9, fontweight='bold', color='black')
    ax.bar_label(p6, label_type='center', fmt=label_fmt, fontsize=9, fontweight='bold', color='white')

    ax.set_ylabel('Average Tokens per Claim', fontsize=12, fontweight='bold')
    ax.set_title('Token Consumption Cost (Avg per Claim)', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=10)
    
    totals = dec_in + dec_out + uq_in + uq_out + gen_in + gen_out
    if len(totals) > 0: ax.set_ylim(0, max(totals) * 1.3) 
    
    legend_elements = [
        mpatches.Patch(facecolor=c_dec_in, edgecolor='black', label='Decomp Input'),
        mpatches.Patch(facecolor=c_dec_out, edgecolor='black', label='Decomp Output'),
        mpatches.Patch(facecolor=c_uq_in, edgecolor='black', label='UQ Input'),
        mpatches.Patch(facecolor=c_uq_out, edgecolor='black', label='UQ Output'),
        mpatches.Patch(facecolor=c_gen_in, edgecolor='black', label='RAG Input'),
        mpatches.Patch(facecolor=c_gen_out, edgecolor='black', label='RAG Output')
    ]
    ax.legend(handles=legend_elements, loc="upper left", fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    for i, total in enumerate(totals):
        ax.text(i, total + (max(totals) * 0.02), f"{int(total)}", ha='center', fontsize=10, fontweight='bold', rotation=45)

def plot_calls(ax, records):
    labels = [r['Display_Name'] for r in records]
    llm_vals = [r['LLM_Calls'] for r in records]
    ret_vals = [r['Retrieval_Calls'] for r in records]

    x = np.arange(len(labels))
    width, offset = 0.35, 0.20
    
    r1 = ax.bar(x - offset, ret_vals, width, color='#8E44AD', edgecolor='black', label='Retrieval Calls')
    r2 = ax.bar(x + offset, llm_vals, width, color='#16A085', edgecolor='black', label='LLM Calls')

    ax.bar_label(r1, fmt='%.2f', padding=4, fontsize=9, fontweight='bold')
    ax.bar_label(r2, fmt='%.2f', padding=4, fontsize=9, fontweight='bold')

    ax.set_ylabel('Average Calls per Claim', fontsize=12, fontweight='bold')
    ax.set_title('LLM & Retrieval Calls (Avg per Claim)', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=10)
    
    max_val = max(max(llm_vals, default=0), max(ret_vals, default=0))
    if max_val > 0: ax.set_ylim(0, max_val * 1.35)
    
    ax.legend(fontsize=10, loc="upper left")
    ax.grid(axis='y', linestyle='--', alpha=0.7)

def plot_auroc(ax, records):
    uq_records = [r for r in records if r['AUROC'] is not None]
    if not uq_records:
        ax.text(0.5, 0.5, 'No AUROC Data Available', ha='center', va='center', fontsize=12, color='gray')
        ax.set_xticks([]); ax.set_yticks([]); ax.set_title('Error Detection AUROC', fontsize=14, fontweight='bold')
        return

    labels = [r['Display_Name'] for r in uq_records]
    auroc_vals = [r['AUROC'] for r in uq_records]
    x = np.arange(len(labels))
    
    bars = ax.bar(x, auroc_vals, 0.5, color='#e67e22', edgecolor='black')
    ax.bar_label(bars, fmt='%.3f', padding=3, fontsize=10, fontweight='bold')
    ax.set_ylabel('AUROC Score', fontsize=12, fontweight='bold')
    ax.set_title('Uncertainty Error Detection AUROC', fontsize=14, fontweight='bold')
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=10, rotation=45, ha='right')
    ax.set_ylim(0, 1.1)
    ax.axhline(0.5, color='red', linestyle=':', linewidth=2, label='Random Guessing')
    ax.legend(fontsize=10, loc="upper right")
    ax.grid(axis='y', linestyle='--', alpha=0.7)

# ==========================================
# DEEP DIVE UQ PLOTS
# ==========================================

def generate_roc_curves(uq_data, save_path):
    if not uq_data: return
    
    plt.figure(figsize=(12, 10))
    for method, claims in uq_data.items():
        y_true = [c['needs_rag'] for c in claims]
        y_score = [c['score'] for c in claims]
        
        if len(set(y_true)) > 1: 
            fpr, tpr, _ = roc_curve(y_true, y_score)
            roc_auc = auc(fpr, tpr)
            
            linestyle = '-' if 'ON' in method else '--'
            plt.plot(fpr, tpr, lw=2, linestyle=linestyle, label=f'{method.replace(chr(10), " ")} (AUC = {roc_auc:.3f})')
            
    plt.plot([0, 1], [0, 1], color='black', lw=2, linestyle=':', label='Random Guessing')
    plt.xlim([0.0, 1.0]); plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate (Flagged a Correct Claim)', fontsize=12, fontweight='bold')
    plt.ylabel('True Positive Rate (Flagged an Incorrect Claim)', fontsize=12, fontweight='bold')
    plt.title('Uncertainty Filter Performance (ROC Curves)', fontsize=16, fontweight='bold')
    plt.legend(loc="lower right", fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, facecolor='white')
    plt.close()

def generate_uq_flow_plots(uq_data, save_path):
    if not uq_data: return
    
    stats = []
    for m, claims in uq_data.items():
        param_mistakes = [c for c in claims if not c['param_correct']]
        caught_mistakes = [c for c in param_mistakes if c['uq_flagged']]
        slipped_mistakes_count = len(param_mistakes) - len(caught_mistakes)
        
        resolved = sum(1 for c in caught_mistakes if c['final_correct'])
        unresolved = len(caught_mistakes) - resolved
        
        param_successes = [c for c in claims if c['param_correct']]
        unnecessarily_flagged = [c for c in param_successes if c['uq_flagged']]
        efficiently_bypassed = len(param_successes) - len(unnecessarily_flagged)
        
        remained_correct = sum(1 for c in unnecessarily_flagged if c['final_correct'])
        broken_by_rag = len(unnecessarily_flagged) - remained_correct
        
        recall = len(caught_mistakes) / max(1, len(param_mistakes))
        
        stats.append({
            'method': m,
            'caught': len(caught_mistakes), 'slipped': slipped_mistakes_count,
            'resolved': resolved, 'unresolved': unresolved,
            'bypassed': efficiently_bypassed, 'unnec_flagged': len(unnecessarily_flagged),
            'remained': remained_correct, 'broken': broken_by_rag,
            'recall': recall
        })

    stats.sort(key=lambda x: x['recall'])

    methods = [s['method'].replace('\n', ' ') for s in stats] 
    y = np.arange(len(methods))
    
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(22, 16), sharey=True) 
    
    def add_labels(containers, ax):
        for c in containers:
            ax.bar_label(c, label_type='center', fmt=lambda x: f'{int(x)}' if x > 0 else '', fontsize=10, fontweight='bold', color='black')

    ax1, ax2 = axes[0, 0], axes[0, 1]
    caught_vals = np.array([s['caught'] for s in stats])
    slipped_vals = np.array([s['slipped'] for s in stats])
    resolved_vals = np.array([s['resolved'] for s in stats])
    unresolved_vals = np.array([s['unresolved'] for s in stats])
    
    p1 = ax1.barh(y, caught_vals, color='#2ecc71', edgecolor='black', label='Successfully Flagged')
    p2 = ax1.barh(y, slipped_vals, left=caught_vals, color='#e74c3c', edgecolor='black', label='Slipped Through')
    add_labels([p1], ax1); ax1.bar_label(p2, label_type='center', fmt=lambda x: f'{int(x)}' if x > 0 else '', fontsize=10, fontweight='bold', color='white')
    ax1.set_title('1. Out of all Parametric Mistakes...', fontsize=15, fontweight='bold')
    ax1.set_xlabel('Number of Claims', fontsize=12, fontweight='bold'); ax1.legend(loc='upper right', fontsize=10); ax1.grid(axis='x', linestyle='--', alpha=0.7)
    
    p3 = ax2.barh(y, resolved_vals, color='#3498db', edgecolor='black', label='Fixed by RAG')
    p4 = ax2.barh(y, unresolved_vals, left=resolved_vals, color='#f39c12', edgecolor='black', label='Failed to Fix')
    add_labels([p3, p4], ax2)
    ax2.set_title('2. Out of the CAUGHT Mistakes...', fontsize=15, fontweight='bold')
    ax2.set_xlabel('Number of Claims', fontsize=12, fontweight='bold'); ax2.legend(loc='upper right', fontsize=10); ax2.grid(axis='x', linestyle='--', alpha=0.7)

    ax3, ax4 = axes[1, 0], axes[1, 1]
    bypassed_vals = np.array([s['bypassed'] for s in stats])
    unnec_flagged_vals = np.array([s['unnec_flagged'] for s in stats])
    remained_vals = np.array([s['remained'] for s in stats])
    broken_vals = np.array([s['broken'] for s in stats])

    p5 = ax3.barh(y, bypassed_vals, color='#9b59b6', edgecolor='black', label='Efficiently Bypassed (Saved Tokens)')
    p6 = ax3.barh(y, unnec_flagged_vals, left=bypassed_vals, color='#f1c40f', edgecolor='black', label='Unnecessarily Flagged (Wasted Tokens)')
    add_labels([p5, p6], ax3)
    ax3.set_title('3. Out of all Parametric Successes...', fontsize=15, fontweight='bold')
    ax3.set_xlabel('Number of Claims', fontsize=12, fontweight='bold'); ax3.legend(loc='upper right', fontsize=10); ax3.grid(axis='x', linestyle='--', alpha=0.7)
    ax3.set_yticks(y); ax3.set_yticklabels(methods, fontsize=11)
    
    p7 = ax4.barh(y, remained_vals, color='#16a085', edgecolor='black', label='Remained Correct (Harmless Waste)')
    p8 = ax4.barh(y, broken_vals, left=remained_vals, color='#c0392b', edgecolor='black', label='Broken by RAG (Fatal Harm)')
    add_labels([p7], ax4); ax4.bar_label(p8, label_type='center', fmt=lambda x: f'{int(x)}' if x > 0 else '', fontsize=10, fontweight='bold', color='white')
    ax4.set_title('4. Out of the UNNECESSARILY FLAGGED...', fontsize=15, fontweight='bold')
    ax4.set_xlabel('Number of Claims', fontsize=12, fontweight='bold'); ax4.legend(loc='upper right', fontsize=10); ax4.grid(axis='x', linestyle='--', alpha=0.7)

    fig.suptitle('Complete UQ Pipeline Flow: Mistakes vs. Successes', fontsize=20, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, facecolor='white', bbox_inches='tight')
    plt.close()

def generate_uq_routing_accuracy_plot(uq_data, save_path):
    if not uq_data: return
    
    stats = []
    for m, claims in uq_data.items():
        caught, bypassed, slipped, wasted = 0, 0, 0, 0
        
        for c in claims:
            if c['needs_rag'] == 1: 
                if c['uq_flagged']: caught += 1    
                else: slipped += 1                 
            else: 
                if c['uq_flagged']: wasted += 1    
                else: bypassed += 1                
                
        correct_routing = caught + bypassed
        incorrect_routing = slipped + wasted
        total = correct_routing + incorrect_routing
        acc = correct_routing / max(1, total)
        
        stats.append({
            'method': m, 'caught': caught, 'bypassed': bypassed,
            'slipped': slipped, 'wasted': wasted, 'acc': acc
        })

    stats.sort(key=lambda x: x['acc'])

    methods = [s['method'].replace('\n', ' ') for s in stats] 
    bypassed_vals = np.array([s['bypassed'] for s in stats])
    caught_vals = np.array([s['caught'] for s in stats])
    wasted_vals = np.array([s['wasted'] for s in stats])
    slipped_vals = np.array([s['slipped'] for s in stats])
    
    plt.figure(figsize=(16, 9)) 
    y = np.arange(len(methods))
    width = 0.65
    
    c_bypassed = '#27ae60'  
    c_caught = '#2ecc71'    
    c_wasted = '#f39c12'    
    c_slipped = '#e74c3c'   
    
    p1 = plt.barh(y, bypassed_vals, height=width, color=c_bypassed, edgecolor='black', label='Correct Bypass (Saved Tokens)')
    p2 = plt.barh(y, caught_vals, height=width, left=bypassed_vals, color=c_caught, edgecolor='black', label='Correct Flag (Caught Mistake)')
    
    p3 = plt.barh(y, wasted_vals, height=width, left=bypassed_vals+caught_vals, color=c_wasted, edgecolor='black', label='Incorrect Flag (Wasted Tokens)')
    p4 = plt.barh(y, slipped_vals, height=width, left=bypassed_vals+caught_vals+wasted_vals, color=c_slipped, edgecolor='black', label='Incorrect Bypass (Fatal Slip)')
    
    def add_labels(containers):
        for c in containers:
            plt.bar_label(c, label_type='center', fmt=lambda x: f'{int(x)}' if x > 20 else '', fontsize=9, fontweight='bold', color='black')
            
    add_labels([p1, p2, p3])
    plt.bar_label(p4, label_type='center', fmt=lambda x: f'{int(x)}' if x > 20 else '', fontsize=9, fontweight='bold', color='white')

    total_claims = bypassed_vals[0] + caught_vals[0] + wasted_vals[0] + slipped_vals[0]
    for i, acc in enumerate([s['acc'] for s in stats]):
        plt.text(total_claims + 15, i, f"{acc*100:.1f}%", va='center', fontsize=11, fontweight='bold', color='#2c3e50')

    plt.xlim(0, total_claims * 1.15) 
    plt.xlabel('Total Claims Evaluated', fontsize=12, fontweight='bold')
    plt.title('Overall UQ Router Accuracy: Subdivided Successes & Failures', fontsize=16, fontweight='bold')
    plt.yticks(y, methods, fontsize=11)
    
    plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.15), ncol=2, fontsize=10)
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, facecolor='white', bbox_inches='tight')
    plt.close()

# ==========================================
# EXECUTION
# ==========================================

def main():
    datasets = ["quantemp", "scifact"]
    models = ["Llama-3.1-8B-Instruct", "Qwen3-4B-Instruct-2507", "Mistral-7B-Instruct-v0.3", "gemma-3-12b-it"]

    # Resolve project root (two levels up from scripts/visualization/)
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

    unified_tables_dir = PROJECT_ROOT / "vis" / "unified_tables"
    unified_tables_dir.mkdir(parents=True, exist_ok=True)
    
    all_table1_records = []
    all_table2_records = []

    for dataset in datasets:
        all_calib_records = []
        print(f"\nProcessing dataset: {dataset}")
        for model in models:
            print(f"  Processing model: {model}")
            target_dir = PROJECT_ROOT / "results_dump" / "final_2" / dataset / model
            out_dir = PROJECT_ROOT / "vis" / dataset / model
            out_dir.mkdir(parents=True, exist_ok=True)
            
            print(f"Scanning {target_dir} for data...")
            records = extract_experiment_data(target_dir)
            uq_data = extract_uq_jsonl_data(target_dir)

            # ---> INJECT DYNAMIC FLAG RATE INTO RECORDS HERE
            for r in records:
                d_name = r['Display_Name']
                # Compute it directly from the parsed test JSONL responses if available
                if d_name in uq_data and len(uq_data[d_name]) > 0:
                    flag_count = sum(1 for c in uq_data[d_name] if c['uq_flagged'])
                    r['Flag_Rate'] = flag_count / len(uq_data[d_name])
                else:
                    # Handle baselines that don't generate UQ data
                    if r['Mode'] == 'always_retrieve':
                        r['Flag_Rate'] = 1.0
                    elif r['Mode'] in ['never_retrieve', 'granular']:
                        r['Flag_Rate'] = 0.0
                    else:
                        r['Flag_Rate'] = np.nan

            calib_records = extract_calibration_data(target_dir, dataset, model)
            all_calib_records.extend(calib_records)
        
            if not records:
                print("No summary records found. Check the path!")
                continue
            
            print(f"Found {len(records)} summary records. Assembling Master Dashboard...")
            fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(24, 16)) 
            fig.suptitle(f'Fact-Checking Pipeline Evaluation Dashboard | {dataset.capitalize()} - {model}', fontsize=20, fontweight='bold', y=0.97)
            
            plot_accuracy(axes[0, 0], records)
            plot_tokens(axes[0, 1], records)
            plot_calls(axes[1, 0], records)
            plot_auroc(axes[1, 1], records)
            
            plt.tight_layout(rect=[0, 0.03, 1, 0.95], h_pad=3.0, w_pad=2.0)
            plt.savefig(out_dir / "1_dashboard_summary.png", dpi=300, bbox_inches='tight', facecolor='white')
            plt.close()
            
            if uq_data:
                print(f"Found {len(uq_data)} UQ JSONL files. Generating Deep Analyses...")
                generate_roc_curves(uq_data, out_dir / "2_uq_roc_curves.png")
                generate_uq_flow_plots(uq_data, out_dir / "3_uq_conditional_flow.png")
                generate_uq_routing_accuracy_plot(uq_data, out_dir / "4_uq_overall_routing_accuracy.png")
            else:
                print("Warning: UQ JSONL data could not be parsed. Deep Analyses skipped.")

            print(f"Generating Tabular Reports...")
            
            table1_df, table2_df = export_summary_tables(records, unified_tables_dir, dataset, model)
            if table1_df is not None:
                all_table1_records.append(table1_df)
            if table2_df is not None:
                all_table2_records.append(table2_df)

            print(f"✅ All visualizations saved successfully to: {out_dir}")
            print(f"✅ All tables saved successfully to: {unified_tables_dir}")

        if all_calib_records:
            print(f"Generating Unified Calibration Appendix Table...")
            export_unified_calibration_table(all_calib_records, unified_tables_dir, dataset)
            print(f"✅ Calibration Appendix table saved successfully to: {unified_tables_dir}")
            
    if all_table1_records:
        unified_df = pd.concat(all_table1_records, ignore_index=True)
        out_path = unified_tables_dir / 'Table1_UQ_Performance_unified.csv'
        unified_df.to_csv(out_path, index=False)
        print(f"✅ Successfully saved unified Table 1 results to {out_path}")
        
    if all_table2_records:
        unified_df2 = pd.concat(all_table2_records, ignore_index=True)
        out_path2 = unified_tables_dir / 'Table2_End_to_End_Efficiency_unified.csv'
        unified_df2.to_csv(out_path2, index=False)
        print(f"✅ Successfully saved unified Table 2 results to {out_path2}")

if __name__ == "__main__":
    main()