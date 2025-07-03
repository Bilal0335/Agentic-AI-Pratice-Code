from dotenv import load_dotenv
from litellm import completion
import os

# Load .env variables
load_dotenv()

open_ai_key = os.getenv("OPENAI_API_KEYS")
gemini_ai_key = os.getenv("GEMINI_API_KEYS")

def openai():
    try:
        response = completion(
            model="openai/gpt-4o",
            messages=[{ "content": "Hello, how are you?", "role": "user" }],
            api_key=open_ai_key
        )
        print("✅ OpenAI Response:\n", response)
    except Exception as e:
        print("❌ OpenAI Error:", e)

def gemini():
    try:
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[{ "content": "Hello, how are you?", "role": "user" }],
            api_key=gemini_ai_key
        )
        # print("✅ Gemini 1.5 Response:\n", response)
        content = response['choices'][0]['message']['content']
        print("✅ Gemini 1.5 Response:\n", content)
    except Exception as e:
        print("❌ Gemini 1.5 Error:", e)

def gemini2():
    try:
        response = completion(
            model="gemini/gemini-2.0-flash-exp",
            messages=[{ "content": "Hello, how are you?", "role": "user" }],
            api_key=gemini_ai_key
        )
        print("✅ Gemini 2.0 Response:\n", response)
    except Exception as e:
        print("❌ Gemini 2.0 Error:", e)

# Call the functions
gemini()
# gemini2()
# openai()



# ! Example # 02
# prompt = "Who is founder of Pakistan?"

# try:
#     response = completion(
#         model="gemini/gemini-2.0-flash",
#         messages=[  
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ],
#         api_key=gemini_ai_key
#     )
#     print("🤖 Gemini says:")
#     print(response['choices'][0]['message']['content'])

# except Exception as e:
#     print("❌ Gemini Error:", e)
