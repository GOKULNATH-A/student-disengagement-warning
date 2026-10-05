# Risk Register

## Student Disengagement Early-Warning System

This risk register identifies technical, ethical, data, and operational risks associated with the early-warning prototype.

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R1 | Attendance-only decisions may miss hidden disengagement | High | High | Use multiple learning signals instead of attendance alone |
| R2 | Model produces false positives | Medium | Medium | Require human review before intervention |
| R3 | Model produces false negatives | Medium | High | Monitor recall and perform regular failure analysis |
| R4 | Conflicting signals may produce misleading predictions | Medium | High | Display individual learning signals and require staff review |
| R5 | Prediction confidence may be misunderstood as certainty | Medium | High | Clearly label confidence as a model indicator, not guaranteed certainty |
| R6 | Synthetic data may not represent real student behaviour | High | High | Validate using appropriately governed real-world data before deployment |
| R7 | Missing or incorrect data may affect predictions | Medium | High | Perform data validation and missing-value handling |
| R8 | Student privacy could be compromised | Low | High | Use access controls, data minimisation and secure storage |
| R9 | Students may be unfairly labelled as disengaged | Medium | High | Use predictions only as support signals, not automatic decisions |
| R10 | Staff may rely too heavily on model predictions | Medium | High | Provide evidence, confidence and human-review requirements |
| R11 | Model performance may change over time | Medium | Medium | Periodically evaluate model performance and retrain when appropriate |
| R12 | System may be difficult to maintain | Low | Medium | Use open-source Python tools and a reproducible project structure |
| R13 | Data leakage may produce unrealistically high performance | Medium | High | Use proper train/test separation and document synthetic-label limitations |
| R14 | Stakeholder requirements may differ from technical assumptions | Medium | Medium | Conduct stakeholder validation before real deployment |
| R15 | Automated recommendations may not suit every student | Medium | High | Treat recommendations as suggestions and allow staff judgement |

---

## 1. Risk Priority

The highest-priority risks are:

### Data Representativeness

The current dataset is synthetic. Its patterns may not accurately represent real university students.

**Mitigation:**  
Validate the approach using appropriately governed institutional data before deployment.

### False Negatives

A disengaged student may not be identified by the system.

**Mitigation:**  
Monitor recall, analyse false negatives and use additional staff-led support processes.

### False Positives

An engaged student may incorrectly receive a high-risk prediction.

**Mitigation:**  
Require human review and avoid automatic punitive action.

### Privacy

Student engagement data can contain sensitive information.

**Mitigation:**  
Use data minimisation, access control, secure storage and appropriate institutional privacy policies.

### Over-reliance on Predictions

Staff may treat model predictions as definitive decisions.

**Mitigation:**  
Show evidence and confidence, clearly communicate limitations, and require human judgement.

---

## 2. Ethical Safeguards

The prototype follows these principles:

- Human-in-the-loop decision making.
- Supportive rather than punitive use.
- Transparent evidence.
- Risk and confidence displayed separately.
- Explicit acknowledgement of uncertainty.
- No automatic disciplinary action.
- Synthetic data for the prototype.
- Privacy-aware design.

---

## 3. Risk Monitoring

For a real deployment, the following should be monitored regularly:

- Accuracy
- Precision
- Recall
- F1 Score
- False-positive rate
- False-negative rate
- Prediction confidence
- Data quality
- Changes in student engagement patterns
- Stakeholder feedback

---

## 4. Risk Acceptance

The current prototype is suitable for demonstration and technical evaluation using synthetic data.

It should **not** be treated as a production-ready student decision system until:

1. Real-world data is appropriately validated.
2. Stakeholder validation is completed.
3. Privacy and governance requirements are reviewed.
4. Model performance is evaluated on representative data.
5. Bias and fairness are assessed.
6. Operational monitoring is established.
