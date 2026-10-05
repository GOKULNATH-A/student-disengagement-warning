# System Architecture

## Student Disengagement Early-Warning System

### 1. Architecture Overview

The system is designed as a low-cost, transparent early-warning prototype that combines multiple student learning signals to identify students who may require additional support.

The architecture consists of data generation, preprocessing, exploratory analysis, baseline comparison, machine learning, evaluation, failure analysis, and a Streamlit dashboard.

---

## 2. End-to-End Architecture

```text
                    ┌─────────────────────────┐
                    │   Synthetic Student     │
                    │      Data Sources       │
                    │                         │
                    │ Attendance               │
                    │ LMS Activity             │
                    │ Assignments              │
                    │ Assessments              │
                    │ Help Requests            │
                    │ Feedback                 │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Data Generation      │
                    │  src/data_generator.py  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Raw Dataset          │
                    │ data/raw/                │
                    │ student_engagement.csv   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Data Preprocessing     │
                    │ src/preprocessing.py     │
                    │                         │
                    │ Missing values           │
                    │ Duplicate checks         │
                    │ Range validation        │
                    │ Data cleaning            │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Clean Dataset          │
                    │ data/processed/          │
                    │ student_engagement_      │
                    │ clean.csv                │
                    └────────────┬────────────┘
                                 │
                ┌────────────────┴────────────────┐
                │                                 │
                ▼                                 ▼
     ┌─────────────────────┐           ┌─────────────────────┐
     │ Exploratory Data    │           │ Attendance-only     │
     │ Analysis            │           │ Baseline            │
     │ notebooks/01_eda.py │           │ notebooks/02_...    │
     └──────────┬──────────┘           └──────────┬──────────┘
                │                                 │
                └────────────────┬────────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │  Multi-Signal Machine   │
                    │  Learning Model          │
                    │                         │
                    │ Random Forest            │
                    │ models/train_model.py   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       Evaluation         │
                    │                         │
                    │ Accuracy                 │
                    │ Precision                │
                    │ Recall                   │
                    │ F1 Score                 │
                    │ Baseline comparison      │
                    └────────────┬────────────┘
                                 │
                ┌────────────────┴────────────────┐
                │                                 │
                ▼                                 ▼
     ┌─────────────────────┐           ┌─────────────────────┐
     │ Failure Analysis    │           │ Edge Case Testing   │
     │ False Positives      │           │ Hidden disengagement│
     │ False Negatives      │           │ Low attendance      │
     │ Uncertain cases      │           │ Conflicting signals │
     └──────────┬──────────┘           └──────────┬──────────┘
                │                                 │
                └────────────────┬────────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │   Streamlit Dashboard   │
                    │       app/app.py        │
                    │                         │
                    │ Risk Level              │
                    │ Risk Probability        │
                    │ Prediction Confidence   │
                    │ Learning Signals        │
                    │ Evidence                │
                    │ Support Recommendation  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Human Review        │
                    │                         │
                    │ Academic / Student       │
                    │ Support Team             │
                    │                         │
                    │ Support-focused action   │
                    └─────────────────────────┘

