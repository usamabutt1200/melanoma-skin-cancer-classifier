
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import textwrap

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
    background: linear-gradient(
        145deg,
        #14243A,
        #0D192B
    );
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

.metric-value {
    color: #F4F8FD;
    font-size: 29px;
    font-weight: 800;
    margin-top: 10px;
}

/* Upload section */

[data-testid="stFileUploader"] {
    background: #101F33;
    border: 1px dashed #35D6C0;
    border-radius: 16px;
    padding: 15px;
}

/* Buttons */

.stButton > button {
    background: linear-gradient(90deg, #20BFAE, #35D6C0);
    color: #071522;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    padding: 12px 25px;
    width: 100%;
}

.stButton > button:hover {
    background: #63E5D4;
    color: #071522;
}

/* Results */

.result-title {
    font-size: 24px;
    font-weight: 800;
    margin-bottom: 8px;
}

.result-description {
    color: #A9BBD0;
    font-size: 14px;
    line-height: 1.7;
}

.footer {
    text-align: center;
    color: #71849B;
    font-size: 12px;
    border-top: 1px solid #203149;
    padding-top: 22px;
    margin-top: 45px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)
