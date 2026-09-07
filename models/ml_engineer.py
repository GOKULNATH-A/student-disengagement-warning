import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ---------------------------------------------------------
# 1. Load cleaned dataset
# ---------------------------------------------------------

file_path = "data/processed/student_engagement_clean.csv"

df = pd.read_csv(file_path)

print("=" * 70)
print("MULTI-SIGNAL DISENGAGEMENT MODEL")
print("=" * 70)

print("\nDataset shape:")
print(df.shape)


# ---------------------------------------------------------
# 2. Define features
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


print("\nFeatures used:")
for feature in features:
    print("-", feature)


# ---------------------------------------------------------
# 3. Train-test split
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


# ---------------------------------------------------------
# 4. Create Random Forest model
# ---------------------------------------------------------

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    min_samples_leaf=10,
    random_state=42,
    class_weight="balanced"
)


# ---------------------------------------------------------
# 5. Train model
# ---------------------------------------------------------

print("\nTraining Random Forest...")

model.fit(
    X_train,
    y_train
)

print("Training completed.")


# ---------------------------------------------------------
# 6. Predictions
# ---------------------------------------------------------

y_pred = model.predict(X_test)

y_probability = model.predict_proba(X_test)[:, 1]


# ---------------------------------------------------------
# 7. Model evaluation
# ---------------------------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

cm = confusion_matrix(
    y_test,
    y_pred
)


# ---------------------------------------------------------
# 8. Print performance
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("MODEL PERFORMANCE")
print("=" * 70)

print(f"\nAccuracy : {accuracy:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall   : {recall:.3f}")
print(f"F1 Score : {f1:.3f}")

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "No Disengagement",
            "Disengagement"
        ],
        zero_division=0
    )
)


# ---------------------------------------------------------
# 9. Feature importance
# ---------------------------------------------------------

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")

print(importance)


# ---------------------------------------------------------
# 10. Save feature importance
# ---------------------------------------------------------

os.makedirs(
    "models",
    exist_ok=True
)

importance.to_csv(
    "models/feature_importance.csv",
    index=False
)


# ---------------------------------------------------------
# 11. Save model
# ---------------------------------------------------------

model_file = "models/disengagement_model.pkl"

joblib.dump(
    model,
    model_file
)

print("\nModel saved to:")
print(model_file)


# ---------------------------------------------------------
# 12. Save test predictions
# ---------------------------------------------------------

test_results = X_test.copy()

test_results["actual_label"] = y_test.values

test_results["predicted_label"] = y_pred

test_results["confidence"] = np.maximum(
    y_probability,
    1 - y_probability
)

test_results["risk_probability"] = y_probability

test_results.to_csv(
    "models/test_predictions.csv",
    index=False
)

print("\nTest predictions saved to:")
print("models/test_predictions.csv")


# ---------------------------------------------------------
# 13. Save metrics
# ---------------------------------------------------------

metrics = pd.DataFrame({
    "Model": ["Multi-signal Random Forest"],
    "Accuracy": [accuracy],
    "Precision": [precision],
    "Recall": [recall],
    "F1_Score": [f1],
    "Test_Samples": [len(X_test)]
})

metrics.to_csv(
    "models/model_metrics.csv",
    index=False
)

print("\nMetrics saved to:")
print("models/model_metrics.csv")


print("\n" + "=" * 70)
print("MULTI-SIGNAL MODEL TRAINING COMPLETED")
print("=" * 70)
