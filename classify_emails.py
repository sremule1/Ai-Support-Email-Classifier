import pandas as pd

def simple_rule_based_classifier(text: str) -> str:
    """
    Very simple offline classifier based on keywords.
    This does NOT call any API, so it works without credits.
    """

    t = text.lower()

    if any(word in t for word in ["refund", "charged twice", "billing", "invoice", "credit card"]):
        return "Billing"

    if any(word in t for word in ["password", "log in", "login", "sign in", "account locked", "username"]):
        return "Account Help"

    if any(word in t for word in ["error", "crash", "bug", "not working", "issue", "problem", "fail"]):
        return "Technical Issue"

    if any(word in t for word in ["complaint", "angry", "upset", "terrible", "bad service"]):
        return "Complaint"

    return "Other"


def classify_email(text: str) -> str:
    # For now we just call the simple offline classifier.
    # In the future, this is where you would plug in the OpenAI API again.
    return simple_rule_based_classifier(text)


# ---- Main script ----

# Read input CSV of emails
df = pd.read_csv("data/emails.csv")

# Apply the classifier to each email_text
df["category"] = df["email_text"].apply(classify_email)

# Save to a new CSV
df.to_csv("classified_emails.csv", index=False)

print("✅ Classification complete (offline). Results saved to classified_emails.csv!")

