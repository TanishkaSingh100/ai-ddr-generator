# AI Detailed Diagnostic Report Generator

This project converts raw inspection reports and thermal imaging reports into a structured Detailed Diagnostic Report (DDR) using AI.

## Features
- Upload inspection and thermal PDF reports
- Extract text and images using PyMuPDF
- AI analyzes reports and generates structured diagnostic insights
- Displays supporting visual evidence

## Tech Stack
- Python
- Streamlit
- PyMuPDF
- LLM via OpenRouter API

## How to Run

1. Clone the repository
2. Install dependencies

   pip install -r requirements.txt

3. Set API key

   export OPENROUTER_API_KEY = your key here

4. Run the app

   streamlit run app.py
