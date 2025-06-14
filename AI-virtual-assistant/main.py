import streamlit as st
import google.generativeai as genai


genai.configure(api_key='APi_key')
model = genai.GenerativeModel('gemini-1.5-flash')


if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[
        {"role": "user", "parts": ["INSTRUCTION : Crisp Answers and frank humble responses"]}
    ])
    st.session_state.messages = [] 

st.set_page_config(page_title="Jarvis - AI Assistant", layout="centered")
st.title("🤖 Jarvis - Your AI Chat Assistant")


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])


user_input = st.chat_input("Ask anything...")


if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "text": user_input})

    response = st.session_state.chat.send_message(user_input)
    reply = response.text

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "text": reply})