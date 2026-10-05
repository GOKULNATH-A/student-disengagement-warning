# Student Disengagement Early-Warning System

## Project Report

---

## 1. Project Title

**Student Disengagement Early-Warning System**

A transparent, multi-signal machine learning prototype for early identification of students who may require additional support.

---

## 2. Abstract

Student disengagement is often difficult to identify when universities rely mainly on attendance and assessment marks.

This project develops a transparent early-warning prototype that combines multiple student learning signals, including attendance, Learning Management System (LMS) activity, assignment completion, late submissions, assessment performance, help-seeking behaviour and student feedback.

A synthetic dataset containing 10,000 student records was generated for technical evaluation. The data was cleaned, analysed and used to train a Random Forest classification model.

The proposed multi-signal model was compared with an attendance-only baseline using the same stratified test dataset.

The multi-signal model achieved 88.40% accuracy, 76.21% precision, 89.17% recall and 82.18% F1 score, compared with 61.50% accuracy, 34.43% precision, 31.33% recall and 32.81% F1 score for the attendance-only baseline.

The prototype also provides prediction probability, prediction confidence, supporting learning signals, failure analysis, edge-case testing and a Streamlit dashboard.

The system is designed as a decision-support tool and not as an automatic punitive system.

---

## 3. Problem Statement

Flexible university programmes provide students with multiple elective pathways and different ways of engaging with learning.

Because of this flexibility, early signs of disengagement may not always appear through attendance or marks alone.

A student may:

- Attend classes regularly but stop using the LMS.
- Have low attendance but remain highly engaged with online learning.
- Complete some assessments while becoming less active in other areas.
- Show changes in help-seeking or feedback behaviour.

Therefore, relying on a single indicator can result in both missed students and unnecessary support flags.

The project addresses this problem by combining multiple learning signals into a transparent early-warning workflow.

---

## 4. Project Objectives

The main objectives are:

1. Generate or obtain suitable synthetic student engagement data.
2. Clean and validate the data.
3. Analyse relationships between engagement signals and disengagement.
4. Build an attendance-only baseline.
5. Develop a multi-signal machine learning model.
6. Compare the model with the baseline.
7. Display prediction probability and confidence.
8. Analyse false positives and false negatives.
9. Test important edge cases.
10. Build an interactive dashboard.
11. Demonstrate measurable workflow improvement.
12. Provide documentation, risk analysis and responsible-use guidance.
13. Create a reproducible low-cost prototype.

---

## 5. Dataset

The project uses a synthetic dataset containing:

- 10,000 student records
- 12 columns

### Main Signals

- Attendance rate
- LMS logins
- LMS activity minutes
- Assignment completion rate
- Late submissions
- Assessment score
- Help requests
- Feedback score

### Target

```text
disengagement_label

0 = Not disengaged
1 = Potentially disengaged