import pandas as pd
import os

# ---------------------------------------------------------
# 1. Load raw dataset
# ---------------------------------------------------------

input_file = "data/raw/student_engagement.csv"

df = pd.read_csv(input_file)

print("=" * 60)
print("DATA CLEANING AND VALIDATION")
print("=" * 60)

print("\nOriginal dataset shape:")
print(df.shape)

# ---------------------------------------------------------
# 2. Check missing values
# ---------------------------------------------------------

print("\nMissing values:")
print(df.isnull().sum())

# ---------------------------------------------------------
# 3. Check duplicate rows
# ---------------------------------------------------------

duplicates = df.duplicated().sum()

print("\nDuplicate rows:")
print(duplicates)

# Remove duplicates if any
df = df.drop_duplicates()

# ---------------------------------------------------------
# 4. Check invalid values
# ---------------------------------------------------------

print("\nChecking invalid values...")

invalid_attendance = (
    (df["attendance_rate"] < 0) |
    (df["attendance_rate"] > 100)
).sum()

invalid_feedback = (
    (df["feedback_score"] < 1) |
    (df["feedback_score"] > 5)
).sum()

invalid_assessment = (
    (df["assessment_score"] < 0) |
    (df["assessment_score"] > 100)
).sum()

invalid_assignment = (
    (df["assignment_completion_rate"] < 0) |
    (df["assignment_completion_rate"] > 100)
).sum()

invalid_lms = (
    (df["lms_logins"] < 0) |
    (df["lms_activity_minutes"] < 0)
).sum()

invalid_help = (
    df["help_requests"] < 0
).sum()

invalid_late = (
    df["late_submissions"] < 0
).sum()

print(f"Invalid attendance values: {invalid_attendance}")
print(f"Invalid feedback values: {invalid_feedback}")
print(f"Invalid assessment values: {invalid_assessment}")
print(f"Invalid assignment values: {invalid_assignment}")
print(f"Invalid LMS values: {invalid_lms}")
print(f"Invalid help requests: {invalid_help}")
print(f"Invalid late submissions: {invalid_late}")

# ---------------------------------------------------------
# 5. Handle missing numerical values
# ---------------------------------------------------------

numeric_columns = [
    "attendance_rate",
    "lms_logins",
    "lms_activity_minutes",
    "assignment_completion_rate",
    "late_submissions",
    "assessment_score",
    "help_requests",
    "feedback_score"
]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# ---------------------------------------------------------
# 6. Handle missing categorical values
# ---------------------------------------------------------

df["programme"] = df["programme"].fillna("Unknown")

df["semester"] = df["semester"].fillna(
    df["semester"].median()
)

# ---------------------------------------------------------
# 7. Ensure correct data types
# ---------------------------------------------------------

df["student_id"] = df["student_id"].astype(str)
df["programme"] = df["programme"].astype(str)

# ---------------------------------------------------------
# 8. Final validation
# ---------------------------------------------------------

print("\nFinal missing values:")
print(df.isnull().sum())

print("\nFinal dataset shape:")
print(df.shape)

# ---------------------------------------------------------
# 9. Save processed dataset
# ---------------------------------------------------------

output_dir = "data/processed"

os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(
    output_dir,
    "student_engagement_clean.csv"
)

df.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)

print(f"Processed file saved to:")
print(output_file)

print("\nFinal dataset preview:")
print(df.head())