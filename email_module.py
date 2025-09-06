import smtplib
import os
from email.message import EmailMessage

# Load from environment variables
EMAIL_USER = os.environ.get("EMAIL_USER")   # Your Gmail ID
EMAIL_PASS = os.environ.get("EMAIL_PASS")   # Your App Password

def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg["From"] = EMAIL_USER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
        return True, "Email sent successfully!"
    except Exception as e:
        return False, f"Error: {str(e)}"

