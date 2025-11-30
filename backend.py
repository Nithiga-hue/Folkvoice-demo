from faster_whisper import WhisperModel
from openai import OpenAI
import io

# initialize client once
client = OpenAI()

def generate_tamil_speech(text: str):
    """Use OpenAI TTS to create Tamil audio and return BytesIO (mp3)"""
    if not text or not text.strip():
        return None

    # Call OpenAI TTS
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text
    )

    # response is binary audio — wrap in BytesIO to return
    audio_bytes = io.BytesIO(response)
    audio_bytes.seek(0)
    return audio_bytes



# Load model once
model = WhisperModel("small")

def transcribe_tamil_audio(audio_file):
    # Save uploaded audio to temp file
    with open("temp.wav", "wb") as f:
        f.write(audio_file.read())

    # Transcribe
    segments, _ = model.transcribe("temp.wav", language="ta")

    full_text = " ".join([seg.text for seg in segments]).strip()

    words = full_text.split()
    selected_words = words[:6]
    emotion = "Neutral"

    return selected_words, emotion, full_text


def convert_word(word, slang):
    slang_dict = {
        "Madurai": {
            "ஒரு": "ஒரு",
            "ஊருல": "ஊருல்லே",
            "பெரியவர்": "பெரியவரு",
            "வாழ்ந்து": "வாழ்ந்தாரு",
            "வந்தார்": "வந்தாரு"
        },
        "Kongu": {
            "ஒரு": "ஒரு",
            "ஊருல": "ஊருல்ல",
            "பெரியவர்": "பெரியவங்க",
            "வாழ்ந்து": "வாழ்ந்தாங்க",
            "வந்தார்": "வந்தாங்க"
        },
        "Nellai": {
            "ஒரு": "ஒரு",
            "ஊருல": "ஊருலே",
            "பெரியவர்": "பெரியவரே",
            "வாழ்ந்து": "வாழ்ந்தாரே",
            "வந்தார்": "வந்தாரே"
        }
    }

    if word in slang_dict[slang]:
        return slang_dict[slang][word]

    return word


def narrate_in_slang(words, slang):
    converted = [convert_word(w, slang) for w in words]
    return " ".join(converted)



