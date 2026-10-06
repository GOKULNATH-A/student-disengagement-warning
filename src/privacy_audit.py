import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE, "data", "processed", "student_engagement_clean.csv")
df = pd.read_csv(path)

direct_identifiers = {"name", "email", "phone", "address", "dob", "aadhaar", "passport"}
sensitive_text = {"message", "chat", "transcript", "notes"}

columns_lower = {c.lower() for c in df.columns}
found_identifiers = sorted(columns_lower & direct_identifiers)
found_sensitive_text = sorted(columns_lower & sensitive_text)

status = "PASS" if not found_identifiers and not found_sensitive_text else "REVIEW REQUIRED"

print("PRIVACY / PII AUDIT")
print(f"Rows checked: {len(df)}")
print(f"Direct identifier columns: {found_identifiers or 'None'}")
print(f"Sensitive free-text columns: {found_sensitive_text or 'None'}")
print(f"Audit status: {status}")

pd.DataFrame([{
    "rows_checked": len(df),
    "direct_identifier_columns": ", ".join(found_identifiers) or "None",
    "sensitive_text_columns": ", ".join(found_sensitive_text) or "None",
    "status": status
}]).to_csv(os.path.join(BASE, "models", "privacy_audit.csv"), index=False)
