# Student Disengagement Early-Warning System

## 1. Project Overview

This project develops a transparent early-warning prototype for identifying university students who may need academic or engagement support.

The university scenario assumes flexible programmes with multiple elective pathways. In such an environment, disengagement may not be visible through attendance or marks alone.

The prototype combines multiple learning signals:

- Attendance
- LMS logins
- LMS activity
- Assignment completion
- Late submissions
- Assessment performance
- Help-seeking behaviour
- Learner feedback

The system provides a risk level, risk probability, confidence, supporting evidence and a recommended human support workflow.

---

## 2. Problem Statement

Traditional monitoring approaches may rely heavily on attendance or assessment marks.

This can result in:

- Hidden disengagement being missed
- Students with low attendance but strong engagement being unnecessarily flagged
- Conflicting learning signals being ignored
- Lack of evidence behind intervention decisions

The proposed system uses multiple signals to provide a transparent support-priority indication rather than an automatic punitive decision.

---

## 3. Objectives

The project aims to:

1. Generate or obtain synthetic student learning data.
2. Combine multiple learning signals.
3. Create a simple attendance-only baseline.
4. Build a multi-signal machine learning model.
5. Back-test the model against the baseline.
6. Display prediction probability and confidence.
7. Analyse false positives, false negatives and uncertain cases.
8. Demonstrate at least three edge cases.
9. Build a working Streamlit MVP.
10. Demonstrate improvement to a support workflow.
11. Provide reproducible documentation and low-cost infrastructure.

---

## 4. Dataset

A synthetic dataset containing 10,000 student records was generated.

The dataset contains 12 columns:

| Column | Description |
|---|---|
| student_id | Unique student identifier |
| programme | Student programme |
| semester | Current semester |
| attendance_rate | Attendance percentage |
| lms_logins | Number of LMS logins |
| lms_activity_minutes | LMS activity duration |
| assignment_completion_rate | Assignment completion percentage |
| late_submissions | Number of late submissions |
| assessment_score | Assessment score |
| help_requests | Number of help requests |
| feedback_score | Learner feedback score |
| disengagement_label | Synthetic target label |

The data is simulated for prototype and technical feasibility purposes. Results should not be interpreted as findings about a real university population.

---

## 5. Data Pipeline

```text
Synthetic Data Generation
          |
          v
Raw CSV
          |
          v
Data Cleaning and Validation
          |
          v
Processed CSV
          |
          v
Exploratory Data Analysis
          |
          v
Baseline + Machine Learning
          |
          v
Evaluation
          |
          v
Failure Analysis
          |
          v
Streamlit Dashboard