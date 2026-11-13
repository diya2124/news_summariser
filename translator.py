from llm import generate
from deep_translator import GoogleTranslator

LANG_CODES = {
    "Kannada": "kn", "Hindi": "hi", "Marathi": "mr", "Tamil": "ta",
    "Telugu": "te", "Malayalam": "ml", "Bengali": "bn",
    "Gujarati": "gu", "Punjabi": "pa", "English": "en",
}


def translate(text: str, language: str) -> str:
    try:
        return generate(
            f"Translate this into {language}. Keep names, numbers and dates "
            f"exact. Output only the translation:\n\n{text}",
            system="You are a professional news translator.",
        )
    except Exception:
        # Gemini unavailable: free Google Translate fallback
        code = LANG_CODES.get(language, "en")
        return GoogleTranslator(source="auto", target=code).translate(text)