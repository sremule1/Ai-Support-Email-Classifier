# AI Support Email Classifier

This project is a complete end-to-end mini system that uses AI to read customer support emails and automatically sort them into helpful categories such as Billing, Technical Issue, Account Help, Complaint, and Other.

Instead of manually reading through each message, the system uses an AI model to understand the content of every email, assign it to the correct category, save the results, and then display simple insights in an interactive dashboard.

This shows how AI can streamline customer support by reducing workload and helping teams prioritize issues more efficiently.


---


## 📸 AI Dashboard Screenshot
<p align="center">
  <img src="./AI screenshot.png" width="900">
</p>





## 🧩 Features


- Upload or load a CSV file of sample support emails  
- Use an LLM (e.g. OpenAI GPT) to classify each email  
- Save the classified results to a new CSV  
- View counts per category in a simple Streamlit dashboard  

---

## 🛠 Tech Stack

- **Python** (3.9+)
- **Pandas** for data handling  
- **OpenAI API** (or another LLM API) for classification  
- **Streamlit** for the dashboard


---

## 🧠 How it works (step-by-step)

## 1.   Input Data

- Project begins with emails.csv

- Contains one column: email_text

## 2️.  Classify Emails

 classify_emails.py:

    - Loads data with Pandas

    - Uses classify_email(text) (rule-based, offline)

    - Assigns one of:

          - Billing

          - Technical Issue

          - Account Help

          - Complaint

          - Other

## 3️.  Save Results

  Output is saved to classified_emails.csv

  Includes:

    - Original message

    - Predicted category

## 4️.  Visualize in Dashboard

app.py (Streamlit):

  Loads the classified CSV

  Shows:

        - A bar chart of categories

        - A table of labeled emails

Runs at:

👉 http://localhost:8501

---
## 🚀 Deployment / Running instructions

## 1️⃣Clone the Repository

git clone https://github.com/...
cd Ai-Support-Email-Classifier

## 2️⃣Create & Activate a Virtual Environment

python -m venv venv
.\venv\Scripts\activate

## 3️⃣Install Dependencies

pip install -r requirements.txt

## 4️⃣(Optional) Add Your OpenAI API Key

Only needed if you upgrade to real AI classification:

$env:OPENAI_API_KEY="your_api_key_here"

## 5️⃣Run the Classifier

python classify_emails.py

## 6️⃣Launch the Dashboard

streamlit run app.py
---


## 📁 Project Structure (target)

```text
```text
Ai-Support-Email-Classifier/
│
├── data/                      # (optional folder for datasets)
├── emails.csv                 # sample raw emails
├── classified_emails.csv      # sample classified output
├── classify_emails.py         # email classifier script
├── app.py                     # Streamlit dashboard
├── AI screenshot.png          # dashboard screenshot
├── requirements.txt
└── README.md


