import streamlit as st

from backend import transcribe_tamil_audio

st.set_page_config(page_title="Folk Voice Archive - Demo", layout="centered")

st.title("Folk Voice Archive — Demo UI")

with st.sidebar:
    st.header("More to Know")
    st.write("Folktales are fun to listen to and share. This demo app showcases a pipeline for processing folk audio into transcriptions, translations, summaries, and tags.")

st.header("1. Upload Audio")
audio_file = st.file_uploader("Upload audio (mp3/wav)", type=["mp3", "wav"])
if audio_file:
    st.audio(audio_file)

st.header("2. Transcription")

if audio_file and st.button("Transcribe"):
    with st.spinner("Transcribing..."):
        tamil_text = transcribe_tamil_audio(audio_file)
    st.text_area("Tamil transcription", value=tamil_text, height=150)


st.header("3. Translation & Summary")
col1, col2 = st.columns(2)
with col1:
    english_translation = st.text_area("English translation", value="", height=120)
with col2:
    summary_text = st.text_area("Short summary (2-3 lines)", value="", height=120)

st.header("4. Emotion & Cultural Tag")
col3, col4 = st.columns([1,2])
with col3:
    emotion_label = st.selectbox("Emotion", ["", "Neutral", "Happy", "Sad", "Excited"])
with col4:
    culture_tag = st.text_input("Cultural tag (e.g., Proverb, Moral Story)")

st.write("---")
if st.button("Load sample data"):
    st.session_state['tamil_text'] = "ஒரு காலத்தில் ஒரு கிராமத்தில்..."
    st.session_state['english_translation'] = "Once upon a time in a village..."
    st.session_state['summary_text'] = "A short folk tale about a wise elder."
    st.session_state['emotion_label'] = "Neutral"
    st.session_state['culture_tag'] = "Moral Story"

if 'tamil_text' in st.session_state:
    st.experimental_rerun()
