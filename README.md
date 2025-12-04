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
