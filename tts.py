import io
import re
from gtts import gTTS

LANG_CODES = {
    "Kannada": "kn", "Hindi": "hi", "Marathi": "mr", "Tamil": "ta",
    "Telugu": "te", "Malayalam": "ml", "Bengali": "bn",
    "Gujarati": "gu", "Punjabi": "pa", "English": "en",
}


def clean_for_speech(text: str) -> str:
    """Remove markdown symbols so the voice doesn't read '*' or '#'."""
    text = re.sub(r"[*#_`>]", "", text)
    text = re.sub(r"^\s*[-•]\s*", "", text, flags=re.MULTILINE)
    return re.sub(r"\n{2,}", "\n", text).strip()


def speak(text: str, language: str) -> bytes:
    """Return MP3 audio bytes of the text in the chosen language."""
    buf = io.BytesIO()
    gTTS(text=clean_for_speech(text), lang=LANG_CODES.get(language, "en")).write_to_fp(buf)
    return buf.getvalue()