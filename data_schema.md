# Data Schema

## 1. Dataset Overview

The Student Disengagement Early-Warning System uses a synthetic student engagement dataset containing multiple learning and support signals.

The dataset is designed to demonstrate how combining multiple signals can identify students who may require academic or wellbeing support more effectively than using attendance alone.

- Dataset type: Synthetic
- Number of records: 10,000 students
- Number of columns: 12
- Target variable: `disengagement_label`

---

## 2. Data Fields

| Column | Data Type | Range / Example | Description | Role |
|---|---|---|---|---|
| `student_id` | String | S0001 | Unique student identifier | Identifier |
| `programme` | String | Computer Science | Student's academic programme | Input |
| `semester` | Integer | 1–8 | Current semester | Input |
| `attendance_rate` | Float | 0–100 | Percentage of classes attended | Input |
| `lms_logins` | Integer | 0+ | Number of LMS login sessions | Input |
| `lms_activity_minutes` | Integer | 0+ | Time spent interacting with LMS | Input |
| `assignment_completion_rate` | Float | 0–100 | Percentage of assignments completed | Input |
| `late_submissions` | Integer | 0+ | Number of late assignment submissions | Input |
| `assessment_score` | Float | 0–100 | Assessment performance score | Input |
| `help_requests` | Integer | 0+ | Number of academic/support requests | Input |
| `feedback_score` | Float | 1–5 | Student feedback/engagement score | Input |
| `disengagement_label` | Integer | 0 or 1 | Indicates potential disengagement | Target |

---

## 3. Target Variable

### `disengagement_label`

The target variable represents whether a student is classified as potentially disengaged.

```text
0 = Not disengaged
1 = Potentially disengaged