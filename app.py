import streamlit as st
import tensorflow as tf
import numpy as np
import os
from PIL import Image

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="DermaAI | Skin Analysis",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #080F1D;
    color: #E5EDF7;
}

header {
    background: transparent !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0D1728;
    border-right: 1px solid #1E3048;
}

section[data-testid="stSidebar"] * {
    color: #DCE7F5;
}

/* Main heading */
.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #F1F6FC;
    letter-spacing: -1.5px;
    margin-bottom: 5px;
}

.subtitle {
    color: #91A4BD;
    font-size: 15px;
    margin-bottom: 30px;
}

.accent {
    color: #35D6C0;
}

/* Cards */
.premium-card {
    background: linear-gradient(145deg, #14243A, #0D192B);
    border: 1px solid #263B55;
    border-radius: 18px;
    padding: 24px;
    margin-bottom: 18px;
}

.metric-label {
    color: #91A4BD;
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_safe_html=False) # یہاں ٹرپل کوٹ بند کر دیا گیا ہے

# ==========================================
# APP MAIN BODY (Test UI)
# ==========================================
st.markdown('<h1 class="main-title">DermaAI <span class="accent">Skin Analysis</span></h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Advanced AI-powered dermatological screening tool</p>', unsafe_allow_html=True)

st.sidebar.title("Navigation")
st.sidebar.info("Upload your image to begin analytics.")
