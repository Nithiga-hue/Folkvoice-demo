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
    narration_text = st.session_state.get("narration_output", "").strip()
    if not narration_text:
        st.error("Please generate narration first (click 'Generate Narration').")
    else:
        audio_data = backend.generate_tamil_speech(narration_text)
        if audio_data:
            st.subheader("Tamil Narration (Audio)")
            st.audio(audio_data, format="audio/mp3")
        else:
            st.error("Failed to generate audio. Check OpenAI API key and logs.")





