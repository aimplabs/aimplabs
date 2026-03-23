import requests
import streamlit as st
from datetime import date


PAGE_TITLE = "Legal AI Chatbot by AIMP LABS"
API_URL = "https://abhishekaimp.pythonanywhere.com/api/chat"
WELCOME_MESSAGE = (
    "Hello! Ask your legal question and I will help using the configured chatbot backend."
)
FALLBACK_MESSAGE = (
    "Apologies, I'm unable to process your legal query right now. Please try "
    "again in a moment."
)
SAMPLE_QUERIES = [
    (
        "Sample Query 1",
        "A vehicle jumped the red light and collided with my car, then fled the "
        "scene. This has happened in Patuli, Kolkata. I hope that CCTV cameras "
        "installed at the Patuli's E M Bypass crossing may contain the license "
        "plate number of the concerned vehicle. I'd like to explore our legal "
        "options for pursuing the perpetrator and recovering damages for my "
        "vehicle. Could you please advise on the next steps?",
    ),
    (
        "Sample Query 2",
        "I'm experiencing a noise disturbance issue with my neighbors who are "
        "hosting loud parties over the weekend. Despite politely requesting to "
        "keep the noise down, they're not adhering to the rules. I'd like to "
        "explore our legal options for addressing this issue and finding a "
        "resolution.",
    ),
    (
        "Sample Query 3",
        "I need your assistance with a pressing issue regarding one of my "
        "tenants. They've stopped paying rent for the past three months and are "
        "still occupying the ground floor unit. I'd like to explore our legal "
        "options for eviction. I'd appreciate your guidance on how to proceed.",
    ),
]


def init_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": WELCOME_MESSAGE}]
    if "chat_input" not in st.session_state:
        st.session_state.chat_input = ""


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


def submit_query(user_message: str) -> None:
    cleaned_message = user_message.strip()
    if not cleaned_message:
        return

    st.session_state.messages.append({"role": "user", "content": cleaned_message})
    with st.chat_message("user"):
        st.markdown(cleaned_message)

    with st.spinner("Thinking..."):
        assistant_reply = ask_legalbot(cleaned_message)

    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)


st.set_page_config(page_title=PAGE_TITLE, page_icon=":scroll:")
init_state()

st.header("Featured Innovation: Legal AI Chatbot by AIMP LABS")
st.markdown(
    "At AIMP LABS, innovation is at the heart of everything we do. "
    "This chatbot is designed to interact with and interpret three recently "
    "enacted Indian laws:"
)
st.markdown(
    "- **BNS (Bharatiya Nyaya Sanhita)** - Replacing IPC; governs criminal offenses.\n"
    "- **BNSS (Bharatiya Nagrik Suraksha Sanhita)** - Replacing CrPC; outlines criminal procedure.\n"
    "- **BSA (Bharatiya Sakshya Adhiniyam)** - Replacing the Indian Evidence Act; governs evidence rules."
)
st.caption(
    "Ask about sections, clauses, and legal terminology for quick contextual guidance."
)
st.divider()

if st.button("Reset Chat"):
    reset_chat()

st.caption("Sample queries")
sample_cols = st.columns(3)
for idx, (label, query) in enumerate(SAMPLE_QUERIES):
    with sample_cols[idx]:
        if st.button(label, use_container_width=True):
            st.session_state.chat_input = query
            st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask your legal question", key="chat_input")
if prompt:
    submit_query(prompt)

st.divider()
st.markdown("### AIMP LABS")
st.caption("Private AI Research & Training Center")
st.caption("Computer Vision | Machine Learning | Cloud & Edge Computing")
st.caption("Contact: contact@aimplabs.org")
# st.markdown("[About us](about.html) • [Student developer/researcher](rudev.html)")
# st.markdown(
#     "[GitHub](https://github.com/aimplabs) • "
#     "[Twitter](https://twitter.com/aimplabs) • "
#     "[YouTube](https://youtube.com/@aimplabs) • "
#     "[Facebook](https://www.facebook.com/aimplabs)"
# )
st.caption(f"Copyright 2019 - {date.today().year}")
