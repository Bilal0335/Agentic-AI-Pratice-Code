# import os
# import smtplib
# from email.message import EmailMessage
# from dotenv import load_dotenv

# # Load .env variables
# load_dotenv()

# EMAIL_SENDER = os.getenv("EMAIL_SENDER")
# EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
# EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# # Create email content
# subject = "Mail sent using Python"
# body = """
# Hi there,

# This email is sent using Python and Gmail SMTP with a secure app password.

# Thanks,
# Your Script
# """

# # Build the email
# email = EmailMessage()
# email['From'] = EMAIL_SENDER
# email['To'] = EMAIL_RECEIVER
# email['Subject'] = subject
# email.set_content(body)

# try:
#     # Connect to Gmail SMTP server
#     with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
#         smtp.ehlo()
#         smtp.starttls()  # Secure the connection
#         smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
#         smtp.send_message(email)
#         print("✅ Email sent successfully!")

# except Exception as e:
#     print("❌ Failed to send email:", e)





import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Get user inputs
receiver = input("📧 Enter recipient's email address: ")
subject = input("📌 Enter the email subject: ")
body = input("📝 Enter the email body:\n")

# Build email
email = EmailMessage()
email['From'] = EMAIL_SENDER
email['To'] = receiver
email['Subject'] = subject
email.set_content(body)

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(email)
        print("✅ Email sent successfully to", receiver)

except Exception as e:
    print("❌ Failed to send email:", e)
