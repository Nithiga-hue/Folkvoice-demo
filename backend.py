# backend.py
import whisper

# Load model once (faster)
model = whisper.load_model("small")



def transcribe_tamil_audio(audio_file):
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.read())

    result = model.transcribe("temp_audio.wav", language="ta")

    full_text = result["text"].strip()

    words = full_text.split()

    selected_words = words[ :6]

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
