# AI Support Email Classifier

This project is a small end-to-end demo that uses AI to automatically
classify customer support emails into categories like **Billing**,
**Technical Issue**, **Account Help**, **Complaint**, and **Other**, then
shows simple analytics in a dashboard.

> Perfect portfolio project for an Information Systems student who wants
> a role in AI / data / product at companies like Google or Apple.

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
🧠 How it works (step-by-step)

1. **Input data**
   - The project starts with a CSV file: `emails.csv`
   - It has one column: `email_text` with raw customer support messages.

2. **Classify emails**
   - `classify_emails.py` reads `emails.csv` with pandas.
   - For each row, it calls `classify_email(text)` which uses a **simple rule-based classifier** (offline, no API required) to assign one of these labels:
     - `Billing`
     - `Technical Issue`
     - `Account Help`
     - `Complaint`
     - `Other`

3. **Save results**
   - The script writes a new file: `classified_emails.csv`
   - This file contains the original email text plus the predicted category.

4. **Visualize in a dashboard**
   - `app.py` (Streamlit) loads `classified_emails.csv`.
   - It:
     - Counts how many emails fall into each category.
     - Displays a bar chart using Plotly.
     - Shows a table of sample classified emails.
   - The dashboard runs locally in the browser at `http://localhost:8501`.

---
## 🚀 Deployment / Running instructions

### 1. Clone the repo

```bash
git clone https://github.com/sremule1/Ai-Support-Email-Classifier.git
cd Ai-Support-Email-Classifier
---
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


