import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_kpis(df):
    # Placeholder logic for KPIs
    return {
        "Total Sales": round(df.iloc[:, 1].sum(), 2),
        "Average Monthly Sales": round(df.iloc[:, 1].mean(), 2),
        "Unique Regions": df.iloc[:, 2].nunique(),
    }

def ask_ai_about_data(df, question):
    prompt = f"""
You are a business analyst. Here is a preview of the dataset:
{df.head(20).to_string(index=False)}

Now answer this user question based on the data:
Q: {question}
A:
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()
