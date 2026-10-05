import streamlit as st
import pandas as pd
import numpy as np
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Disengagement Early Warning",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# LOAD DATA AND MODEL
# =========================================================

@st.cache_data
def load_data():

    data = pd.read_csv(
        "data/processed/student_engagement_clean.csv"
    )

    return data


@st.cache_resource
def load_model():

    model = joblib.load(
        "models/disengagement_model.pkl"
    )

    return model


df = load_data()
model = load_model()


# =========================================================
# FEATURES
# =========================================================

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


# =========================================================
# CREATE MODEL PREDICTIONS
# =========================================================

X = df[features]

df["risk_probability"] = model.predict_proba(X)[:, 1]

df["prediction"] = model.predict(X)

df["confidence"] = np.maximum(
    df["risk_probability"],
    1 - df["risk_probability"]
)


# =========================================================
# RISK LEVEL
# =========================================================

def get_risk_level(probability):

    if probability >= 0.70:
        return "High"

    elif probability >= 0.40:
        return "Medium"

    else:
        return "Low"


df["risk_level"] = df[
    "risk_probability"
].apply(get_risk_level)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎓 Early Warning System")

st.sidebar.write(
    "Multi-signal student disengagement detection"
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
This prototype uses multiple learning signals.

It does NOT rely on attendance alone.

Signals include:

• Attendance
• LMS activity
• Assignments
• Assessments
• Help-seeking
• Feedback
"""
)


# =========================================================
# MAIN TITLE
# =========================================================

st.title(
    "🎓 Student Disengagement Early-Warning Dashboard"
)

st.write(
    "Transparent, multi-signal support identification "
    "for flexible university programmes."
)


# =========================================================
# DASHBOARD METRICS
# =========================================================

total_students = len(df)

high_risk = (
    df["risk_level"] == "High"
).sum()

medium_risk = (
    df["risk_level"] == "Medium"
).sum()

low_risk = (
    df["risk_level"] == "Low"
).sum()


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Total Students",
        total_students
    )


with col2:

    st.metric(
        "🔴 High Risk",
        high_risk
    )


with col3:

    st.metric(
        "🟡 Medium Risk",
        medium_risk
    )


with col4:

    st.metric(
        "🟢 Low Risk",
        low_risk
    )


# =========================================================
# STUDENT SEARCH
# =========================================================

st.markdown("---")

st.subheader(
    "🔎 Student Risk Review"
)

student_ids = df["student_id"].tolist()

selected_student = st.selectbox(
    "Select Student ID",
    student_ids
)


student = df[
    df["student_id"] == selected_student
].iloc[0]


# =========================================================
# STUDENT RISK SUMMARY
# =========================================================

st.markdown("---")

risk_col, confidence_col = st.columns(2)


with risk_col:

    risk = student["risk_level"]

    if risk == "High":

        st.error(
            f"🔴 HIGH SUPPORT PRIORITY\n\n"
            f"Risk probability: "
            f"{student['risk_probability']:.1%}"
        )

    elif risk == "Medium":

        st.warning(
            f"🟡 MEDIUM SUPPORT PRIORITY\n\n"
            f"Risk probability: "
            f"{student['risk_probability']:.1%}"
        )

    else:

        st.success(
            f"🟢 LOW SUPPORT PRIORITY\n\n"
            f"Risk probability: "
            f"{student['risk_probability']:.1%}"
        )


with confidence_col:

    st.metric(
        "Prediction Confidence",
        f"{student['confidence']:.1%}"
    )

    if student["confidence"] < 0.60:

        st.warning(
            "Borderline prediction — "
            "human review recommended."
        )

    else:

        st.info(
            "Model confidence is above the "
            "borderline threshold."
        )


# =========================================================
# STUDENT PROFILE
# =========================================================

st.markdown("---")

st.subheader(
    "📊 Learning Signals"
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Attendance",
        f"{student['attendance_rate']:.1f}%"
    )


with col2:

    st.metric(
        "LMS Activity",
        f"{student['lms_activity_minutes']:.0f} min"
    )


with col3:

    st.metric(
        "Assessment",
        f"{student['assessment_score']:.1f}"
    )


with col4:

    st.metric(
        "Assignment Completion",
        f"{student['assignment_completion_rate']:.1f}%"
    )


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "LMS Logins",
        f"{student['lms_logins']:.0f}"
    )


with col2:

    st.metric(
        "Late Submissions",
        f"{student['late_submissions']:.0f}"
    )


with col3:

    st.metric(
        "Help Requests",
        f"{student['help_requests']:.0f}"
    )


with col4:

    st.metric(
        "Feedback Score",
        f"{student['feedback_score']:.1f}/5"
    )


# =========================================================
# EVIDENCE / EXPLANATION
# =========================================================

st.markdown("---")

st.subheader(
    "🔍 Evidence Behind the Risk"
)

evidence = []


if student["attendance_rate"] < 75:

    evidence.append(
        "Attendance is below 75%."
    )


if student["lms_activity_minutes"] < 120:

    evidence.append(
        "LMS activity is relatively low."
    )


if student["assignment_completion_rate"] < 60:

    evidence.append(
        "Assignment completion is low."
    )


if student["assessment_score"] < 50:

    evidence.append(
        "Assessment performance is low."
    )


if student["late_submissions"] >= 3:

    evidence.append(
        "Multiple late submissions detected."
    )


if student["help_requests"] >= 3:

    evidence.append(
        "Multiple help requests indicate possible support needs."
    )


if student["feedback_score"] < 3:

    evidence.append(
        "Feedback score indicates lower learner satisfaction."
    )


if len(evidence) == 0:

    evidence.append(
        "No single strong negative signal was detected."
    )


for item in evidence:

    st.write(
        "• " + item
    )


# =========================================================
# SUPPORT RECOMMENDATION
# =========================================================

st.markdown("---")

st.subheader(
    "🤝 Recommended Support Action"
)


if risk == "High":

    st.warning(
        """
Recommended workflow:

1. Advisor reviews the evidence.
2. Contact the student for a check-in.
3. Identify academic or engagement barriers.
4. Offer appropriate support.
5. Record the outcome.

The prediction should NOT automatically trigger
punitive action.
"""
    )

elif risk == "Medium":

    st.info(
        """
Recommended workflow:

1. Review the student's learning signals.
2. Consider a low-intensity check-in.
3. Monitor progress.
4. Escalate only if multiple signals remain concerning.
"""
    )

else:

    st.success(
        """
No immediate intervention recommended.

Continue normal academic monitoring.
"""
    )
    
    # ============================================================
# BEFORE vs AFTER WORKFLOW COMPARISON
# ============================================================

st.markdown("---")

st.header("📈 Before vs After: Workflow Improvement")

st.write(
    "The prototype compares a simple attendance-only baseline "
    "with the proposed multi-signal early-warning model."
)

comparison_data = {
    "Metric": ["Accuracy", "Recall", "F1 Score"],
    "Attendance-only Baseline": [61.5, 31.3, 32.8],
    "Multi-Signal MVP": [88.4, 89.2, 82.2]
}

comparison_df = pd.DataFrame(comparison_data)

st.dataframe(
    comparison_df,
    use_container_width=True,
    hide_index=True
)

st.subheader("🎯 Measured Improvement")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Accuracy Improvement",
        "+26.9 percentage points"
    )

with col2:
    st.metric(
        "Recall Improvement",
        "+57.9 percentage points"
    )

with col3:
    st.metric(
        "F1 Improvement",
        "+49.4 percentage points"
    )

st.info(
    "Workflow impact: instead of relying mainly on attendance, "
    "the MVP combines attendance, LMS activity, assignments, "
    "assessments, help-seeking and feedback to identify students "
    "who may need support."
)
    
    
# =========================================================
# DISCLAIMER
# =========================================================

st.markdown("---")

st.caption(
    "Prototype only — predictions support human decision-making "
    "and should not be used as an automatic punitive decision."
)
