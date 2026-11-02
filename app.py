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
# Corrected parameter name to unsafe_allow_html=True
st.markdown("""
<style>
@import url('https://googleapis.com');

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
""", unsafe_allow_html=True) 

# ==========================================
# APP MAIN BODY (Test UI)
# ==========================================
st.markdown('<h1 class="main-title">DermaAI <span class="accent">Skin Analysis</span></h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Advanced AI-powered dermatological screening tool</p>', unsafe_allow_html=True)

st.sidebar.title("Navigation")
st.sidebar.info("Upload your image to begin analytics.")
# ==========================================
# IMAGE UPLOAD & ANALYSIS SECTION
# ==========================================
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
st.markdown('<p class="metric-label">📊 Screening Panel</p>', unsafe_allow_html=True)

# فائل اپلوڈر ایڈ کریں
uploaded_file = st.file_uploader("Choose a skin lesion image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # امیج کو اوپن کریں
    image = Image.open(uploaded_file)
    
    # اسکرین کو دو حصوں میں تقسیم کریں (لیفٹ پر امیج، رائٹ پر رزلٹ)
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption='Uploaded Image', use_container_width=True)
        
    with col2:
        st.write("⏳ Analyzing image with AI model...")
        # یہاں آپ کا ماڈل پریڈکشن کا کوڈ آئے گا

st.markdown('</div>', unsafe_allow_html=True)

