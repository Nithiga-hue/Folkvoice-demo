import streamlit as st
import backend
from backend import generate_tamil_speech

st.title("Kadhai Visai - A Folk Voice Archive")

uploaded = st.file_uploader("Upload Tamil audio", type=["wav", "mp3", "m4a"])

if uploaded:
    st.success("Audio uploaded successfully!")

    words, emotion, full_text = backend.transcribe_tamil_audio(uploaded)

    st.subheader("Full Transcription")
    st.write(full_text)

    st.subheader("Extracted Words")
    st.write(", ".join(words))

    st.subheader("Detected Emotion")
    st.write(emotion)

    slang = st.selectbox("Choose slang", ["Madurai", "Kongu", "Nellai"])

    # Generate narration text in chosen slang and save in session_state
if st.button("Generate Narration"):
    output = backend.narrate_in_slang(words, slang)
    st.session_state["narration_output"] = output
    st.subheader(f"Narration in {slang} Slang")
    st.write(output)

# Show the narration (if exists)
if "narration_output" in st.session_state:
    st.subheader("Narration Preview")
    st.write(st.session_state["narration_output"])

# Button to generate audio from the narration stored in session_state
narration_text = st.text_area("Enter Tamil text:")

if st.button("Generate Audio"):
    with st.spinner("Generating speech..."):
        try:
            audio_bytes = backend.generate_tamil_speech(narration_text)
            st.audio(audio_bytes, format="audio/wav")
        except Exception as e:
            st.error(f"Error: {e}")






