import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

print("=" * 70)
print("CONFIDENCE AND FAILURE ANALYSIS")
print("=" * 70)

# ---------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------

df = pd.read_csv(
    "data/processed/student_engagement_clean.csv"
)

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
# 2. Same test split used in comparison
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ---------------------------------------------------------
# 3. Load trained model
# ---------------------------------------------------------

model = joblib.load(
    "models/disengagement_model.pkl"
)

# ---------------------------------------------------------
# 4. Predictions and probabilities
# ---------------------------------------------------------

predictions = model.predict(X_test)

probabilities = model.predict_proba(X_test)[:, 1]

confidence = np.maximum(
    probabilities,
    1 - probabilities
)

# ---------------------------------------------------------
# 5. Create analysis dataframe
# ---------------------------------------------------------

analysis = X_test.copy()

analysis["actual_label"] = y_test.values

analysis["predicted_label"] = predictions

analysis["risk_probability"] = probabilities

analysis["confidence"] = confidence

# ---------------------------------------------------------
# 6. Risk levels
# ---------------------------------------------------------

def risk_level(probability):

    if probability >= 0.70:
        return "High"

    elif probability >= 0.40:
        return "Medium"

    else:
        return "Low"


analysis["risk_level"] = (
    analysis["risk_probability"]
    .apply(risk_level)
)

# ---------------------------------------------------------
# 7. Prediction correctness
# ---------------------------------------------------------

analysis["correct"] = (
    analysis["actual_label"]
    == analysis["predicted_label"]
)

# ---------------------------------------------------------
# 8. Error type
# ---------------------------------------------------------

def error_type(row):

    if row["actual_label"] == 0 and row["predicted_label"] == 1:
        return "False Positive"

    elif row["actual_label"] == 1 and row["predicted_label"] == 0:
        return "False Negative"

    else:
        return "Correct"


analysis["error_type"] = analysis.apply(
    error_type,
    axis=1
)

# ---------------------------------------------------------
# 9. Print confidence summary
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("CONFIDENCE SUMMARY")
print("=" * 70)

print(
    "\nAverage confidence:",
    round(analysis["confidence"].mean(), 3)
)

print(
    "Minimum confidence:",
    round(analysis["confidence"].min(), 3)
)

print(
    "Maximum confidence:",
    round(analysis["confidence"].max(), 3)
)

# ---------------------------------------------------------
# 10. Risk distribution
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("RISK LEVEL DISTRIBUTION")
print("=" * 70)

print(
    analysis["risk_level"]
    .value_counts()
)

# ---------------------------------------------------------
# 11. Error distribution
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("ERROR ANALYSIS")
print("=" * 70)

print(
    analysis["error_type"]
    .value_counts()
)

# ---------------------------------------------------------
# 12. Confusion matrix
# ---------------------------------------------------------

cm = confusion_matrix(
    y_test,
    predictions
)

print("\n" + "=" * 70)
print("CONFUSION MATRIX")
print("=" * 70)

print(cm)

# ---------------------------------------------------------
# 13. False Positives
# ---------------------------------------------------------

false_positives = analysis[
    analysis["error_type"]
    == "False Positive"
].copy()

print("\n" + "=" * 70)
print("FALSE POSITIVE EXAMPLES")
print("=" * 70)

print(
    false_positives[
        [
            "attendance_rate",
            "lms_activity_minutes",
            "assessment_score",
            "help_requests",
            "feedback_score",
            "risk_probability",
            "confidence"
        ]
    ].head(5)
)

# ---------------------------------------------------------
# 14. False Negatives
# ---------------------------------------------------------

false_negatives = analysis[
    analysis["error_type"]
    == "False Negative"
].copy()

print("\n" + "=" * 70)
print("FALSE NEGATIVE EXAMPLES")
print("=" * 70)

print(
    false_negatives[
        [
            "attendance_rate",
            "lms_activity_minutes",
            "assessment_score",
            "help_requests",
            "feedback_score",
            "risk_probability",
            "confidence"
        ]
    ].head(5)
)

# ---------------------------------------------------------
# 15. Uncertain cases
# ---------------------------------------------------------

uncertain = analysis[
    analysis["confidence"] < 0.60
].copy()

print("\n" + "=" * 70)
print("UNCERTAIN / BORDERLINE CASES")
print("=" * 70)

print(
    "Number of uncertain cases:",
    len(uncertain)
)

print(
    uncertain[
        [
            "attendance_rate",
            "lms_activity_minutes",
            "assessment_score",
            "help_requests",
            "feedback_score",
            "risk_probability",
            "confidence",
            "risk_level"
        ]
    ].head(10)
)

# ---------------------------------------------------------
# 16. Save complete analysis
# ---------------------------------------------------------

analysis.to_csv(
    "models/failure_analysis.csv",
    index=False
)

print("\nAnalysis saved to:")
print("models/failure_analysis.csv")

print("\n" + "=" * 70)
print("FAILURE ANALYSIS COMPLETED")
print("=" * 70)
