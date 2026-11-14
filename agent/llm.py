
import os
import time
from google import genai
from google.genai import errors
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_ai(question):
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=question
            )
            return response.text

        except errors.ServerError as e:
            if attempt == 2:
                return f"Gemini service unavailable: {e}"

            time.sleep(2 ** (attempt + 1))

        except Exception as e:
            return f"Error: {e}"

