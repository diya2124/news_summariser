import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODELS = [
    "gemini-3.8-flash",      # main
    "models/gemini-3.6-flash",  # e.g. a flash-lite model from list_models.py
]
MODEL = MODELS[0]            # keeps test_key.py working # change here if Google renames the model
MAX_CHARS = 15000            # article text sent to the model

LANGUAGES = [
    "Kannada", "Hindi", "Marathi", "Tamil", "Telugu",
    "Malayalam", "Bengali", "Gujarati", "Punjabi", "English",
]

SYSTEM_PROMPT = """You are a news summarization assistant.
Summarize the given news article faithfully in the requested language.
Rules:
- Use only facts from the article. Do not add outside information.
- Keep names, places, numbers and dates accurate.
- Use simple, natural language that a common reader understands.
- Format: a one-line headline, then 3-5 bullet points, then a one-line 'Why it matters'."""
