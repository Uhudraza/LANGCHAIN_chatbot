import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

# Set page config
st.set_page_config(
    page_title="Syed's GPT App",
    page_icon="🦜",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: lightblue;
        padding: 2rem;
    }
    .sidebar .sidebar-content {
        background-color: #eef;
    }
    .stTextInput, .stTextArea {
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton button {
        background-color: #007Bdd;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton button:hover {
        background-color: #0056b3;
        color: white;
    }
    .st-alert-warning {
        background-color: #ffcc00;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title
st.title("🦜🔗 Syed's GPT App")

# Sidebar for API key input
st.sidebar.title("Configuration")
openai_api_key = st.sidebar.text_input("Enter the API Key", type="password")

# Function to generate and display response
def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text))

# Main form for user input
with st.form("input_form"):
    text = st.text_area(
        "Enter your question or prompt:",
        "What are the three key pieces of advice for learning how to code?",
        height=150,
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
