from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_DIR = Path(__file__).parent / "my_model"

_tok = None
_model = None


def _load():
    global _tok, _model
    if _model is None:
        if not (MODEL_DIR / "config.json").exists():
            raise FileNotFoundError(
                f"No trained model found in {MODEL_DIR}. "
                "Copy config.json, model.safetensors and the tokenizer files "
                "directly into this folder."
            )
        _tok = AutoTokenizer.from_pretrained(str(MODEL_DIR))
        _model = AutoModelForSeq2SeqLM.from_pretrained(str(MODEL_DIR))
        _model.eval()


def summarize_local(text: str) -> str:
    """Summarize in English using your own trained model."""
    _load()
    inputs = _tok("summarize: " + text, return_tensors="pt",
                  max_length=384, truncation=True)
    ids = _model.generate(**inputs, max_length=70, num_beams=4,
                          no_repeat_ngram_size=3)
    return _tok.decode(ids[0], skip_special_tokens=True)