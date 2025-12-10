import streamlit as st
import pandas as pd

# -------------------------------
# Page setup
# -------------------------------
st.set_page_config(
    page_title="LGL Chatbot",
    page_icon="🚢",
    layout="wide"
)

# -------------------------------
# Custom CSS for Slack-like UI
# -------------------------------
st.markdown("""
    <style>
    .main {
        background-color: #1a1d21;
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: #f5f5f5;
    }
    .stTextInput > div > div > input {
        background-color: #2c2f33;
        color: white;
        border-radius: 6px;
    }
    .stButton > button {
        background-color: #0077cc;
        color: white;
        border-radius: 6px;
        font-weight: bold;
    }
    .term-card {
        background-color: #2c2f33;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 0 10px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Title and branding
# -------------------------------
st.title("🚢 LGL Chatbot")
st.subheader("Liberty Global Logistics — Your Logistics Knowledge Companion")
st.write("Ask me about any logistics term and I'll explain it!")

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Cargo_ship.jpg", use_column_width=True)
    st.markdown("### About LGL")
    st.markdown("""
    **Liberty Global Logistics (LGL)** is a leader in worldwide shipping and logistics solutions.
    
    This chatbot helps you explore logistics terminology and concepts interactively.
    """)
    st.markdown("---")
    st.markdown("💡 Try terms like *3PL*, *AFRICOM*, or *AWB*.")

# -------------------------------
# Load terms from CSV
# -------------------------------
# Adjustments: strip spaces from headers, handle Excel-export quirks
df = pd.read_csv("terms.csv")
df.columns = df.columns.str.strip()   # remove leading/trailing spaces
df = df.dropna(how="all")             # drop empty rows

# Debug: show columns so you can confirm they match
# st.write("Columns loaded:", df.columns.tolist())

# -------------------------------
# Chat Interface
# -------------------------------
st.markdown("### 💬 Ask me a logistics term")

query = st.text_input("🔍 Enter a logistics term:")

if query:
    term = query.strip().upper()
    if "Term" in df.columns:
        match = df[df["Term"].str.upper() == term]
        if not match.empty:
            row = match.iloc[0]
            st.markdown(f"""
                <div class="term-card">
                    <h3>📘 {row['Term']} — {row['Complete Form']}</h3>
                    <p><b>Category:</b> {row['Category']}</p>
                    <p><b>Definition:</b> {row['Definition']}</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Sorry, I couldn't find that term. Try another one!")
    else:
        st.error("CSV file is missing the 'Term' column. Please check your