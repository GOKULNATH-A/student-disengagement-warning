import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------
# Load cleaned dataset
# ---------------------------------------------------------

file_path = "data/processed/student_engagement_clean.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nDataset information:")
df.info()

print("\nStatistical summary:")
print(df.describe())

# ---------------------------------------------------------
# Disengagement distribution
# ---------------------------------------------------------

print("\nDisengagement distribution:")
print(df["disengagement_label"].value_counts())

print("\nDisengagement percentage:")
print(
    df["disengagement_label"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

# Create output folder
os.makedirs("notebooks/eda_outputs", exist_ok=True)


# ---------------------------------------------------------
# Function to create and save boxplots
# ---------------------------------------------------------

def create_boxplot(column, title, ylabel, filename):

    fig, ax = plt.subplots(figsize=(8, 5))

    df.boxplot(
        column=column,
        by="disengagement_label",
        ax=ax
    )

    ax.set_title(title)
    ax.set_xlabel("Disengagement Label (0 = No, 1 = Yes)")
    ax.set_ylabel(ylabel)

    # Remove pandas automatic super-title
    fig.suptitle("")

    fig.tight_layout()

    fig.savefig(
        f"notebooks/eda_outputs/{filename}",
        dpi=150,
        bbox_inches="tight"
    )

    plt.close(fig)


# ---------------------------------------------------------
# 1. Attendance
# ---------------------------------------------------------

create_boxplot(
    "attendance_rate",
    "Attendance Rate by Disengagement Status",
    "Attendance Rate (%)",
    "attendance_vs_disengagement.png"
)


# ---------------------------------------------------------
# 2. LMS Activity
# ---------------------------------------------------------

create_boxplot(
    "lms_activity_minutes",
    "LMS Activity by Disengagement Status",
    "LMS Activity Minutes",
    "lms_activity_vs_disengagement.png"
)


# ---------------------------------------------------------
# 3. Assessment
# ---------------------------------------------------------

create_boxplot(
    "assessment_score",
    "Assessment Score by Disengagement Status",
    "Assessment Score",
    "assessment_vs_disengagement.png"
)


# ---------------------------------------------------------
# 4. Help Requests
# ---------------------------------------------------------

create_boxplot(
    "help_requests",
    "Help Requests by Disengagement Status",
    "Number of Help Requests",
    "help_requests_vs_disengagement.png"
)


# ---------------------------------------------------------
# 5. Feedback
# ---------------------------------------------------------

create_boxplot(
    "feedback_score",
    "Feedback Score by Disengagement Status",
    "Feedback Score (1-5)",
    "feedback_vs_disengagement.png"
)


# ---------------------------------------------------------
# 6. Late Submissions
# ---------------------------------------------------------

create_boxplot(
    "late_submissions",
    "Late Submissions by Disengagement Status",
    "Number of Late Submissions",
    "late_submissions_vs_disengagement.png"
)


# ---------------------------------------------------------
# Correlation analysis
# ---------------------------------------------------------

numeric_columns = [
    "attendance_rate",
    "lms_logins",
    "lms_activity_minutes",
    "assignment_completion_rate",
    "late_submissions",
    "assessment_score",
    "help_requests",
    "feedback_score",
    "disengagement_label"
]

correlation = df[numeric_columns].corr()

print("\nCorrelation with disengagement:")

print(
    correlation["disengagement_label"]
    .sort_values(ascending=False)
)


# ---------------------------------------------------------
# Save correlation table
# ---------------------------------------------------------

correlation.to_csv(
    "notebooks/eda_outputs/correlation_matrix.csv"
)


# ---------------------------------------------------------
# Completion
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("EDA COMPLETED")
print("=" * 60)

print("\nGraphs saved in:")
print("notebooks/eda_outputs/")
