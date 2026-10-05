import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ---------------------------------------------------------
# Load cleaned dataset
# ---------------------------------------------------------

file_path = "data/processed/student_engagement_clean.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("ATTENDANCE-ONLY BASELINE")
print("=" * 60)

print("\nDataset size:")
print(df.shape)

# ---------------------------------------------------------
# Actual labels
# ---------------------------------------------------------

y_actual = df["disengagement_label"]

# ---------------------------------------------------------
# BASELINE RULE
#
# Attendance below 75% = Support Needed
# Attendance 75% or above = No Support Flag
# ---------------------------------------------------------

y_baseline = (
    df["attendance_rate"] < 75
).astype(int)

# ---------------------------------------------------------
# Calculate metrics
# ---------------------------------------------------------

accuracy = accuracy_score(
    y_actual,
    y_baseline
)

precision = precision_score(
    y_actual,
    y_baseline,
    zero_division=0
)

recall = recall_score(
    y_actual,
    y_baseline,
    zero_division=0
)

f1 = f1_score(
    y_actual,
    y_baseline,
    zero_division=0
)

cm = confusion_matrix(
    y_actual,
    y_baseline
)

# ---------------------------------------------------------
# Print results
# ---------------------------------------------------------

print("\nBaseline Rule:")
print("Attendance < 75% = Support Needed")

print("\nBaseline Performance:")
print(f"Accuracy : {accuracy:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall   : {recall:.3f}")
print(f"F1 Score : {f1:.3f}")

# ---------------------------------------------------------
# Confusion Matrix
# ---------------------------------------------------------

print("\nConfusion Matrix:")
print(cm)

# ---------------------------------------------------------
# Classification Report
# ---------------------------------------------------------

print("\nClassification Report:")

print(
    classification_report(
        y_actual,
        y_baseline,
        target_names=[
            "No Disengagement",
            "Disengagement"
        ],
        zero_division=0
    )
)

# ---------------------------------------------------------
# Student counts
# ---------------------------------------------------------

flagged_students = y_baseline.sum()

actual_disengaged = y_actual.sum()

print("\nStudent Counts:")
print(
    f"Students flagged by baseline: {flagged_students}"
)

print(
    f"Actual disengaged students: {actual_disengaged}"
)

# ---------------------------------------------------------
# Save baseline results
# ---------------------------------------------------------

results = pd.DataFrame({
    "Model": ["Attendance-only baseline"],
    "Accuracy": [accuracy],
    "Precision": [precision],
    "Recall": [recall],
    "F1_Score": [f1],
    "Students_Flagged": [flagged_students],
    "Actual_Disengaged": [actual_disengaged]
})

results.to_csv(
    "notebooks/baseline_results.csv",
    index=False
)

print("\nBaseline results saved to:")
print("notebooks/baseline_results.csv")

print("\n" + "=" * 60)
print("BASELINE COMPLETED")
print("=" * 60)
