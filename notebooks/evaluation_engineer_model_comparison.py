import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

print("=" * 70)
print("FAIR BASELINE VS MULTI-SIGNAL MODEL COMPARISON")
print("=" * 70)

# ---------------------------------------------------------
# 1. Load cleaned dataset
# ---------------------------------------------------------

df = pd.read_csv(
    "data/processed/student_engagement_clean.csv"
)

# ---------------------------------------------------------
# 2. Features
# ---------------------------------------------------------

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

target = "disengagement_label"

X = df[features]
y = df[target]

# ---------------------------------------------------------
# 3. SAME test split for both models
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples :", len(X_test))

# =========================================================
# BASELINE
# =========================================================

# Attendance below 75% = support needed

baseline_pred = (
    X_test["attendance_rate"] < 75
).astype(int)

baseline_accuracy = accuracy_score(
    y_test,
    baseline_pred
)

baseline_precision = precision_score(
    y_test,
    baseline_pred,
    zero_division=0
)

baseline_recall = recall_score(
    y_test,
    baseline_pred,
    zero_division=0
)

baseline_f1 = f1_score(
    y_test,
    baseline_pred,
    zero_division=0
)

baseline_cm = confusion_matrix(
    y_test,
    baseline_pred
)

# =========================================================
# MULTI-SIGNAL RANDOM FOREST
# =========================================================

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    min_samples_leaf=10,
    random_state=42,
    class_weight="balanced"
)

model.fit(
    X_train,
    y_train
)

model_pred = model.predict(X_test)

model_accuracy = accuracy_score(
    y_test,
    model_pred
)

model_precision = precision_score(
    y_test,
    model_pred,
    zero_division=0
)

model_recall = recall_score(
    y_test,
    model_pred,
    zero_division=0
)

model_f1 = f1_score(
    y_test,
    model_pred,
    zero_division=0
)

model_cm = confusion_matrix(
    y_test,
    model_pred
)

# =========================================================
# COMPARISON TABLE
# =========================================================

comparison = pd.DataFrame({
    "Model": [
        "Attendance-only Baseline",
        "Multi-Signal Random Forest"
    ],
    "Accuracy": [
        baseline_accuracy,
        model_accuracy
    ],
    "Precision": [
        baseline_precision,
        model_precision
    ],
    "Recall": [
        baseline_recall,
        model_recall
    ],
    "F1_Score": [
        baseline_f1,
        model_f1
    ]
})

print("\n" + "=" * 70)
print("MODEL COMPARISON")
print("=" * 70)

print(
    comparison.to_string(index=False)
)

# =========================================================
# IMPROVEMENT
# =========================================================

f1_improvement = (
    (model_f1 - baseline_f1)
    / baseline_f1
) * 100

recall_improvement = (
    (model_recall - baseline_recall)
    / baseline_recall
) * 100

print("\n" + "=" * 70)
print("IMPROVEMENT")
print("=" * 70)

print(
    f"\nF1 improvement    : {f1_improvement:.2f}%"
)

print(
    f"Recall improvement: {recall_improvement:.2f}%"
)

# =========================================================
# CONFUSION MATRICES
# =========================================================

print("\n" + "=" * 70)
print("BASELINE CONFUSION MATRIX")
print("=" * 70)

print(baseline_cm)

print("\n" + "=" * 70)
print("MODEL CONFUSION MATRIX")
print("=" * 70)

print(model_cm)

# =========================================================
# SUPPORT FLAGS
# =========================================================

baseline_flagged = baseline_pred.sum()
model_flagged = model_pred.sum()
actual_disengaged = y_test.sum()

print("\n" + "=" * 70)
print("SUPPORT IDENTIFICATION")
print("=" * 70)

print(
    f"\nActual disengaged students in test set: "
    f"{actual_disengaged}"
)

print(
    f"Students flagged by baseline: "
    f"{baseline_flagged}"
)

print(
    f"Students flagged by multi-signal model: "
    f"{model_flagged}"
)

# =========================================================
# SAVE RESULTS
# =========================================================

comparison.to_csv(
    "notebooks/model_comparison.csv",
    index=False
)

print("\nComparison saved to:")
print("notebooks/model_comparison.csv")

print("\n" + "=" * 70)
print("FAIR COMPARISON COMPLETED")
print("=" * 70)
