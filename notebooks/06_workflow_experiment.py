import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib


# ============================================================
# 1. Load cleaned dataset
# ============================================================

DATA_PATH = "data/processed/student_engagement_clean.csv"
MODEL_PATH = "models/disengagement_model.pkl"
OUTPUT_PATH = "models/workflow_experiment.csv"

df = pd.read_csv(DATA_PATH)


# ============================================================
# 2. Define features and target
# ============================================================

features = [
    "attendance_rate",
    "lms_logins",
    "lms_activity_minutes",
    "assignment_completion_rate",
    "late_submissions",
    "assessment_score",
    "help_requests",
    "feedback_score"
]

X = df[features]
y = df["disengagement_label"]


# ============================================================
# 3. Create the same test split used by the ML model
# ============================================================

_, X_test, _, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ============================================================
# 4. Attendance-only baseline
# ============================================================

baseline_predictions = (
    X_test["attendance_rate"] < 75
).astype(int)


# ============================================================
# 5. Multi-signal Random Forest
# ============================================================

model = joblib.load(MODEL_PATH)

model_predictions = model.predict(X_test)


# ============================================================
# 6. Calculate workflow metrics
# ============================================================

def calculate_metrics(y_true, predictions):

    return {
        "Flagged Students": int(predictions.sum()),
        "Actual Disengaged": int(y_true.sum()),
        "True Positives": int(
            ((predictions == 1) & (y_true == 1)).sum()
        ),
        "False Positives": int(
            ((predictions == 1) & (y_true == 0)).sum()
        ),
        "False Negatives": int(
            ((predictions == 0) & (y_true == 1)).sum()
        ),
        "Accuracy": round(
            accuracy_score(y_true, predictions) * 100, 2
        ),
        "Precision": round(
            precision_score(y_true, predictions, zero_division=0) * 100,
            2
        ),
        "Recall": round(
            recall_score(y_true, predictions, zero_division=0) * 100,
            2
        ),
        "F1 Score": round(
            f1_score(y_true, predictions, zero_division=0) * 100,
            2
        )
    }


baseline_metrics = calculate_metrics(
    y_test,
    baseline_predictions
)

model_metrics = calculate_metrics(
    y_test,
    model_predictions
)


# ============================================================
# 7. Create comparison table
# ============================================================

comparison = pd.DataFrame([
    {
        "Workflow": "Attendance-only Baseline",
        **baseline_metrics
    },
    {
        "Workflow": "Multi-Signal Random Forest",
        **model_metrics
    }
])


# ============================================================
# 8. Calculate improvement
# ============================================================

recall_improvement = (
    model_metrics["Recall"]
    - baseline_metrics["Recall"]
)

f1_improvement = (
    model_metrics["F1 Score"]
    - baseline_metrics["F1 Score"]
)

accuracy_improvement = (
    model_metrics["Accuracy"]
    - baseline_metrics["Accuracy"]
)


# ============================================================
# 9. Save results
# ============================================================

comparison.to_csv(
    OUTPUT_PATH,
    index=False
)


# ============================================================
# 10. Display results
# ============================================================

print("\n" + "=" * 70)
print("WORKFLOW EXPERIMENT")
print("=" * 70)

print("\nTest Set Size:", len(X_test))

print("\nComparison:")
print(comparison.to_string(index=False))

print("\n" + "-" * 70)
print("IMPROVEMENT")
print("-" * 70)

print(
    f"Accuracy improvement : +{accuracy_improvement:.2f} percentage points"
)

print(
    f"Recall improvement   : +{recall_improvement:.2f} percentage points"
)

print(
    f"F1 improvement       : +{f1_improvement:.2f} percentage points"
)

print("\nResults saved to:")
print(OUTPUT_PATH)

print("\n" + "=" * 70)
print("WORKFLOW EXPERIMENT COMPLETED")
print("=" * 70)
