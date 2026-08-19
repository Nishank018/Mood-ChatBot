import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

# ---------- Mood prompts ----------
MOODS = {
    "Neutral": "You are a helpful AI assistant.",
    "Funny": "You are a hilarious AI assistant who cracks jokes, uses playful humor, "
             "and never gives a boring answer. Keep responses light and witty, but still helpful.",
    "Angry": "You are an easily annoyed AI assistant who responds with irritation and "
              "short temper, complaining a bit before giving the actual (still correct) answer.",
    "Sarcastic": "You are a deeply sarcastic AI assistant. Every response drips with dry wit "
                 "and sarcasm, but you still provide the correct and useful answer underneath.",
    "Formal": "You are a highly formal, professional AI assistant. Respond with precise, "
              "polished, business-appropriate language.",
}

# ---------- Page config ----------
st.set_page_config(page_title="Mood Chatbot", page_icon="💬", layout="centered")

# ---------- Minimal clean styling ----------
st.markdown(
    """
    <style>
        .block-container { max-width: 720px; padding-top: 2rem; }
        [data-testid="stChatMessage"] { padding: 0.4rem 0; }
        h1 { font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💬 Mood Chatbot")

# ---------- Sidebar: mood selector ----------
with st.sidebar:
    st.header("Settings")
    mood = st.selectbox("Choose a mood", list(MOODS.keys()), index=0)

    if st.button("Clear chat", use_container_width=True):
        st.session_state.messages = [SystemMessage(content=MOODS[mood])]
        st.rerun()

# ---------- Session state init ----------
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=MOODS[mood])]
    st.session_state.mood = mood

# If mood changed, reset the system message (and history, so tone is consistent)
if st.session_state.get("mood") != mood:
    st.session_state.mood = mood
    st.session_state.messages = [SystemMessage(content=MOODS[mood])]
    st.info(f"Mood switched to **{mood}** — chat history cleared.")

# ---------- LLM ----------
@st.cache_resource
def get_llm():
    return ChatMistralAI(model="mistral-small-latest", temperature=0.7)

llm = get_llm()

# ---------- Render chat history ----------
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# ---------- Chat input ----------
prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(st.session_state.messages)
        st.write(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))