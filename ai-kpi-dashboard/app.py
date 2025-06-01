import streamlit as st
import pandas as pd
import plotly.express as px
from kpi_analyzer import analyze_kpis, ask_ai_about_data
from utils import load_data
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="AI-Powered KPI Dashboard", layout="wide")
st.title("📊 AI-Powered Business KPI Dashboard")

uploaded_file = st.file_uploader("Upload your business CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.success("Data loaded successfully!")
    st.subheader("📌 Raw Data Preview")
    st.dataframe(df.head())

    # KPI Analysis
    st.subheader("📈 KPI Summary")
    kpis = analyze_kpis(df)
    for kpi, value in kpis.items():
        st.metric(label=kpi, value=value)

    # Visualizations
    st.subheader("📊 Visual Insights")
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(px.line(df, x=df.columns[0], y=df.columns[1], title="Sales Trend"))
    with col2:
        st.plotly_chart(px.bar(df, x=df.columns[2], y=df.columns[1], title="Region-wise Sales"))

    # AI Assistant
    st.subheader("💬 Ask the AI about your data")
    user_question = st.text_input("What do you want to know?", placeholder="e.g. Why did sales drop in March?")
    if user_question:
        ai_response = ask_ai_about_data(df, user_question)
        st.markdown(f"**AI Insight:** {ai_response}")
