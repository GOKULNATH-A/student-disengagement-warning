import pandas as pd
import numpy as np
import os

# Reproducibility
np.random.seed(42)

# Number of students
N = 10000

# Student IDs
student_ids = [f"S{i:04d}" for i in range(1, N + 1)]

# Programmes
programmes = np.random.choice(
    [
        "Computer Science",
        "Business Administration",
        "Data Science",
        "Information Technology",
        "Artificial Intelligence"
    ],
    size=N
)

# Semester
semesters = np.random.randint(1, 9, size=N)

# Attendance
attendance_rate = np.clip(
    np.random.normal(82, 12, N),
    45,
    100
).round(1)

# LMS logins
lms_logins = np.clip(
    np.random.poisson(18, N),
    0,
    50
)

# LMS activity minutes
lms_activity_minutes = np.clip(
    np.random.normal(300, 120, N),
    0,
    700
).round(0)

# Assignment completion
assignment_completion_rate = np.clip(
    np.random.normal(78, 18, N),
    20,
    100
).round(1)

# Late submissions
late_submissions = np.clip(
    np.random.poisson(1.5, N),
    0,
    8
)

# Assessment score
assessment_score = np.clip(
    np.random.normal(68, 15, N),
    20,
    100
).round(1)

# Help-seeking requests
help_requests = np.clip(
    np.random.poisson(1, N),
    0,
    8
)

# Feedback score (1 to 5)
feedback_score = np.clip(
    np.random.normal(3.5, 0.8, N),
    1,
    5
).round(1)

# ---------------------------------------------------------
# Create disengagement tendency using MULTIPLE signals
# ---------------------------------------------------------

risk_score = (
    (100 - attendance_rate) * 0.15
    + (50 - lms_logins) * 0.20
    + (500 - lms_activity_minutes) * 0.10
    + (100 - assignment_completion_rate) * 0.15
    + late_submissions * 3
    + (100 - assessment_score) * 0.15
    + help_requests * 4
    + (5 - feedback_score) * 8
)

# Add small random variation
risk_score += np.random.normal(0, 5, N)

# Convert to binary target
threshold = np.percentile(risk_score, 70)

disengagement_label = (risk_score >= threshold).astype(int)

# ---------------------------------------------------------
# Create special edge-case students
# ---------------------------------------------------------

# Edge Case 1:
# Low attendance but otherwise highly engaged
for i in range(3):
    attendance_rate[i] = 68
    lms_logins[i] = 35
    lms_activity_minutes[i] = 500
    assignment_completion_rate[i] = 95
    late_submissions[i] = 0
    assessment_score[i] = 85
    help_requests[i] = 0
    feedback_score[i] = 4.7
    disengagement_label[i] = 0

# Edge Case 2:
# High attendance but hidden disengagement
for i in range(3, 6):
    attendance_rate[i] = 94
    lms_logins[i] = 5
    lms_activity_minutes[i] = 80
    assignment_completion_rate[i] = 55
    late_submissions[i] = 4
    assessment_score[i] = 48
    help_requests[i] = 4
    feedback_score[i] = 2.2
    disengagement_label[i] = 1

# Edge Case 3:
# Insufficient evidence / new student
for i in range(6, 9):
    attendance_rate[i] = 90
    lms_logins[i] = 2
    lms_activity_minutes[i] = 30
    assignment_completion_rate[i] = 100
    late_submissions[i] = 0
    assessment_score[i] = 75
    help_requests[i] = 0
    feedback_score[i] = 4.0
    disengagement_label[i] = 0

# Create dataframe
df = pd.DataFrame({
    "student_id": student_ids,
    "programme": programmes,
    "semester": semesters,
    "attendance_rate": attendance_rate,
    "lms_logins": lms_logins,
    "lms_activity_minutes": lms_activity_minutes,
    "assignment_completion_rate": assignment_completion_rate,
    "late_submissions": late_submissions,
    "assessment_score": assessment_score,
    "help_requests": help_requests,
    "feedback_score": feedback_score,
    "disengagement_label": disengagement_label
})

# Create output directory
output_dir = os.path.join("data", "raw")
os.makedirs(output_dir, exist_ok=True)

# Save dataset
output_file = os.path.join(output_dir, "student_engagement.csv")
df.to_csv(output_file, index=False)

print("Dataset created successfully!")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print(f"Saved to: {output_file}")

print("\nFirst 5 rows:")
print(df.head())

print("\nDisengagement distribution:")
print(df["disengagement_label"].value_counts())