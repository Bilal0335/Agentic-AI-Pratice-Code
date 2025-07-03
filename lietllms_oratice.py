from dotenv import load_dotenv
from litellm import completion
import os

load_dotenv()  

open_ai_key = os.getenv("OPENAI_API_KEYS")
gemini_ai_key = os.getenv("GEMINI_API_KEYS")

prompt = "Who is founder of Pakistan?"

try:
    response = completion(
        model="gemini/gemini-2.0-flash",
        messages=[  
            {
                "role": "user",
                "content": prompt
            }
        ],
        api_key=gemini_ai_key
    )
    print("🤖 Gemini says:")
    print(response['choices'][0]['message']['content'])

except Exception as e:
    print("❌ Gemini Error:", e)
