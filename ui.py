import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Mental Health Chatbot", page_icon="🌿")

# Soft CSS styling
st.markdown("""
<style>
body {
    background-color: #f5f7f9;
}

.chat-container {
    max-height: 400px;
    overflow-y: auto;
    padding: 10px;
}

.user-bubble {
    background-color: #d1e7dd;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
    text-align: right;
}

.bot-bubble {
    background-color: #ffffff;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
    text-align: left;
    border: 1px solid #e0e0e0;
}
</style>
""", unsafe_allow_html=True)

st.title("🌿 Mental Health AI Chatbot")
st.write("Feel free to share how you're feeling...")

# Store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat display
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Input form (auto clears)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message...")
    submit = st.form_submit_button("Send")

if submit and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = requests.post(
        "http://127.0.0.1:5000/chat",
        json={"message": user_input}
    )

    bot_reply = response.json()["reply"]

    st.session_state.messages.append({"role": "bot", "content": bot_reply})

    st.rerun()