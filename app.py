import os
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="AI Support Email Classifier", layout="wide")

st.title("📧 AI Support Email Classifier Dashboard")
st.write(
    "This dashboard shows the categories assigned to support emails. "
    "Run `python src/classify_emails.py` first to generate `classified_emails.csv`."
)

csv_path = "classified_emails.csv"

if not os.path.exists(csv_path):
    st.error("`classified_emails.csv` not found. Please run `python src/classify_emails.py` first.")
else:
    df = pd.read_csv(csv_path)

    st.subheader("📊 Category counts")

    counts = df["category"].value_counts().reset_index()
    counts.columns = ["category", "count"]

    fig = px.bar(counts, x="category", y="count", title="Number of emails per category")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📄 Sample classified emails")
    st.dataframe(df.head(20))