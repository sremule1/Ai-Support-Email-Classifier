# AI Support Email Classifier

This project is a complete end-to-end mini system that uses AI to read customer support emails and automatically sort them into helpful categories such as Billing, Technical Issue, Account Help, Complaint, and Other.

Instead of manually reading through each message, the system uses an AI model to understand the content of every email, assign it to the correct category, save the results, and then display simple insights in an interactive dashboard.

This shows how AI can streamline customer support by reducing workload and helping teams prioritize issues more efficiently.


---


![AI Dashboard Screenshot](./AI%20screenshot.png)

















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
🧠 How It Works (Step-by-Step)
1️⃣ Input Data

The project starts with a CSV file named emails.csv

Contains a single column: email_text

2️⃣ Classify Emails

classify_emails.py:

Loads emails using Pandas

Processes each message through classify_email(text)

Current version uses a rule-based classifier (offline, no API required)

Assigns one of the following labels:

Billing

Technical Issue

Account Help

Complaint

Other

3️⃣ Save Results

Output is written to classified_emails.csv

Includes:

Original email

Predicted category

4️⃣ Visualize in a Dashboard

app.py (Streamlit):

Loads classified_emails.csv

Shows:

A bar chart of email category counts

A table displaying all classified messages

Dashboard runs locally at:
http://localhost:8501

🚀 Installation & Running the App
1️⃣ Clone the Repository
git clone https://github.com/sremule1/Ai-Support-Email-Classifier.git
cd Ai-Support-Email-Classifier

2️⃣ Create & Activate a Virtual Environment
python -m venv venv
.\venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ (Optional) Add Your OpenAI API Key

Only required if upgrading to LLM-based classification:

$env:OPENAI_API_KEY="your_api_key_here"

5️⃣ Run the Classifier
python classify_emails.py

6️⃣ Launch the Dashboard
streamlit run app.py

## 📁 Project Structure (target)

```text
Ai-Support-Email-Classifier/
│
├── data/
│   └── emails.csv              # sample raw emails
│
├── src/
│   ├── classify_emails.py      # uses AI to label each email
│   └── app.py                  # Streamlit dashboard
│
├── requirements.txt
└── README.md


