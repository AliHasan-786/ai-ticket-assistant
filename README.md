# 🛠️ AI-Powered IT Ticket Automation Tool

This is a Streamlit-based application that uses a local LLM (Mistral via Ollama) and LangChain to generate structured Jira service tickets from natural language input.

## 🔧 Features
- Converts IT issues into structured JSON tickets
- Uses LangChain for prompt templating
- Sends tickets directly to Jira via REST API
- Clean, minimal Streamlit interface

## 📦 Requirements
- Python 3.9+
- Streamlit
- LangChain
- Ollama (running Mistral)
- Jira account with API token

## 🚀 How to Run
1. Start Mistral via Ollama:
   ```bash
   ollama run mistral
2. Run the Streamlit app: streamlit run main.py

3. Enter an IT issue and submit!

