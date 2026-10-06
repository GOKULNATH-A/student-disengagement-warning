import os
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE, "models", "disengagement_model.pkl")
pred_path = os.path.join(BASE, "models", "test_predictions.csv")

model = joblib.load(model_path)
pred = pd.read_csv(pred_path)

target_col = "actual" if "actual" in pred.columns else "disengagement_label"
prediction_col = "prediction" if "prediction" in pred.columns else "predicted"

y_true = pred[target_col]
y_pred = pred[prediction_col]

metrics = {
    "accuracy": accuracy_score(y_true, y_pred),
    "precision": precision_score(y_true, y_pred, zero_division=0),
    "recall": recall_score(y_true, y_pred, zero_division=0),
    "f1": f1_score(y_true, y_pred, zero_division=0),
}

cm = confusion_matrix(y_true, y_pred)
out_dir = os.path.join(BASE, "models")
os.makedirs(out_dir, exist_ok=True)

pd.DataFrame([metrics]).to_csv(
    os.path.join(out_dir, "final_validation_metrics.csv"), index=False
)

pd.DataFrame(
    cm,
    index=["Actual 0", "Actual 1"],
    columns=["Predicted 0", "Predicted 1"],
).to_csv(os.path.join(out_dir, "final_confusion_matrix.csv"))

print("FINAL VALIDATION")
for key, value in metrics.items():
    print(f"{key.title():10}: {value:.4f}")
print("\nConfusion Matrix:")
print(cm)
print("\nSaved final validation outputs to models/")
