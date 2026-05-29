import pandas as pd
import numpy as np

def get_display_method(raw_method):
    if raw_method == 'Granular':
        return 'Granular Verification'
    elif raw_method == 'Ensemble [Logic Check On]':
        return 'Ensemble w/ ACE'
    else:
        return raw_method.replace(' [Logic Check On]', '')

def generate_latex_table_per_model(df, model_name, display_name):
    df_model = df[df['Model'] == model_name].copy()
    
    baselines = [
        'Parametric (0% RAG)',
        'Always Retrieve',
        'Granular'
    ]
    
    uq_methods = [
        'LogicalContradiction [Logic Check On]',
        'MaxSeqProb [Logic Check On]',
        'MeanTokEnt [Logic Check On]',
        'Perplexity [Logic Check On]',
        'Ensemble [Logic Check On]',
        'Ensemble'
    ]
    
    datasets = ['SciFact', 'QuanTemp']
    
    best_acc = {ds: -1.0 for ds in datasets}
    best_tok = {ds: float('inf') for ds in datasets}
    
    for method in uq_methods:
        for ds in datasets:
            row_data = df_model[(df_model['Method'] == method) & (df_model['Dataset'] == ds)]
            if not row_data.empty:
                acc = row_data.iloc[0]['Balanced_Accuracy']
                tok = float(row_data.iloc[0]['Total_Tokens'])
                if acc > best_acc[ds]:
                    best_acc[ds] = acc
                if tok < best_tok[ds]:
                    best_tok[ds] = tok
    
    latex = []
    latex.append("\\begin{table*}[t]")
    latex.append("\\centering")
    latex.append(f"\\caption{{End-to-End Efficiency results for the \\textbf{{{display_name}}} model across datasets. \\textbf{{Acc}} = Balanced Accuracy, \\textbf{{FR}} = Flag Rate, \\textbf{{Tok}} = Total Tokens, \\textbf{{LLM}} = LLM Calls, \\textbf{{Ret}} = Retrieval Calls. The most accurate UQ setup is \\textbf{{bolded}}, and the most efficient is \\underline{{underlined}}.}}")
    latex.append(f"\\label{{tab:efficiency_{display_name.replace(' ', '').lower()}}}")
    latex.append("\\resizebox{\\textwidth}{!}{%")
    latex.append("\\begin{tabular}{l | ccccc | ccccc}")
    latex.append("\\toprule")
    
    header1 = "& \\multicolumn{5}{c|}{\\textbf{SciFact}} & \\multicolumn{5}{c}{\\textbf{QuanTemp}} \\\\"
    latex.append(header1)
    
    header2 = "\\textbf{Method} "
    for _ in range(2):
        header2 += "& \\textbf{Acc} & \\textbf{FR} & \\textbf{Tok} & \\textbf{LLM} & \\textbf{Ret} "
    header2 += "\\\\"
    latex.append(header2)
    latex.append("\\midrule")
    
    def process_method_row(method, is_uq=False):
        disp_method = get_display_method(method)
        
        is_best_acc_any = False
        is_best_tok_any = False
        
        if is_uq:
            for ds in datasets:
                row_data = df_model[(df_model['Method'] == method) & (df_model['Dataset'] == ds)]
                if not row_data.empty:
                    acc_val = row_data.iloc[0]['Balanced_Accuracy']
                    tok_val = float(row_data.iloc[0]['Total_Tokens'])
                    if abs(acc_val - best_acc[ds]) < 1e-5: is_best_acc_any = True
                    if abs(tok_val - best_tok[ds]) < 1e-5: is_best_tok_any = True
        
        formatted_method = disp_method
        if is_best_acc_any: formatted_method = f"\\textbf{{{formatted_method}}}"
        elif is_best_tok_any: formatted_method = f"\\underline{{{formatted_method}}}"
        # If it's both, we just bold it or we could nest it, but usually one is enough.
        
        row_str = f"{formatted_method} "
        for ds in datasets:
            row_data = df_model[(df_model['Method'] == method) & (df_model['Dataset'] == ds)]
            if not row_data.empty:
                r = row_data.iloc[0]
                acc_val = r['Balanced_Accuracy']
                tok_val = float(r['Total_Tokens'])
                
                acc_str = f"{acc_val:.3f}"
                tok_str = str(int(tok_val))
                fr_str = str(r['Flag Rate']).replace('%', '\\%')
                llm_str = f"{float(r['LLM_Calls']):.2f}"
                ret_str = f"{float(r['Retrieval_Calls']):.2f}"
                
                is_best_acc = is_uq and abs(acc_val - best_acc[ds]) < 1e-5
                is_best_tok = is_uq and abs(tok_val - best_tok[ds]) < 1e-5
                
                if is_best_acc:
                    acc_str = f"\\textbf{{{acc_str}}}"
                    tok_str = f"\\textbf{{{tok_str}}}"
                    fr_str = f"\\textbf{{{fr_str}}}"
                    llm_str = f"\\textbf{{{llm_str}}}"
                    ret_str = f"\\textbf{{{ret_str}}}"
                elif is_best_tok:
                    acc_str = f"\\underline{{{acc_str}}}"
                    tok_str = f"\\underline{{{tok_str}}}"
                    fr_str = f"\\underline{{{fr_str}}}"
                    llm_str = f"\\underline{{{llm_str}}}"
                    ret_str = f"\\underline{{{ret_str}}}"
                
                row_str += f"& {acc_str} & {fr_str} & {tok_str} & {llm_str} & {ret_str} "
            else:
                row_str += "& - & - & - & - & - "
        row_str += "\\\\"
        latex.append(row_str)

    for method in baselines:
        process_method_row(method, is_uq=False)
        
    latex.append("\\midrule")
    
    for method in uq_methods:
        process_method_row(method, is_uq=True)
        
    latex.append("\\bottomrule")
    latex.append("\\end{tabular}%")
    latex.append("}")
    latex.append("\\end{table*}")
    latex.append("")
    
    return "\n".join(latex)

def main():
    csv_path = 'visualizations/unified_tables/Table2_End_to_End_Efficiency_unified.csv'
    df = pd.read_csv(csv_path)
    
    models = [
        ('Qwen3-4B-Instruct-2507', 'Qwen 4B'),
        ('Mistral-7B-Instruct-v0.3', 'Mistral 7B'),
        ('Llama-3.1-8B-Instruct', 'Llama 8B')
    ]
    
    for model_name, display_name in models:
        print(f"================== {display_name.upper()} TABLE ==================")
        print(generate_latex_table_per_model(df, model_name, display_name))

if __name__ == '__main__':
    main()
