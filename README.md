# Regional News Summarizer

## Setup
1. Open this folder in VS Code (File > Open Folder)
2. python -m venv venv
3. venv\Scripts\activate   (Windows)  |  source venv/bin/activate  (Mac/Linux)
4. pip install -r requirements.txt
5. Put your Gemini key in .env  (GEMINI_API_KEY=...)
6. python test_key.py
7. streamlit run app.py

## Trained model mode
Unzip my_model.zip from Colab into the my_model/ folder.
Gemini mode works without it.

## Files
config.py            settings, model name, languages, prompt
scraper.py           URL -> article text
summarizer.py        Gemini summarizer
local_summarizer.py  your fine-tuned model
translator.py        English summary -> regional language
app.py               Streamlit interface
list_models.py       prints models your key can use
