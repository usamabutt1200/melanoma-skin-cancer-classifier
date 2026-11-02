import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

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
    transition: 0.3s;
}

.stButton > button:hover {
    background: #63E5D4;
    color: #071522;
    border: none;
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


# ==========================================
# MODEL LOADING
# ==========================================

MODEL_PATH = "skin_cancer_model.tflite"


@st.cache_resource
def load_model():

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            "Model file not found: " + MODEL_PATH
        )

    interpreter = tf.lite.Interpreter(
        model_path=MODEL_PATH
    )

    interpreter.allocate_tensors()

    return interpreter


# ==========================================
# IMAGE PREPROCESSING
# ==========================================

def preprocess_image(image):

    image = image.convert("RGB")

    image = image.resize((224, 224))

    image_array = np.array(
        image,
        dtype=np.float32
    )

    image_array = image_array / 255.0

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    return image_array


# ==========================================
# PREDICTION
# ==========================================

def predict_image(interpreter, image):

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    processed_image = preprocess_image(image)

    interpreter.set_tensor(
        input_details[0]["index"],
        processed_image
    )

    interpreter.invoke()

    prediction = interpreter.get_tensor(
        output_details[0]["index"]
    )

    score = float(prediction[0][0])

    return score


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown(
        "<h2 style='color:#35D6C0;'>◈ DermaAI</h2>",
        unsafe_allow_html=True
    )

    st.caption("INTELLIGENT SKIN IMAGE CLASSIFICATION")

    st.markdown("---")

    st.markdown("### Navigation")

    st.markdown("🔬 Skin Analysis")
    st.markdown("📊 Model Information")
    st.markdown("🛡️ Safety Information")

    st.markdown("---")

    st.markdown("### Model Details")

    st.markdown("""
    **Architecture:** CNN

    **Input Size:** 224 × 224

    **Classes:** 2

    **Test Accuracy:** 89.5%

    **Model Format:** TensorFlow Lite
    """)

    st.markdown("---")

    st.caption("Educational AI Research Project")


# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="main-title">
    AI Skin <span class="accent">Analysis</span>
</div>

<div class="subtitle">
    Intelligent image classification powered by a
    Convolutional Neural Network.
</div>
""", unsafe_allow_html=True)


# ==========================================
# TOP METRICS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="premium-card">
        <div class="metric-label">Model Architecture</div>
        <div class="metric-value">CNN</div>
    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="premium-card">
        <div class="metric-label">Test Accuracy</div>
        <div class="metric-value">89.5%</div>
    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="premium-card">
        <div class="metric-label">Classification Classes</div>
        <div class="metric-value">02</div>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# MAIN ANALYSIS AREA
# ==========================================

left, right = st.columns(
    [1, 1],
    gap="large"
)


with left:

    st.markdown("### Upload Skin Image")

    st.markdown(
        '<p class="result-description">'
        'Upload an image in JPG, JPEG or PNG format '
        'to perform an educational AI classification.'
        '</p>',
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    if uploaded_file:

        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        st.markdown(
            f"""
            <div class="premium-card">
                <div class="metric-label">Image Information</div>

                <p style="color:#E5EDF7;">
                    Resolution: {image.width} × {image.height}
                </p>

                <p style="color:#E5EDF7;">
                    Format: {uploaded_file.type}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown("""
        <div class="premium-card"
             style="text-align:center; padding:65px 20px;">

            <div style="font-size:48px;">🔬</div>

            <h3 style="color:#E5EDF7;">
                Ready for Analysis
            </h3>

            <p style="color:#91A4BD;">
                Upload an image to begin classification.
            </p>

        </div>
        """, unsafe_allow_html=True)


# ==========================================
# ANALYSIS RESULTS
# ==========================================

with right:

    st.markdown("### Analysis Results")

    if uploaded_file:

        if st.button(
            "Run AI Analysis",
            use_container_width=True
        ):

            try:

                with st.spinner(
                    "Analyzing image with DermaAI..."
                ):

                    interpreter = load_model()

                    score = predict_image(
                        interpreter,
                        image
                    )

                # Class mapping:
                # 0 = Benign
                # 1 = Malignant

                if score >= 0.5:

                    result = "Malignant"
                    model_score = score * 100
                    result_color = "#FF7272"

                    description = (
                        "The model classified this image "
                        "as belonging to the Malignant class."
                    )

                else:

                    result = "Benign"
                    model_score = (1 - score) * 100
                    result_color = "#35D6C0"

                    description = (
                        "The model classified this image "
                        "as belonging to the Benign class."
                    )

                st.markdown(
                    f"""
                    <div class="premium-card"
                         style="border-color:{result_color};">

                        <div class="metric-label">
                            MODEL CLASSIFICATION
                        </div>

                        <div class="result-title"
                             style="color:{result_color};">
                            {result}
                        </div>

                        <p class="result-description">
                            {description}
                        </p>

                        <hr style="border-color:#263B55;">

                        <div class="metric-label">
                            MODEL SCORE
                        </div>

                        <div class="metric-value">
                            {model_score:.2f}%
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.progress(
                    min(max(model_score / 100, 0.0), 1.0)
                )

                st.caption(
                    "This score represents the model's "
                    "classification output, not a medical "
                    "probability or diagnostic certainty."
                )

                st.warning(
                    "This is an educational AI model, not a "
                    "medical diagnostic tool. It may produce "
                    "incorrect results. Do not use this result "
                    "to rule out or confirm skin cancer. "
                    "Consult a qualified healthcare professional "
                    "for medical evaluation."
                )

            except Exception as e:

                st.error(
                    f"Analysis failed: {str(e)}"
                )

    else:

        st.markdown("""
        <div class="premium-card"
             style="text-align:center; padding:75px 20px;">

            <div style="font-size:42px;">📊</div>

            <h3 style="color:#E5EDF7;">
                No Analysis Yet
            </h3>

            <p style="color:#91A4BD;">
                Your classification results will appear here.
            </p>

        </div>
        """, unsafe_allow_html=True)


# ==========================================
# INFORMATION SECTION
# ==========================================

st.markdown("---")

st.markdown("### About DermaAI")

info1, info2 = st.columns(2)


with info1:

    st.markdown("""
    <div class="premium-card">

        <h4 style="color:#35D6C0;">
            ◈ AI Technology
        </h4>

        <p class="result-description">
            DermaAI uses a Convolutional Neural Network
            trained on a skin image dataset to classify
            uploaded images into two categories:
            Benign and Malignant.
        </p>

    </div>
    """, unsafe_allow_html=True)


with info2:

    st.markdown("""
    <div class="premium-card">

        <h4 style="color:#35D6C0;">
            ◈ Important Disclaimer
        </h4>

        <p class="result-description">
            This application is developed for educational
            and research purposes only. Its predictions
            are not a substitute for professional medical
            examination or diagnosis.
        </p>

    </div>
    """, unsafe_allow_html=True)


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">

    <p>DERMAAI © 2026</p>

    <p>
        AI-Powered Skin Image Classification |
        Educational Research Project
    </p>

    <p>Designed for responsible AI experimentation.</p>

</div>
""", unsafe_allow_html=True)
