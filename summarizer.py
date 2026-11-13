from llm import generate
from config import MAX_CHARS, SYSTEM_PROMPT


def summarize(text: str, language: str) -> str:
    return generate(
        f"Summarize this article in {language}:\n\n{text[:MAX_CHARS]}",
        system=SYSTEM_PROMPT,
    )