# Deployment and Operational Readiness

## Prototype
Run the dashboard with:

`python -m streamlit run app/app.py`

## Runtime flow
1. Load the trained Random Forest model.
2. Load processed learning-signal data.
3. Generate risk probability.
4. Assign Low / Medium / High support priority.
5. Display evidence from multiple signals.
6. Route high-risk or uncertain cases to human support staff.

## Responsible use
This is a support-prioritisation tool, not a disciplinary or grading system. A high-risk result should trigger supportive review rather than automatic action.

## Monitoring
The final phase includes data-quality monitoring, model-metric retention, explainability output and a privacy audit.

## Low-cost feasibility
The prototype uses Python, pandas, scikit-learn, joblib and Streamlit. No paid cloud service is required for local execution.

## Production upgrades
Before real deployment, add authentication, role-based access, encrypted storage, calibrated probabilities, drift monitoring, fairness testing, formal privacy review and stakeholder acceptance testing.
