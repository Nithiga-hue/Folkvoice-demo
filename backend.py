from faster_whisper import WhisperModel
import io
import time
from openai import OpenAI, RateLimitError

client = OpenAI()

def generate_tamil_speech(text):
    for _ in range(3):  # retry 3 times
        try:
            response = client.audio.speech.create(
                model="gpt-4o-mini-tts",
                voice="alloy",
                input=text
            )
            return response.read()
        except RateLimitError:
            time.sleep(2)
    raise Exception("Too many requests. Try again later.")

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



