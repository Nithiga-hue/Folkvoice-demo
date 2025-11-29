import whisper
import tempfile
import io

# Load model once (small model used in notebook)
# You can change "small" to "base" or "medium" if needed
model = whisper.load_model("small")

def transcribe_tamil_audio(uploaded_audio_file):
    """
    Takes an uploaded audio file from Streamlit (file uploader)
    Returns the Tamil transcription text.
    """

    # Save uploaded audio to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_audio_file.read())
        temp_path = tmp.name

    # Transcribe using Whisper
    result = model.transcribe(temp_path, language="ta")

    return result.get("text", "")
