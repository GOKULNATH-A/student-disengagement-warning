import os
import pandas as pd
import joblib

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_model_exists():
    assert os.path.exists(os.path.join(BASE, "models", "disengagement_model.pkl"))

def test_dataset_exists_and_has_10000_rows():
    path = os.path.join(BASE, "data", "processed", "student_engagement_clean.csv")
    assert os.path.exists(path)
    df = pd.read_csv(path)
    assert len(df) == 10000

def test_required_columns_exist():
    path = os.path.join(BASE, "data", "processed", "student_engagement_clean.csv")
    df = pd.read_csv(path)
    required = {
        "student_id", "programme", "semester", "attendance_rate",
        "lms_logins", "lms_activity_minutes", "assignment_completion_rate",
        "late_submissions", "assessment_score", "help_requests",
        "feedback_score", "disengagement_label"
    }
    assert required.issubset(df.columns)

def test_model_has_eight_features():
    model = joblib.load(os.path.join(BASE, "models", "disengagement_model.pkl"))
    assert len(model.feature_importances_) == 8

def test_final_phase_files_exist():
    paths = [
        "notebooks/07_final_validation.py",
        "notebooks/08_monitoring_simulation.py",
        "src/explainability.py",
        "src/privacy_audit.py"
    ]
    assert all(os.path.exists(os.path.join(BASE, p)) for p in paths)
