from google import genai
from config import API_KEY, MODEL

client = genai.Client(api_key=API_KEY)
r = client.models.generate_content(model=MODEL, contents="Say hello in Kannada")
print(r.text)
