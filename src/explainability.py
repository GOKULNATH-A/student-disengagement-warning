import os
import pandas as pd
import joblib

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE, "models", "disengagement_model.pkl")
importance_path = os.path.join(BASE, "models", "feature_importance.csv")

model = joblib.load(model_path)

if os.path.exists(importance_path):
    importance = pd.read_csv(importance_path)
else:
    features = [
        "attendance_rate", "lms_logins", "lms_activity_minutes",
        "assignment_completion_rate", "late_submissions",
        "assessment_score", "help_requests", "feedback_score"
    ]
    importance = pd.DataFrame({
        "feature": features,
        "importance": model.feature_importances_
    })

if "importance" in importance.columns:
    importance = importance.sort_values("importance", ascending=False).reset_index(drop=True)
importance["rank"] = range(1, len(importance) + 1)

out_path = os.path.join(BASE, "models", "explainability_summary.csv")
importance.to_csv(out_path, index=False)

print("FEATURE IMPORTANCE / EXPLAINABILITY")
print(importance.to_string(index=False))
print(f"\nSaved: {out_path}")
print("\nNote: feature importance indicates model contribution, not causation.")
