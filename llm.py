import time
from google import genai
from google.genai import types
from config import API_KEY, MODELS

client = genai.Client(
    api_key=API_KEY,
    http_options=types.HttpOptions(timeout=60000),  # never hangs forever
)


def generate(prompt: str, system: str | None = None) -> str:
    """Try each model in MODELS, retrying when Google is busy."""
    config = types.GenerateContentConfig(system_instruction=system) if system else None
    last_error = None

    for model in MODELS:
        for attempt in range(3):
            try:
                r = client.models.generate_content(
                    model=model, contents=prompt, config=config
                )
                return r.text
            except Exception as e:
                last_error = e
                if any(x in str(e) for x in ("503", "429", "UNAVAILABLE")):
                    time.sleep(2 * (attempt + 1))   # wait 2s, 4s, 6s
                    continue
                break   # other error: try next model

    raise last_error