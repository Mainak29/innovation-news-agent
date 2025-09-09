import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_address, subject, body):
    
    sender_address = os.getenv("SENDER_EMAIL_ADDRESS")
    sender_password = os.getenv("SENDER_APP_PASSWORD")

    if not sender_address or not sender_password:
        raise ValueError("Sender email address or password not set in environment variables.")
    else:
        print(f"Sender Address: {sender_address}")
        msg = MIMEMultipart()
        msg["From"] = sender_address
        msg["To"] = to_address
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        try:
            # Connect to Gmail SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_address, sender_password)
            server.sendmail(sender_address, to_address, msg.as_string())
            server.quit()
            print(f"✅ Email sent to {to_address}")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")