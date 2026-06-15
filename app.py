import streamlit as st
import os

from auth.login import authenticate
from rag.ingest import ingest_pdf
from rag.retriever import get_context
from rag.llm import ask_llm

# ==================================
# PAGE CONFIG
# ==================================
st.set_page_config(
    page_title="🏦 Banking GenAI Assistant",
    page_icon="🏦",
    layout="wide"
)

# ==================================
# CUSTOM CSS
# ==================================
st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #f5f7fb;
}

/* Header */
.main-header {
    background: linear-gradient(90deg, #0f172a, #1e40af);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
}

.main-header h1 {
    margin: 0;
    font-size: 42px;
}

.main-header p {
    color: #dbeafe;
    font-size: 18px;
}

/* Cards */
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #0f172a;
}

/* Sidebar text */
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: white !important;
}

/* Input Fields */
.stTextInput input {
    background-color: white !important;
    color: black !important;
    border: 2px solid #2563eb !important;
    border-radius: 10px !important;
    padding: 10px !important;
    font-size: 16px !important;
}

.stTextInput input::placeholder {
    color: #64748b !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 45px;
    border-radius: 10px;
    border: none;
    font-size: 16px;
    font-weight: bold;
    background: linear-gradient(90deg,#2563eb,#1d4ed8);
    color: white;
}

.stButton > button:hover {
    background: linear-gradient(90deg,#1d4ed8,#1e3a8a);
}

/* Footer */
.footer {
    text-align: center;
    color: gray;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# HEADER
# ==================================
st.markdown("""
<div class="main-header">
    <h1>🏦 Banking GenAI Assistant</h1>
    <p>AI-Powered Banking Knowledge & Document Intelligence Platform</p>
</div>
""", unsafe_allow_html=True)

# ==================================
# DASHBOARD METRICS
# ==================================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Documents", "Unlimited")

with col2:
    st.metric("🤖 AI Model", "Gemini")

with col3:
    st.metric("🔒 Security", "Role Based")

st.markdown("---")

# ==================================
# LOGIN SECTION
# ==================================
st.sidebar.title("🔐 Login Portal")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if st.sidebar.button("🚀 Login"):

    role = authenticate(username, password)

    if role:
        st.session_state.logged_in = True
        st.session_state.role = role
        st.sidebar.success("Login Successful")
    else:
        st.sidebar.error("Invalid Username or Password")

# ==================================
# SHOW CONTENT AFTER LOGIN
# ==================================
if st.session_state.logged_in:

    st.success(f"✅ Welcome {username}")
    st.info(f"👤 Role: {st.session_state.role}")

    st.markdown("""
    <div class="card">
        <h3>📂 Upload Banking PDF</h3>
        <p>Upload banking documents to create your AI knowledge base.</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose Banking PDF",
        type=["pdf"]
    )

    if uploaded_file:

        os.makedirs("data", exist_ok=True)

        file_path = os.path.join(
            "data",
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("📚 Processing PDF..."):
            result = ingest_pdf(file_path)

        st.success(result)

# ==================================
# QUESTION SECTION
# ==================================
st.markdown("""
<div class="card">
    <h3>💬 Ask Banking Questions</h3>
    <p>Ask questions from uploaded documents and get AI-powered answers.</p>
</div>
""", unsafe_allow_html=True)

question = st.text_input(
    "🔍 Enter Your Banking Question"
)

if st.button("🤖 Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:
        with st.spinner("🔎 Searching..."):

            context = get_context(question)
            answer = ask_llm(question, context)

        st.subheader("📌 AI Answer")
        st.success(answer)

# ==================================
# FOOTER
# ==================================
st.markdown("""
<div class="footer">
<hr>
Developed with ❤️ using Streamlit | Banking GenAI Assistant
</div>
""", unsafe_allow_html=True)