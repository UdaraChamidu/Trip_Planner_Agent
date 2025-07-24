import re
import streamlit as st
import requests
import datetime
from fpdf import FPDF
import base64
import uuid
import tempfile

BASE_URL = "http://localhost:8000"

# 🌐 Page config
st.set_page_config(
    page_title="🌍 Travel Planner AI",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# 📂 Initialize session state
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {}

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = str(uuid.uuid4())

# ✨ Sidebar (reduced height by scrolling container)
with st.sidebar:
    st.markdown("## 💬 Chat Sessions")
    with st.container():
        with st.expander("View Sessions", expanded=False):  # collapse by default
            delete_keys = []
            for chat_id, data in st.session_state.chat_sessions.items():
                col1, col2 = st.columns([0.85, 0.15])
                with col1:
                    if st.button(data["title"], key=f"title_{chat_id}"):
                        st.session_state.current_chat_id = chat_id
                with col2:
                    delete_button_key = f"del_{chat_id}"
                    if st.button("❌", key=delete_button_key):
                        delete_keys.append(chat_id)

            for key in delete_keys:
                del st.session_state.chat_sessions[key]
                if st.session_state.current_chat_id == key:
                    st.session_state.current_chat_id = list(st.session_state.chat_sessions.keys())[0] if st.session_state.chat_sessions else str(uuid.uuid4())
                    break

    st.markdown("---")
    if st.button("➕ New Chat"):
        new_chat_id = str(uuid.uuid4())
        st.session_state.current_chat_id = new_chat_id
        st.session_state.chat_sessions[new_chat_id] = {"title": f"New Chat", "messages": []}

# 💬 Load messages
if st.session_state.current_chat_id not in st.session_state.chat_sessions:
    st.session_state.chat_sessions[st.session_state.current_chat_id] = {"title": "New Chat", "messages": []}

chat_data = st.session_state.chat_sessions[st.session_state.current_chat_id]

# 🎨 Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌍 Travel Planner AI Agent</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Plan your perfect trip using AI ✨</p>", unsafe_allow_html=True)
st.divider()

# 🛅 User input
st.markdown("### 📍 Ask me about your next trip")
st.markdown("*Try something like:* `Plan a 7-day Tour to Sri Lanka on a low budget.`")

with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input("Ask anything travel-related:", placeholder="e.g. Plan a 5-day trip to Kandy")
    submit_button = st.form_submit_button("✈️ Send")

# 🧠 Process input
if submit_button and user_input.strip():
    with st.spinner("🧠 Generating travel plan..."):
        try:
            payload = {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)

            if response.status_code == 200:
                answer = response.json().get("answer", "No answer returned.")
                message = {
                    "question": user_input,
                    "answer": answer,
                    "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                chat_data["messages"].append(message)

                # ✨ Dynamic title generation
                suggested_title = user_input.strip()
                if len(suggested_title) > 30:
                    suggested_title = suggested_title[:27] + "..."
                chat_data["title"] = suggested_title

            else:
                st.error("Bot failed to respond: " + response.text)
        except Exception as e:
            st.error(f"Request failed due to: {e}")

# 🧴 Show chat
if chat_data["messages"]:
    for msg in chat_data["messages"]:
        with st.chat_message("user"):
            st.markdown(f"**You:** {msg['question']}")
        with st.chat_message("assistant"):
            st.markdown(f"**AI Plan:** {msg['answer']}")

    # Function to remove emojis/special characters
    def clean_text(text):
        return re.sub(r'[^\x00-\x7F]+', '', text)

    # 📄 Download PDF
    if chat_data["messages"]:
        latest_msg = chat_data["messages"][-1]

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="AI Travel Plan", ln=True, align="C")
        pdf.ln(10)

        # Clean and format
        question = clean_text(latest_msg["question"])
        answer = clean_text(latest_msg["answer"])
        time = latest_msg["time"]
        pdf.multi_cell(0, 10, f"Question: {question}\n\nAnswer:\n{answer}\n\nGenerated on {time}")

        # Save to temp and read bytes
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            pdf.output(tmp_file.name)
            pdf_file_path = tmp_file.name

        with open(pdf_file_path, "rb") as f:
            pdf_bytes = f.read()

        st.download_button(
            label="📅 Download Plan as PDF",
            data=pdf_bytes,
            file_name="travel_plan.pdf",
            mime="application/pdf"
        )
else:
    st.info("Start a chat to generate a travel plan!")

# 🔻 Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by Udara</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Powered by OpenAI GPT-4o</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Contact: udara@travelagent.com</p>", unsafe_allow_html=True)

from langchain_core.messages import SystemMessage