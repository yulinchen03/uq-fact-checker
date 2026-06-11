import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import os
import numpy as np
from pathlib import Path


def parse_mean_std(val):
    """Parses '0.395 ± 0.000' or '202 ± 0' into just the mean float value."""
    if isinstance(val, (int, float)):
        return float(val)
    val = str(val).strip()
    # Remove any trailing units like 's' (for latency)
    val = val.rstrip('s').rstrip('%').strip()
    if '±' in val:
        mean_part = val.split('±')[0].strip()
        return float(mean_part)
    try:
        return float(val)
    except ValueError:
        return np.nan


def main():
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 14,
        'axes.labelsize': 16,
        'axes.titlesize': 18,
        'xtick.labelsize': 14,
        'ytick.labelsize': 14,
        'legend.fontsize': 13,
        'legend.title_fontsize': 14,
        'figure.dpi': 300,
        'savefig.dpi': 300,
        'lines.linewidth': 2.5,
        'lines.markersize': 14
    })

    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    data_path = PROJECT_ROOT / 'vis_run_0.3' / 'unified_tables' / 'Table2_End_to_End_Efficiency_unified.csv'
    df = pd.read_csv(data_path)

    # Parse the "mean ± std" formatted columns into numeric values
    df['Balanced_Accuracy'] = df['Balanced_Accuracy'].apply(parse_mean_std)
    df['Total_Tokens'] = df['Total_Tokens'].apply(parse_mean_std)

    # Output directory under visualizations/
    out_dir = PROJECT_ROOT / 'vis_run_0.3' / 'efficiency_plots'
    out_dir.mkdir(parents=True, exist_ok=True)

    datasets = df['Dataset'].unique()

    # Extremely distinct high-contrast palette (Blue, Orange, Purple) to avoid any clashing
    colors = ['#1F77B4', '#FF7F0E', '#9467BD', '#D62728', '#8C564B', '#E377C2']

    # Distinct markers for different models
    markers = ['o', 's', '^', 'D', 'v', 'p']

    # Clean model names for legend
    model_name_map = {
        'Llama-3.1-8B-Instruct': 'Llama 8B',
        'Mistral-7B-Instruct-v0.3': 'Mistral 7B',
        'Qwen3-4B-Instruct-2507': 'Qwen 4B',
    }

    dataset_title_map = {
        'scifact': 'SciFact',
        'quantemp': 'QuanTemp',
    }

    for dataset in datasets:
        subset = df[df['Dataset'] == dataset]

        fig, ax = plt.subplots(figsize=(12, 7.5))

        models = subset['Model'].unique()

        handles = []
        labels = []

        for idx, model in enumerate(models):
            model_data = subset[subset['Model'] == model].copy()
            
            # Find the "Always Retrieve" tokens for this model to normalize
            ar_row = model_data[model_data['Method'] == 'Always Retrieve']
            if len(ar_row) > 0:
                ar_tokens = ar_row['Total_Tokens'].values[0]
                model_data['Relative_Tokens'] = (model_data['Total_Tokens'] / ar_tokens) * 100
            else:
                print(f"Warning: No 'Always Retrieve' found for {model} on {dataset}. Defaulting to absolute.")
                model_data['Relative_Tokens'] = model_data['Total_Tokens']

            model_data = model_data.sort_values(by='Relative_Tokens')

            color = colors[idx % len(colors)]
            marker_shape = markers[idx % len(markers)]

            # Deterministic dodge to reduce overlap between models (now in % units)
            x_dodge = (idx - 1) * 1.5 
            y_dodge = (idx - 1) * 0.002

            x_vals = model_data['Relative_Tokens'] + x_dodge
            y_vals = model_data['Balanced_Accuracy'] + y_dodge

            clean_name = model_name_map.get(model, model)

            # Plot the line connecting all points (without any markers yet)
            line, = ax.plot(x_vals, y_vals,
                            linestyle='-', label=clean_name,
                            color=color, alpha=0.85, zorder=2)
            handles.append(line)
            labels.append(clean_name)

            # Plot markers: baselines get special markers, UQ methods get hollow shapes
            for _, row in model_data.iterrows():
                method = row['Method']

                is_parametric = 'Parametric' in method
                is_always = 'Always' in method
                is_granular = 'Granular' in method
                is_baseline = is_parametric or is_always or is_granular

                if is_baseline:
                    if is_granular:
                        s_marker, s_size = '*', 26
                    elif is_always:
                        s_marker, s_size = 'X', 22
                    else:  # Parametric
                        s_marker, s_size = 'P', 22

                    ax.plot(row['Relative_Tokens'] + x_dodge, row['Balanced_Accuracy'] + y_dodge,
                            marker=s_marker, color=color, markersize=s_size,
                            linestyle='None', markeredgecolor='black',
                            markeredgewidth=1.5, zorder=3)
                else:
                    # UQ method: plot hollow marker
                    ax.plot(row['Relative_Tokens'] + x_dodge, row['Balanced_Accuracy'] + y_dodge,
                            marker=marker_shape, markerfacecolor='none',
                            color=color, markersize=14, markeredgewidth=1.5,
                            linestyle='None', zorder=2)

        ax.set_title(f'Accuracy-Efficiency Trade-off: {dataset_title_map.get(dataset, dataset)} Dataset',
                     weight='bold', pad=15)
        ax.set_xlabel('Token Consumption (% of Always RAG)')
        ax.set_ylabel('Balanced Accuracy')

        # Grid and spines
        ax.grid(True, linestyle=':', alpha=0.7, color='gray')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Add artificial padding to the top of the y-axis for legend space
        y_min, y_max = ax.get_ylim()
        y_range = y_max - y_min
        ax.set_ylim(y_min, y_max + y_range * 0.35)

        # Special markers for legend (kept at a readable size for the legend box)
        handles.extend([
            Line2D([0], [0], marker='P', color='gray', linestyle='None',
                   markersize=13, markeredgecolor='black', label='Parametric Only'),
            Line2D([0], [0], marker='X', color='gray', linestyle='None',
                   markersize=13, markeredgecolor='black', label='Always RAG'),
            Line2D([0], [0], marker='*', color='gray', linestyle='None',
                   markersize=17, markeredgecolor='black', label='Fine-grained RAG')
        ])
        labels.extend(['Parametric Only', 'Always RAG', 'Fine-grained RAG'])

        legend = ax.legend(handles, labels, loc='upper right', frameon=True,
                           fancybox=False, edgecolor='black',
                           fontsize=13, labelspacing=0.4, handletextpad=0.5)
        legend.get_frame().set_alpha(0.9)

        plt.tight_layout()
        ds_title = dataset_title_map.get(dataset, dataset)
        plt.savefig(out_dir / f'efficiency_plot_{ds_title}.png', dpi=300, facecolor='white', bbox_inches='tight')
        plt.close()
        print(f"Saved {out_dir / f'efficiency_plot_{ds_title}.png'}")


if __name__ == "__main__":
    main()
