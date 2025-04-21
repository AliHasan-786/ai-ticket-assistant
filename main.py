import streamlit as st
from langchain_community.llms import Ollama 
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from ticket import gen_ticket
import json


llm = Ollama(model="mistral", temperature=0.0)

prompt = """
You are a highly capable AI assistant that writes structured Jira service tickets.

Given a user's input describing an IT problem, generate a valid **JSON object** with exactly these two fields:
- "Title": A short, specific issue title (max 10 words)
- "Summary": A clear explanation of the problem in full sentences

Rules:
- ONLY return valid JSON. No preamble, no explanation.
- Use plain English. Don’t use placeholders like "user" — use real names if given.
- If urgency is implied (e.g. "asap", "urgent"), reflect that in the summary.
- Do NOT include anything outside the JSON block.

Example input:
"Alice’s email isn’t working, and she’s not receiving any messages. Please fix this ASAP."

Example output:
{{ 
  "Title": "Email Issue for Alice",
  "Summary": "Alice is unable to receive emails, which is impacting her work. Please resolve this issue urgently."
}}

Now process this input:
{instruction}
"""

def generate_response(input):
    query_with_prompt = PromptTemplate(
        template=prompt,
        input_variables=["instruction"]
    )
    chain = LLMChain(llm=llm, prompt=query_with_prompt, verbose=True)
    response = chain.invoke({"instruction": input})
    data = response["text"]
    data = data.replace("json", "").strip()
    try:
        data = json.loads(data)
    except json.JSONDecodeError:
        st.error("⚠️ Could not parse a valid JSON response. Please try a simpler input or rephrase.")
        return None
    return data

st.title("🛠️ AI-Driven Service Desk Analyst")
st.write("Describe your IT issue below, and I’ll help create a service ticket for you.")

input = st.text_area("Enter your issue here")
if input:
    if st.button("Submit"):
        response = generate_response(input)
        if response:
            st.subheader("📋 Parsed Ticket Info")
            st.json(response)
            ticket = gen_ticket(response)
            st.subheader("🧾 Generated Ticket")
            st.write(ticket)

