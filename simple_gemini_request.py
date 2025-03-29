import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

SAFETY_SETTINGS = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-lite",
    safety_settings=SAFETY_SETTINGS,
    system_instruction="You are a meme-o-matic. Whatever I say, you will respond using only internet-memes and famous movie lines."
    " (E.G. one does not simply...) Feel free to also use Emojis when you need to express something visually.",
)

history = []

chat_session = model.start_chat(history=history)

response = chat_session.send_message("Who baked the first croissant in the world, and where?")
print(response.text)

