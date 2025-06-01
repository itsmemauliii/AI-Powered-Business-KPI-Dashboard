# AI-Powered KPI Dashboard

This project is a smart business intelligence tool that uses AI to provide KPI summaries, data visualizations, and natural language answers to business questions.

## 🔧 Tech Stack
- Python
- Streamlit
- Pandas
- Plotly
- OpenAI (ChatGPT API)

## 📁 How to Use
1. Clone the repo
```bash
git clone https://github.com/your-username/ai-kpi-dashboard.git
cd ai-kpi-dashboard
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Add your OpenAI API key to your environment
```bash
export OPENAI_API_KEY=your_api_key_here
```
4. Run the app
```bash
streamlit run app.py
```

## 📂 Sample Data
Put your CSV or Excel data in the `sample_data/` folder. Use columns like:
- `Date`
- `Sales`
- `Region`

## ✅ Features
- Upload sales or business metric data
- Get KPI summary cards
- Visualize trends and regional insights
- Ask AI questions like: “Why did sales drop in Q1?”

## ✨ Future Enhancements
- Forecasting module
- Support for PDFs & Google Sheets
- Auto data cleaning using LLM

---
Built with ❤️ by Mauli Patel
