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
# MODEL LOADING (With Caching to prevent reload lags)
# ==========================================
@st.cache_resource
def load_my_model():
    # اگر آپ کی ماڈل فائل کا نام الگ ہے تو اسے یہاں تبدیل کریں (جیسے 'skin_cancer_model.h5')
    model_path = "model.h5" 
    if os.path.exists(model_path):
        return tf.keras.models.load_model(model_path)
    return None

model = load_my_model()

# بیماریوں کی لسٹ (اپنے ماڈل کی کلاسز کے مطابق ترتیب چیک کر لیں)
class_names = ["Benign Keratosis", "Melanoma (Skin Cancer)", "Basal Cell Carcinoma"]

# ==========================================
# IMAGE UPLOAD & ANALYSIS SECTION
# ==========================================
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
st.markdown('<p class="metric-label">📊 Screening Panel</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a skin lesion image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption='Uploaded Image', use_container_width=True)
        
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🔍 Analyze Image", type="primary"):
            if model is None:
                st.error("❌ 'model.h5' فائل نہیں ملی! برائے مہربانی چیک کریں کہ ماڈل فائل اسی فولڈر میں موجود ہے جہاں app.py ہے۔")
            else:
                with st.spinner("⏳ Analyzing image with AI model..."):
                    # 1. امیج کو ماڈل کے مطابق تیار کرنا (Preprocessing)
                    # اگر آپ کا ماڈل 128x128 مانگتا ہے تو نیچے 224 کو 128 کر دیں
                    img_resized = image.resize((224, 224)) 
                    img_array = np.array(img_resized) / 255.0  # Normalization
                    img_array = np.expand_dims(img_array, axis=0)  # Batch dimension
                    
                    # 2. ماڈل سے پریڈکشن لینا
                    predictions = model.predict(img_array)[0]
                    highest_pred_idx = np.argmax(predictions)
                    predicted_class = class_names[highest_pred_idx]
                    confidence = predictions[highest_pred_idx] * 100
                    
                    # 3. رزلٹ اسکرین پر دکھانا
                    st.success("✅ Analysis Complete!")
                    st.metric(label="Predicted Condition", value=predicted_class)
                    st.metric(label="Confidence Level", value=f"{confidence:.2f}%")
                    
                    # سیکیورٹی اور معلوماتی گراف
                    st.write("### Probability Breakdown:")
                    for i, class_nm in enumerate(class_names):
                        st.write(f"**{class_nm}**: {predictions[i]*100:.1f}%")
                        st.progress(float(predictions[i]))

st.markdown('</div>', unsafe_allow_html=True)
