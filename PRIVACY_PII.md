# Privacy and PII Safeguards

The prototype avoids unnecessary personal information.

## Current dataset
The synthetic dataset uses a generated student ID and learning-signal fields. It does not require names, email addresses, phone numbers, free-text messages or government identifiers.

## Audit
`src/privacy_audit.py` checks for common direct identifiers and sensitive free-text columns.

## Production controls
- Use pseudonymous student IDs.
- Minimise collected fields.
- Avoid storing raw counselling/help-seeking text unless strictly necessary.
- Apply access control and encryption.
- Define retention and deletion rules.
- Log model access and administrative actions.
- Provide human review and a support/appeal path.
- Never use the risk score as the sole basis for punitive academic decisions.

Privacy compliance must be reviewed against institutional policy and applicable law before real-data deployment.
