#College Enquiry Chatbot
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

college_data = """
Courses: BTech (CSE, AI, Mechanical), MBA, BBA
Fees: BTech - 2 lakh/year, MBA - 3 lakh/year

Hostel: Available for boys and girls, AC & Non-AC rooms
Mess: Veg and non-veg food available

Transport: College buses available from nearby cities with annual fee

Events: Annual fest, tech fest, cultural events, sports competitions

Attendance: Minimum 75% required to appear in exams

Library: Digital + physical library with study space

Placement: Average package 6 LPA, top companies visit every year

Admission: Entrance exam + interview
Location: Himachal Pradesh
"""


def chatbot(question):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": f"You are a helpful college assistant. Answer only using this data: {college_data}"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content


st.set_page_config(page_title="College Chatbot", page_icon="🎓", layout="centered")


st.title("🎓 College Enquiry Chatbot")
st.caption("Ask anything about college 📚")


if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


user_input = st.chat_input("Type your question here...")

if user_input:
    
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    
    response = chatbot(user_input)

    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
