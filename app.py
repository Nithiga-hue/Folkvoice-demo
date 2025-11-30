import streamlit as st
import backend

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

    if st.button("Generate Narration"):
        output = backend.narrate_in_slang(words, slang)
        st.subheader(f"Narration in {slang} Slang")
        st.write(output)

