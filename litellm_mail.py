
# ! ----------------------------
# ! === GMAIL CODE BELOW ===
# ! ----------------------------
import os 
import smtplib
from email.message import EmailMessage
from litellm import completion
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEYS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")

# Step 1: Get user input
receiver = input("📧 Enter recipient's email address: ")
subject = input("📌 Enter the email subject: ")
prompt = input("💬 Enter your question: ")

try:
    # Get AI response
    response = completion(
        model="gemini/gemini-2.0-flash",
        messages=[
            {
                'role': 'user',
                'content': prompt   # ✅ fixed typo here
            }
        ],
        api_key=GEMINI_API_KEY
    )

    ai_content = response['choices'][0]['message']['content']
    print("🤖 Gemini says:\n", ai_content)

    # Step 2: Compose the email
    email_message = EmailMessage()
    email_message['From'] = EMAIL_SENDER  # ✅ fixed capitalization
    email_message['To'] = receiver
    email_message['Subject'] = subject
    email_message.set_content(ai_content)

    # Step 3: Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(email_message)
        print("✅ Email sent successfully to", receiver)

except Exception as e:
    print("❌ Gemini Error:", e)



# ! ----------------------------
# ! === OLD CODE BELOW ===
# ! ----------------------------
# import os
# import smtplib
# from email.message import EmailMessage
# from litellm import completion
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Get credentials from .env
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEYS")
# EMAIL_SENDER = os.getenv("EMAIL_SENDER")
# EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# # Step 1: Get user input
# receiver = input("📧 Enter recipient's email address: ")

# # Fixed subject (inspirational)
# subject = "🌟 Your Daily Dose of Inspiration"

# # Gemini prompt (can be anything, but we want motivational content)
# prompt = "Give me one short motivational quote with the author's name only."

# try:
#     # Step 2: Get AI-generated quote from Gemini
#     response = completion(
#         model="gemini/gemini-2.0-flash",
#         messages=[{'role': 'user', 'content': prompt}],
#         api_key=GEMINI_API_KEY
#     )

#     quote = response['choices'][0]['message']['content'].strip()

#     # Step 3: Build the email body like a real Gmail message
#     body = f"""Hi there,

# Here’s something to inspire you today:

# {quote}

# Wishing you a great and productive day ahead!

# Best regards,  
# AI Motivation Bot 🤖
# """

#     # Step 4: Create the email
#     email_message = EmailMessage()
#     email_message['From'] = EMAIL_SENDER
#     email_message['To'] = receiver
#     email_message['Subject'] = subject
#     email_message.set_content(body)

#     # Step 5: Send the email using Gmail SMTP
#     with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
#         smtp.ehlo()
#         smtp.starttls()
#         smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
#         smtp.send_message(email_message)
#         print(f"✅ Email sent successfully to {receiver}")

# except Exception as e:
#     print("❌ Error:", e)
