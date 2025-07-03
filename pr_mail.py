import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from litellm import completion

# Load .env variables
load_dotenv()

# Load API Key and email config
gemini_api_key = os.getenv("GEMINI_API_KEYS")
email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("EMAIL_PASSWORD")
email_receiver = os.getenv("EMAIL_RECEIVER")

# Prompt to send
prompt = "Give me either one motivational quote or one interesting historical fact."

def get_gemini_message():
    try:
        response = completion(
            model="gemini/gemini-2.0-flash",
            messages=[{"role": "user", "content": prompt}],
            api_key=gemini_api_key
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error from Gemini: {e}"

def send_email(message):
    try:
        email = EmailMessage()
        email['From'] = email_sender
        email['To'] = email_receiver
        email['Subject'] = "🌟 Your Daily Motivation or Fact!"
        email.set_content(message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_sender, email_password)
            smtp.send_message(email)

        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)

def main():
    print("📬 Fetching content from Gemini...")
    content = get_gemini_message()
    print("📝 Sending this by email:")
    print(content)
    send_email(content)

if __name__ == "__main__":
    main()
