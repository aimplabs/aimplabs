import requests
import streamlit as st


PAGE_TITLE = "Legal AI Chatbot"
API_URL = "https://abhishekaimp.pythonanywhere.com/api/chat"
WELCOME_MESSAGE = (
    "Hello! Ask your legal question and I will help using the configured chatbot backend."
)
FALLBACK_MESSAGE = (
    "Apologies, I'm unable to process your legal query right now. Please try "
    "again in a moment."
)


def init_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": WELCOME_MESSAGE}]


def reset_chat() -> None:
    st.session_state.messages = [{"role": "assistant", "content": WELCOME_MESSAGE}]


def ask_legalbot(user_message: str) -> str:
    try:
        response = requests.post(
            API_URL,
            json={"message": user_message},
            timeout=90,
        )
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        return FALLBACK_MESSAGE

    reply = data.get("reply")
    if isinstance(reply, str) and reply.strip():
        return reply
    return FALLBACK_MESSAGE


st.set_page_config(page_title=PAGE_TITLE, page_icon=":scroll:")
init_state()

st.title(PAGE_TITLE)
if st.button("Reset Chat"):
    reset_chat()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask your legal question")
if prompt:
    cleaned_message = prompt.strip()
    if cleaned_message:
        st.session_state.messages.append({"role": "user", "content": cleaned_message})
        with st.chat_message("user"):
            st.markdown(cleaned_message)

        with st.spinner("Thinking..."):
            assistant_reply = ask_legalbot(cleaned_message)

        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
        with st.chat_message("assistant"):
            st.markdown(assistant_reply)
