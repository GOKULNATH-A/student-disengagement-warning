import os
import pandas as pd
import numpy as np

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE, "data", "processed", "student_engagement_clean.csv")
df = pd.read_csv(data_path)

numeric_cols = [
    "attendance_rate", "lms_logins", "lms_activity_minutes",
    "assignment_completion_rate", "late_submissions",
    "assessment_score", "help_requests", "feedback_score"
]

rows = []
for col in numeric_cols:
    s = df[col]
    rows.append({
        "feature": col,
        "mean": s.mean(),
        "std": s.std(),
        "min": s.min(),
        "max": s.max(),
        "missing": int(s.isna().sum())
    })

monitoring = pd.DataFrame(rows)
monitoring["quality_status"] = np.where(
    (monitoring["missing"] == 0) &
    monitoring["min"].notna() &
    monitoring["max"].notna(),
    "OK",
    "CHECK"
)

out_path = os.path.join(BASE, "models", "monitoring_summary.csv")
monitoring.to_csv(out_path, index=False)

print("MONITORING SUMMARY")
print(monitoring.to_string(index=False))
print(f"\nSaved: {out_path}")
