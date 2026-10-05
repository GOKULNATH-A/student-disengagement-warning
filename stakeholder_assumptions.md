# Stakeholder Assumptions and Validation

## 1. Purpose

The Student Disengagement Early-Warning System is designed to help university staff identify students who may benefit from early academic or student-support intervention.

The system is intended to support human decision-making rather than replace staff judgement.

---

## 2. Key Stakeholders

### Students

Students are the primary people affected by the system.

Expected benefit:

- Earlier access to appropriate support.
- Reduced risk of disengagement.
- Support based on multiple learning signals rather than attendance alone.

### Academic Staff

Academic staff may use the system to identify students who may need academic support.

Expected benefit:

- Earlier identification of potential disengagement.
- Better understanding of multiple learning signals.
- Reduced reliance on attendance as the only indicator.

### Student Support Team

Student support staff may use risk information to prioritise outreach.

Expected benefit:

- Better prioritisation of students requiring support.
- Evidence-based follow-up.
- Ability to review the signals contributing to a risk prediction.

### Programme / University Management

Management may use aggregated results to understand engagement patterns and evaluate the effectiveness of support workflows.

Expected benefit:

- Improved visibility of engagement trends.
- Evidence for improving student-support processes.
- Low-cost prototype suitable for small organisations.

---

## 3. Stakeholder Assumptions

The following assumptions were made while designing the prototype:

1. Student engagement is influenced by multiple factors.
2. Attendance alone may not capture all forms of disengagement.
3. LMS activity can provide additional evidence of engagement.
4. Assignment completion and late submissions can indicate changes in academic participation.
5. Assessment performance can provide useful academic context.
6. Help-seeking behaviour may provide additional support-related information.
7. Student feedback can provide another engagement signal.
8. Staff should be able to understand why a student has been flagged.
9. Model predictions should include a risk probability and confidence indicator.
10. Predictions should be reviewed by humans before intervention.
11. The system should support students rather than automatically punish them.
12. The prototype should be feasible using low-cost and open-source technologies.

---

## 4. Stakeholder Needs

| Stakeholder | Main Need | System Support |
|---|---|---|
| Students | Timely support | Early identification |
| Academic Staff | Identify students needing attention | Risk dashboard |
| Support Team | Prioritise outreach | Risk level and evidence |
| Programme Management | Monitor workflow effectiveness | Model evaluation and comparison |
| Data/IT Team | Maintain the system | Reproducible Python pipeline |

---

## 5. Validation Questions

Before real-world deployment, the following questions should be discussed with stakeholders:

### Academic Staff

- Are the selected learning signals useful for identifying disengagement?
- Is attendance being given too much or too little importance?
- Are the recommended support actions appropriate?
- Is the dashboard easy to understand?

### Student Support Team

- Does the risk ranking help prioritise outreach?
- Is the evidence shown by the system sufficient for staff review?
- What additional information would be useful?
- What actions should be taken for High, Medium and Low risk students?

### Students

- Would early supportive outreach be useful?
- Are there concerns about privacy or automated predictions?
- How should students be informed about the use of engagement data?
- What safeguards should be provided?

### Management

- Does the system improve the existing workflow?
- Are the evaluation metrics sufficient?
- Can the solution be operated with existing infrastructure?
- What governance requirements are necessary?

---

## 6. Proposed Validation Method

A small stakeholder validation exercise can be performed using representative dashboard scenarios.

Participants can review:

1. A high-attendance student showing hidden disengagement.
2. A low-attendance student showing strong engagement.
3. A student with conflicting learning signals.

For each scenario, stakeholders can assess:

- Whether the risk level appears reasonable.
- Whether the displayed evidence is understandable.
- Whether the recommended action is appropriate.
- Whether human review is necessary.
- Whether the system provides more useful information than attendance alone.

---

## 7. Validation Success Criteria

The prototype will be considered useful if stakeholders agree that:

- Multiple signals provide useful additional context.
- The dashboard is understandable.
- Risk predictions can be reviewed using supporting evidence.
- The system can help prioritise student-support workflows.
- The system does not automatically make punitive decisions.
- Uncertain or conflicting cases can be escalated for human review.

---

## 8. Current Prototype Validation Status

The current project provides technical validation through:

- Synthetic dataset generation.
- Data cleaning and validation.
- Exploratory data analysis.
- Attendance-only baseline comparison.
- Multi-signal Random Forest model.
- Test-set evaluation.
- Failure analysis.
- Confidence analysis.
- Three edge-case scenarios.
- Interactive Streamlit dashboard.

Actual stakeholder validation requires review by real academic or student-support staff.

No real stakeholder feedback is claimed unless such a review has been conducted.

---

## 9. Responsible Use

The system is an early-warning decision-support tool.

It must not be used to:

- Automatically penalise students.
- Automatically deny academic opportunities.
- Make disciplinary decisions without human review.
- Treat model predictions as facts.
- Infer sensitive personal characteristics without appropriate justification.

The purpose of the system is to help staff identify students who may benefit from timely and appropriate support.