import openai
from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY", None)

if api_key is None:
    import streamlit as st
    api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

def ask_ai_about_data(df, user_question):
    prompt = f"""
    You are a data analyst assistant. Given this dataset:\n\n
    {df.head(10).to_string(index=False)}\n\n
    Question: {user_question}\n
    Provide a helpful and concise business insight.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
