
                st.progress(
                    min(max(model_score / 100, 0.0), 1.0)
                )

                st.caption(
                    "This score represents the model's "
                    "classification output, not a medical "
                    "probability or diagnostic certainty."
                )

                st.session_state["last_result"] = result

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

        st.markdown(textwrap.dedent("""
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
        """), unsafe_allow_html=True)


# ==========================================
# INFORMATION SECTION
# ==========================================

st.markdown("---")

st.markdown("### About DermaAI")

info1, info2 = st.columns(2)

with info1:

    st.markdown(textwrap.dedent("""
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
    """), unsafe_allow_html=True)

with info2:

    st.markdown(textwrap.dedent("""
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
    """), unsafe_allow_html=True)


# ==========================================
# FOOTER
# ==========================================

st.markdown(textwrap.dedent("""
<div class="footer">

    <p>DERMAAI © 2026</p>

    <p>
        AI-Powered Skin Image Classification |
        Educational Research Project
    </p>

    <p>Designed for responsible AI experimentation.</p>

</div>
"""), unsafe_allow_html=True)
