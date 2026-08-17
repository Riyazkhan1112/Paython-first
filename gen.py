from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

print("API key loaded:", api_key is not None)

data = input("Enter topic for research: ")

prompt = f"""
Do deep research on the following topic:

{data}

Return the research in approximately 100 words.
"""

client = genai.Client(api_key=api_key)

interaction = client.interactions.create(model="gemini-3.6-flash", input=prompt)

print(interaction.output_text)
