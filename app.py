#College Enquiry Chatbot
import streamlit as st
from transformers import pipeline

chatbot_model = pipeline("text-generation", model="distilgpt2")


college_data = """
Courses: BTech (CSE, AI, Mechanical), MBA, BBA
Fees: BTech - 2 lakh/year, MBA - 3 lakh/year
Hostel: Available for boys and girls
Transport: Bus available from nearby cities
Events: Annual fest, tech fest, sports events
Attendance: Minimum 75% required
Placement: Average 6 LPA
"""

def chatbot(question):
    prompt = f"""
You are a college enquiry assistant. Answer clearly and only using this data:

{college_data}

Question: {question}
Answer:
"""
    response = chatbot_model(prompt, max_length=200, num_return_sequences=1)
    return response[0]['generated_text'].split("Answer:")[-1]


st.set_page_config(page_title="College Chatbot", page_icon="🎓")

st.title("🎓 College Enquiry Chatbot")
st.caption("Ask about fees, hostel, transport, events, etc.")

user_input = st.text_input("Ask your question:")

if user_input:
    answer = chatbot(user_input)
    st.write("🤖", answer)
