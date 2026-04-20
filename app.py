#College Enquiry Chatbot
import streamlit as st

st.set_page_config(page_title="College Chatbot", page_icon="🎓", layout="centered")

st.title("🎓 College Enquiry Assistant")
st.markdown("Welcome! Ask anything about admissions, campus life, or facilities.")

st.sidebar.title("Quick Enquiries")
quick_options = [
    "Courses offered",
    "Fees structure",
    "Hostel facilities",
    "Transport",
    "Events",
    "Attendance criteria",
    "Placements",
    "Admission process"
]

selected_option = st.sidebar.radio("Choose a topic:", quick_options)

def chatbot(question):
    q = question.lower()

    if any(word in q for word in ["course", "program", "degree"]):
        return """📚 **Courses Offered**
- BTech (CSE, AI, Mechanical)
- MBA
- BBA

Specializations available with industry-focused curriculum."""

    elif any(word in q for word in ["fee", "fees", "cost", "price"]):
        return """💰 **Fee Structure**
- BTech: ₹2,00,000 per year
- MBA: ₹3,00,000 per year

Scholarships available based on merit."""

    elif any(word in q for word in ["hostel", "accommodation", "stay"]):
        return """🏠 **Hostel Facilities**
- Separate hostels for boys & girls
- AC & Non-AC rooms
- 24/7 security & WiFi
- Mess facility available"""

    elif any(word in q for word in ["transport", "bus", "travel"]):
        return """🚌 **Transport**
- College buses available
- Covers nearby cities
- Safe and reliable service"""

    elif any(word in q for word in ["event", "fest", "function"]):
        return """🎉 **Events & Campus Life**
- Annual Cultural Fest
- Tech Fest
- Sports Competitions
- Clubs & student activities"""

    elif any(word in q for word in ["attendance", "criteria", "requirement"]):
        return """📊 **Attendance Criteria**
- Minimum 75% mandatory
- Required to appear in exams"""

    elif any(word in q for word in ["placement", "job", "package"]):
        return """💼 **Placements**
- Average package: 6 LPA
- Top recruiters visit campus
- Training & placement cell support"""

    elif any(word in q for word in ["admission", "apply", "eligibility"]):
        return """📝 **Admission Process**
1. Entrance Exam
2. Personal Interview
3. Final Selection

Apply online through official portal."""

    else:
        return "🤖 Sorry, I don't have that information. Try selecting a topic from the sidebar."

if "messages" not in st.session_state:
    st.session_state.messages = []

if selected_option:
    st.session_state.messages.append({"role": "user", "content": selected_option})
    st.session_state.messages.append({"role": "assistant", "content": chatbot(selected_option)})

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    answer = chatbot(user_input)

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
