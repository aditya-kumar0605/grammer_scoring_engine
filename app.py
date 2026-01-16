import streamlit as st
import tempfile
import os

from src.transcribe import transcribe_audio
from src.preprocess import clean_text
from src.grammar_score import calculate_grammar_score


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Grammar Scoring Engine",
    page_icon="🎤",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
@keyframes gradient-animation {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.main {
    background: linear-gradient(-45deg, #f9fafc, #eef0f3, #f9fafc, #eef0f3);
    background-size: 400% 400%;
    animation: gradient-animation 25s ease infinite;
}

.title-text {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #2c3e50;
    padding-top: 15px;
}

.subtitle-text {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}

.card {
    background-color: rgba(255, 255, 255, 0.96);
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.15);
    margin-top: 20px;
    border: 1px solid #e0e0e0;
}

.score-box {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #27ae60;
    padding: 10px 0;
}

.footer {
    text-align: center;
    color: #7f8c8d;
    font-size: 14px;
    margin-top: 40px;
    padding-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title-text">🎤 Grammar Scoring Engine</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle-text">Upload an English audio file and get instant grammar feedback</div>',
    unsafe_allow_html=True
)

# ---------- FILE UPLOADER ----------
uploaded_file = st.file_uploader(
    "📂 Upload Audio File (WAV / MP3)",
    type=["wav", "mp3"]
)

# ---------- PROCESS ----------
if uploaded_file is not None:
    temp_path = None
    try:
        with st.spinner("🔍 Transcribing audio & analyzing grammar... Please wait"):
            with tempfile.NamedTemporaryFile(delete=False) as temp:
                temp.write(uploaded_file.read())
                temp_path = temp.name

            transcription = transcribe_audio(temp_path)
            cleaned_text = clean_text(transcription)
            score, errors = calculate_grammar_score(cleaned_text)

    except Exception as e:
        st.error(f"❌ Error occurred: {e}")
        transcription, cleaned_text, score, errors = "", "", 0, 0

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

    # ---------- RESULTS ----------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📝 Transcription")
    st.write(transcription)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧹 Cleaned Text")
    st.write(cleaned_text)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Grammar Score")

    st.markdown(f'<div class="score-box">{score} / 10</div>', unsafe_allow_html=True)
    st.write(f"❌ Grammar Errors Found: **{errors}**")

    if score >= 8:
        st.success("✅ Excellent grammar!")
    elif score >= 5:
        st.warning("⚠️ Average grammar, some improvements needed.")
    else:
        st.error("❌ Poor grammar, needs improvement.")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown(
    '<div class="footer">Built with ❤️ using Whisper, LanguageTool & Streamlit</div>',
    unsafe_allow_html=True
)
