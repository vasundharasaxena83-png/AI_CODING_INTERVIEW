import streamlit as st

def load_theme():
    st.markdown("""
    <style>

    /* GLOBAL BACKGROUND */
    .stApp {
        background: radial-gradient(circle at top, #0B1020, #050816);
        color: white;
        font-family: 'Poppins', sans-serif;
    }

    /* GLASS CARD */
    .glass {
        background: rgba(255,255,255,0.06);
        border-radius: 18px;
        padding: 20px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.4);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 15px;
    }

    /* BUTTON */
    .stButton > button {
        background: linear-gradient(90deg, #6366F1, #8B5CF6);
        color: white;
        border-radius: 12px;
        padding: 10px 18px;
        border: none;
        transition: 0.3s;
        font-weight: 600;
    }

    .stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 20px rgba(99,102,241,0.6);
    }

    /* TEXT AREA (CODE EDITOR) */
    textarea {
        background-color: #0B1220 !important;
        color: white !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background: #0A0F1E;
    }

    /* TITLE GRADIENT */
    .title {
        font-size: 34px;
        font-weight: 800;
        background: linear-gradient(90deg, #6366F1, #22C55E);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    </style>
    """, unsafe_allow_html=True)