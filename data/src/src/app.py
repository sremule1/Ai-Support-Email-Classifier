import streamlit as st
import pandas as pd
import plotly.express as px

st.title("AI Support Email Classifier Dashboard")

df = pd.read_csv("classified_emails.csv")

fig = px.histogram(df, x="category", title="Email Categories")
st.plotly_chart(fig)

st.subheader("Sample Emails and Classifications")
st.dataframe(df.head(10))
