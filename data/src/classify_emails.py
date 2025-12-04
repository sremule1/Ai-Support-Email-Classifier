import pandas as pd
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_email(text):
    prompt = f"Classify the following customer support email into one of these: Billing, Technical Issue, Account Help, Complaint, Other.\nEmail: {text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

df = pd.read_csv("data/emails.csv")

df["category"] = df["email_text"].apply(classify_email)

df.to_csv("classified_emails.csv", index=False)

print("Classification complete. Results saved to classified_emails.csv!")
