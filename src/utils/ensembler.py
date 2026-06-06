import json
import os
import sys
import shap
import pickle
import warnings
from sklearn.exceptions import ConvergenceWarning
import numpy as np
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
import matplotlib.pyplot as plt

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=ConvergenceWarning)

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

def clean_label(label: str) -> str:
    lbl = str(label).upper().replace(".", "").replace("_", " ")
    return " ".join(lbl.split())

class UQEnsembler:
    """Manages the training, cross-validation, and packaging of Logistic Regression UQ Ensembles."""

    def __init__(self, dataset: str, split: str, model_name: str, check_logic: bool, output_format: str, logic_eval_method: str, seed: int = 42):
        self.dataset = dataset
        self.split = split
        self.model_name = model_name.split("/")[-1]
        self.check_logic = check_logic
        self.output_format = output_format
        self.logic_eval_method = logic_eval_method
        self.seed = seed
        
        self.base_dir = ROOT_DIR / "run_results" / f"seed_{self.seed}" / self.dataset / self.model_name / "calibration"
        
        if self.check_logic:
            self.logic_str = f"logic_{self.logic_eval_method}"
        else:
            self.logic_str = "logic_OFF"

        self.path = self.base_dir / f"uq_scores_{self.split}_{self.output_format}_{self.logic_str}.jsonl"
        self.model_path = self.base_dir / f"ensemble_model_bundle_{self.split}_{self.output_format}_{self.logic_str}.pkl"
        self.weights_path = self.base_dir / f"ensemble_weights_{self.split}_{self.output_format}_{self.logic_str}.json"

        if not self.path.exists():
            print(f"❌ Error: Calibration file not found at {self.path}")
            sys.exit(1)

        self.allowed_labels = ["TRUE", "FALSE", "CONFLICTING"] if self.dataset.lower() == "quantemp" else ["SUPPORT", "CONTRADICT", "NOT ENOUGH INFO"]
        
        # Base expected metrics
        self.uq_methods_expected = [
            "MaximumSequenceProbability",
            "Perplexity",
            "MeanTokenEntropy",
        ]

        # Conditionally inject ACE if the flag is enabled!
        if self.check_logic:
            self.uq_methods_expected.append("LogicalContradiction")
            print(f"ACE flag detected ({self.logic_eval_method}): Including 'LogicalContradiction' in feature matrix.")

        # Internal state
        self.data_lines = []
        self.X_raw = None
        self.y_target = None
        self.valid_indices = []
        self.max_finite_replacements = {}

    def load_data(self):
        """Reads JSONL and constructs feature matrix X and target array y."""
        with open(self.path, 'r') as f:
            for line in f:
                try:
                    self.data_lines.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

        X_list = []
        y_list = []

        for i, d in enumerate(self.data_lines):
            gold = clean_label(d.get('gold_label', 'NOT ENOUGH INFO'))
            para = clean_label(d.get('parametric_verdict', 'NOT ENOUGH INFO'))
            
            if para not in self.allowed_labels:
                continue
                
            uq_scores = d.get('uq_scores', {})
            
            feat = []
            for method in self.uq_methods_expected:
                val = uq_scores.get(method)
                if val is None or not isinstance(val, (int, float)) or np.isnan(val):
                    feat.append(np.inf)
                else:
                    feat.append(float(val))
                    
            X_list.append(feat)
            y_list.append(1 if gold != para else 0)  # Error = 1, Correct = 0
            self.valid_indices.append(i)

        self.X_raw = np.array(X_list)
        self.y_target = np.array(y_list)
        
        if len(self.X_raw) == 0:
            print("❌ Error: No valid data for ensemble training.")
            sys.exit(1)

        print(f"✅ Loaded {len(self.X_raw)} valid samples for calibration.")

    def resolve_missing_values(self):
        """Finds max finite scores for replacements, accounting for both positive and negative bounds."""
        for j, method in enumerate(self.uq_methods_expected):
            col = self.X_raw[:, j]
            finite_mask = np.isfinite(col)
            
            if np.any(finite_mask):
                max_val = float(np.max(col[finite_mask]))
                replacement = max_val + np.abs(max_val) * 0.5 + 1e-3
            else:
                replacement = 0.0 
                
            self.max_finite_replacements[method] = replacement
            self.X_raw[~finite_mask, j] = replacement
            
        print(f"✅ Resolved infinite/NaN bounds.")

    def run_cross_validation(self) -> np.ndarray:
        """Executes 5-Fold Stratified CV to generate unbiased cross-validation ensemble predictions."""
        print(f"⏳ Training Ensemble LR via Cross-Validation on {len(self.X_raw)} calibration lines...")
        cross_val_predictions = np.zeros(len(self.X_raw))
        
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=self.seed)
        for train_idx, val_idx in skf.split(self.X_raw, self.y_target):
            X_train, X_val = self.X_raw[train_idx], self.X_raw[val_idx]
            y_train = self.y_target[train_idx]

            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_val_scaled = scaler.transform(X_val)

            clf = LogisticRegression(
                class_weight='balanced',
                l1_ratio=0,         # L2 regularization
                solver='lbfgs',
                C=1.0,
                random_state=self.seed,
                max_iter=10000,
            )
            clf.fit(X_train_scaled, y_train)
            cross_val_predictions[val_idx] = clf.predict_proba(X_val_scaled)[:, 1]

        return cross_val_predictions

    def inject_cross_val_predictions(self, cross_val_predictions: np.ndarray):
        """Merges generated unbiased Cross-Validation Ensemble probabilities back into the JSONL file."""
        print("⏳ Injecting unbiased 'Ensemble' probabilities into dataset...")
        for idx_in_valid, orig_idx in enumerate(self.valid_indices):
            d = self.data_lines[orig_idx]
            if "uq_scores" not in d:
                d["uq_scores"] = {}
            d["uq_scores"]["Ensemble"] = float(cross_val_predictions[idx_in_valid])
            
        with open(self.path, 'w') as f:
            for d in self.data_lines:
                f.write(json.dumps(d) + "\n")
        print("✅ Injection complete.")


    def train_final_model(self):
        """Trains Logistic Regression on 100% of data and packages the model state."""
        print("📦 Exporting final StandardScaler and LogisticRegression model...")
        final_scaler = StandardScaler()
        X_raw_scaled = final_scaler.fit_transform(self.X_raw)

        final_clf = LogisticRegression(
            class_weight='balanced',
            l1_ratio=0,         # L2 regularization
            solver='lbfgs',
            C=1.0,
            random_state=self.seed,
            max_iter=10000,
        )
        final_clf.fit(X_raw_scaled, self.y_target)

        # Coefficient-based weight representations
        raw_weights = final_clf.coef_[0]
        feature_stds = final_scaler.scale_
        standardized_weights = raw_weights * feature_stds

        abs_std = np.abs(standardized_weights)
        total_abs = float(np.sum(abs_std))
        if total_abs > 0:
            relative_importance = abs_std / total_abs
        else:
            relative_importance = np.zeros_like(abs_std)

        # SHAP-based importance
        print("🔍 Computing SHAP values...")
        explainer = shap.Explainer(final_clf, X_raw_scaled, feature_names=self.uq_methods_expected)
        explanation = explainer(X_raw_scaled)
        shap_values = explanation.values  # (n_samples, n_features)

        mean_abs_shap = np.abs(shap_values).mean(axis=0)
        mean_signed_shap = shap_values.mean(axis=0)
        total_shap = float(mean_abs_shap.sum())
        shap_share = mean_abs_shap / total_shap if total_shap > 0 else np.zeros_like(mean_abs_shap)

        # Build combined per-feature JSON dict
        weights_dict = {}
        for j, feat in enumerate(self.uq_methods_expected):
            weights_dict[feat] = {
                "raw": float(raw_weights[j]),
                "standardized": float(standardized_weights[j]),
                "share": float(relative_importance[j]),
                "shap_mean_abs": float(mean_abs_shap[j]),
                "shap_mean_signed": float(mean_signed_shap[j]),
                "shap_share": float(shap_share[j]),
            }

        with open(self.weights_path, 'w') as f:
            json.dump(weights_dict, f, indent=2)
        print(f"✅ Feature weights JSON saved to: {self.weights_path.relative_to(ROOT_DIR)}")

        # Global SHAP visualizations
        print("📊 Generating SHAP summary plots...")
        plot_dir = self.base_dir / "shap_plots"
        plot_dir.mkdir(parents=True, exist_ok=True)
        suffix = f"{self.split}_{self.output_format}_{self.logic_str}"

        # Swap raw feature values into the Explanation for human-readable display
        display_explanation = shap.Explanation(
            values=explanation.values,
            base_values=explanation.base_values,
            data=self.X_raw,
            feature_names=self.uq_methods_expected,
        )

        plt.figure()
        shap.plots.bar(display_explanation, max_display=len(self.uq_methods_expected), show=False)
        bar_path = plot_dir / f"shap_bar_{suffix}.png"
        plt.savefig(bar_path, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"   • Bar plot: {bar_path.relative_to(ROOT_DIR)}")

        plt.figure()
        shap.plots.beeswarm(display_explanation, max_display=len(self.uq_methods_expected), show=False)
        beeswarm_path = plot_dir / f"shap_beeswarm_{suffix}.png"
        plt.savefig(beeswarm_path, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"   • Beeswarm plot: {beeswarm_path.relative_to(ROOT_DIR)}")

        model_bundle = {
            "scaler": final_scaler,
            "model": final_clf,
            "max_finite_replacements": self.max_finite_replacements,
            "features": self.uq_methods_expected,
        }
        with open(self.model_path, 'wb') as f:
            pickle.dump(model_bundle, f)
        print(f"✅ Model bundle saved to: {self.model_path.relative_to(ROOT_DIR)}\n")


    def execute_pipeline(self):
        """Primary orchestrator for the Ensembler."""
        self.load_data()
        self.resolve_missing_values()
        cv_preds = self.run_cross_validation()
        self.inject_cross_val_predictions(cv_preds)
        self.train_final_model()


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--split", required=True)
    parser.add_argument("--model", required=True)
    
    parser.add_argument("--check_logic", action="store_true", help="Whether to expect LogicalContradiction scores")
    parser.add_argument("--output_format", type=str, default="label_only", help="Format suffix of the target file")
    parser.add_argument("--logic_eval_method", type=str, choices=["discrete", "probabilistic"], default="discrete", help="Evaluation method for the logical contradiction")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")

    args, _ = parser.parse_known_args()

    ensembler = UQEnsembler(
        dataset=args.dataset, 
        split=args.split, 
        model_name=args.model,
        check_logic=args.check_logic,
        output_format=args.output_format,
        logic_eval_method=args.logic_eval_method,
        seed=args.seed
    )
    ensembler.execute_pipeline()

if __name__ == "__main__":
    main()