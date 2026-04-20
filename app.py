#College Enquiry Chatbot
import streamlit as st

st.set_page_config(page_title="College Chatbot", page_icon="🎓")

st.title("🎓 College Enquiry Chatbot")
st.caption("Ask about courses, fees, hostel, transport, events, attendance, placement, etc.")

def chatbot(question):
    q = question.lower()

    if any(word in q for word in ["course", "program", "degree"]):
        return "We offer BTech (CSE, AI, Mechanical), MBA, and BBA."

    elif any(word in q for word in ["fee", "fees", "cost", "price"]):
        return "BTech fees are approx ₹2 lakh per year and MBA is ₹3 lakh per year."

    elif any(word in q for word in ["hostel", "accommodation", "stay"]):
        return "Yes, hostel is available for both boys and girls with AC and Non-AC rooms."

    elif any(word in q for word in ["transport", "bus", "travel"]):
        return "College provides bus transportation from nearby cities with annual charges."

    elif any(word in q for word in ["event", "fest", "function"]):
        return "We organize annual fest, tech fest, cultural events and sports competitions."

    elif any(word in q for word in ["attendance", "criteria", "requirement"]):
        return "Minimum 75% attendance is required to appear in exams."

    elif any(word in q for word in ["placement", "job", "package"]):
        return "Average package is around 6 LPA and top companies visit every year."

    elif any(word in q for word in ["admission", "apply", "eligibility"]):
        return "Admission is based on entrance exam followed by interview."

    elif any(word in q for word in ["library", "books"]):
        return "The college has a well-equipped library with digital and physical resources."

    elif any(word in q for word in ["canteen", "food", "mess"]):
        return "Canteen and mess facilities are available with both veg and non-veg options."

    else:
        return "Sorry, I don't have that information. Please ask about courses, fees, hostel, transport, events, attendance, or placement."

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask your question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    answer = chatbot(user_input)

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
        
