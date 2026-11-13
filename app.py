import streamlit as st
from config import LANGUAGES, API_KEY
from scraper import get_article
from summarizer import summarize
from translator import translate
from tts import speak

st.set_page_config(page_title="Regional News Summarizer", page_icon="📰")
st.title("📰 Regional News Summarizer")

if not API_KEY:
    st.error("API key not found. Add GEMINI_API_KEY to your .env file.")
    st.stop()

mode = st.radio("Mode", ["Gemini (direct)", "My trained model + translation"])
language = st.selectbox("Summary language", LANGUAGES)
url = st.text_input("Paste news article URL")
pasted = st.text_area("...or paste the article text here", height=200)

if st.button("Summarize"):
    text = pasted.strip() or (get_article(url) if url else None)

    if not text:
        st.error("Couldn't get the article text. Try pasting it directly.")
    else:
        with st.spinner("Working..."):
            try:
                st.session_state.pop("audio", None)   # clear old audio
                if mode == "Gemini (direct)":
                    out = summarize(text, language)
                    st.session_state["result"] = {"english": None, "final": out, "language": language}
                else:
                    from local_summarizer import summarize_local
                    english = summarize_local(text)
                    final = english if language == "English" else translate(english, language)
                    st.session_state["result"] = {"english": english, "final": final, "language": language}
            except Exception as e:
                st.error(f"Something went wrong: {e}")

# show the saved result (stays on screen after other button clicks)
result = st.session_state.get("result")
if result:
    if result["english"]:
        st.subheader("English summary (your model)")
        st.write(result["english"])
        if result["language"] != "English":
            st.subheader(f"{result['language']} translation")
            st.write(result["final"])
    else:
        st.markdown(result["final"])

    if st.button("🔊 Read aloud"):
        with st.spinner("Generating voice..."):
            try:
                st.session_state["audio"] = speak(result["final"], result["language"])
            except Exception as e:
                st.error(f"Voice failed: {e}")

    if "audio" in st.session_state:
        st.audio(st.session_state["audio"], format="audio/mp3")