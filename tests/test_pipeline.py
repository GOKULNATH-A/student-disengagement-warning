import os
import pandas as pd
import joblib


# ============================================================
# 1. File existence tests
# ============================================================

def test_raw_dataset_exists():
    assert os.path.exists(
        "data/raw/student_engagement.csv"
    )


def test_clean_dataset_exists():
    assert os.path.exists(
        "data/processed/student_engagement_clean.csv"
    )


def test_model_exists():
    assert os.path.exists(
        "models/disengagement_model.pkl"
    )


# ============================================================
# 2. Dataset structure tests
# ============================================================

def test_dataset_has_expected_columns():

    df = pd.read_csv(
        "data/processed/student_engagement_clean.csv"
    )

    expected_columns = [
        "student_id",
        "programme",
        "semester",
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

    assert list(df.columns) == expected_columns


# ============================================================
# 3. Dataset size test
# ============================================================

def test_dataset_has_10000_rows():

    df = pd.read_csv(
        "data/processed/student_engagement_clean.csv"
    )

    assert len(df) == 10000


# ============================================================
# 4. Data quality tests
# ============================================================

def test_attendance_range():

    df = pd.read_csv(
        "data/processed/student_engagement_clean.csv"
    )

    assert df["attendance_rate"].between(0, 100).all()


def test_assessment_range():

    df = pd.read_csv(
        "data/processed/student_engagement_clean.csv"
    )

    assert df["assessment_score"].between(0, 100).all()


def test_assignment_completion_range():

    df = pd.read_csv(
        "data/processed/student_engagement_clean.csv"
    )

    assert df["assignment_completion_rate"].between(0, 100).all()


def test_feedback_range():

    df = pd.read_csv(
        "data/processed/student_engagement_clean.csv"
    )

    assert df["feedback_score"].between(1, 5).all()


def test_target_values():

    df = pd.read_csv(
        "data/processed/student_engagement_clean.csv"
    )

    assert set(
        df["disengagement_label"].unique()
    ).issubset({0, 1})


# ============================================================
# 5. Missing value test
# ============================================================

def test_no_missing_values():

    df = pd.read_csv(
        "data/processed/student_engagement_clean.csv"
    )

    assert df.isnull().sum().sum() == 0


# ============================================================
# 6. Model loading test
# ============================================================

def test_model_can_be_loaded():

    model = joblib.load(
        "models/disengagement_model.pkl"
    )

    assert model is not None


# ============================================================
# 7. Model feature count test
# ============================================================

def test_model_has_expected_features():

    model = joblib.load(
        "models/disengagement_model.pkl"
    )

    assert model.n_features_in_ == 8


# ============================================================
# 8. Workflow experiment output test
# ============================================================

def test_workflow_experiment_exists():

    assert os.path.exists(
        "models/workflow_experiment.csv"
    )


def test_workflow_experiment_has_two_workflows():

    df = pd.read_csv(
        "models/workflow_experiment.csv"
    )

    assert len(df) == 2
    