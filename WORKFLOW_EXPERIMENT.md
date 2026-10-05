# Workflow Experiment

## Student Disengagement Early-Warning System

## 1. Experiment Objective

The objective of this experiment is to determine whether a multi-signal disengagement warning workflow provides better identification of potentially disengaged students than a simple attendance-only workflow.

The experiment compares:

1. Attendance-only baseline
2. Multi-signal Random Forest model

Both approaches are evaluated on the same stratified test set.

---

## 2. Experimental Setup

Dataset:

- Synthetic student engagement dataset
- 10,000 student records
- 12 columns

Test split:

- 20% of the dataset
- 2,000 students
- Stratified by the target label
- Random state: 42

The same test set is used for both the baseline and machine learning model to ensure a fair comparison.

---

## 3. Baseline Workflow

The baseline uses attendance as the primary warning signal.

Rule:

```text
attendance_rate < 75%
        ↓
Flag student for support
