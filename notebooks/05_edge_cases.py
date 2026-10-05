import pandas as pd
import numpy as np
import joblib

print("=" * 70)
print("EDGE AND FAILURE CASE ANALYSIS")
print("=" * 70)

# ---------------------------------------------------------
# 1. Load trained model
# ---------------------------------------------------------

model = joblib.load(
    "models/disengagement_model.pkl"
)

# ---------------------------------------------------------
# 2. Features used by model
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

# ---------------------------------------------------------
# 3. Create three realistic scenarios
# ---------------------------------------------------------

cases = pd.DataFrame([

    {
        "case": "Case 1 - Hidden Disengagement",
        "attendance_rate": 92,
        "lms_logins": 4,
        "lms_activity_minutes": 55,
        "assignment_completion_rate": 45,
        "late_submissions": 4,
        "assessment_score": 48,
        "help_requests": 4,
        "feedback_score": 2.2
    },

    {
        "case": "Case 2 - Low Attendance but Engaged",
        "attendance_rate": 65,
        "lms_logins": 18,
        "lms_activity_minutes": 280,
        "assignment_completion_rate": 92,
        "late_submissions": 0,
        "assessment_score": 88,
        "help_requests": 0,
        "feedback_score": 4.5
    },

    {
        "case": "Case 3 - Conflicting Signals",
        "attendance_rate": 78,
        "lms_logins": 10,
        "lms_activity_minutes": 160,
        "assignment_completion_rate": 60,
        "late_submissions": 2,
        "assessment_score": 70,
        "help_requests": 2,
        "feedback_score": 3.0
    }

])

# ---------------------------------------------------------
# 4. Baseline prediction
# ---------------------------------------------------------

cases["baseline_flag"] = (
    cases["attendance_rate"] < 75
).astype(int)

# ---------------------------------------------------------
# 5. Multi-signal model prediction
# ---------------------------------------------------------

X_cases = cases[features]

predictions = model.predict(
    X_cases
)

probabilities = model.predict_proba(
    X_cases
)[:, 1]

confidence = np.maximum(
    probabilities,
    1 - probabilities
)

cases["model_prediction"] = predictions

cases["risk_probability"] = probabilities

cases["confidence"] = confidence

# ---------------------------------------------------------
# 6. Risk level
# ---------------------------------------------------------

def get_risk(probability):

    if probability >= 0.70:
        return "High"

    elif probability >= 0.40:
        return "Medium"

    else:
        return "Low"


cases["risk_level"] = cases[
    "risk_probability"
].apply(get_risk)

# ---------------------------------------------------------
# 7. Interpretation
# ---------------------------------------------------------

cases["interpretation"] = [
    "Baseline may miss hidden disengagement because attendance is high.",
    "Baseline may over-flag the student because attendance is low.",
    "Multiple signals conflict, so human review is appropriate."
]

# ---------------------------------------------------------
# 8. Display results
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("EDGE CASE RESULTS")
print("=" * 70)

for _, row in cases.iterrows():

    print("\n" + "-" * 70)

    print(row["case"])

    print("-" * 70)

    print(
        f"Attendance              : "
        f"{row['attendance_rate']}%"
    )

    print(
        f"LMS Activity            : "
        f"{row['lms_activity_minutes']} minutes"
    )

    print(
        f"Assignment Completion   : "
        f"{row['assignment_completion_rate']}%"
    )

    print(
        f"Assessment Score        : "
        f"{row['assessment_score']}"
    )

    print(
        f"Help Requests           : "
        f"{row['help_requests']}"
    )

    print(
        f"Feedback Score          : "
        f"{row['feedback_score']}"
    )

    print(
        f"\nAttendance Baseline     : "
        f"{'FLAGGED' if row['baseline_flag'] == 1 else 'NOT FLAGGED'}"
    )

    print(
        f"Multi-Signal Prediction : "
        f"{'DISENGAGED' if row['model_prediction'] == 1 else 'NOT DISENGAGED'}"
    )

    print(
        f"Risk Probability        : "
        f"{row['risk_probability']:.2%}"
    )

    print(
        f"Confidence              : "
        f"{row['confidence']:.2%}"
    )

    print(
        f"Risk Level              : "
        f"{row['risk_level']}"
    )

    print(
        f"\nInterpretation          : "
        f"{row['interpretation']}"
    )

# ---------------------------------------------------------
# 9. Save results
# ---------------------------------------------------------

cases.to_csv(
    "models/edge_case_results.csv",
    index=False
)

print("\n" + "=" * 70)
print("EDGE CASE ANALYSIS COMPLETED")
print("=" * 70)

print(
    "\nSaved to:"
)

print(
    "models/edge_case_results.csv"
)
