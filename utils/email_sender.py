import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

def send_email(to_email, email_body):
    try:
        sender_email = st.secrets["SENDER_EMAIL"]
        password = st.secrets["EMAIL_PASSWORD"]
        smtp_server = st.secrets["SMTP_SERVER"]
        smtp_port = st.secrets["SMTP_PORT"]

        message = MIMEMultipart("alternative")
        message["Subject"] = "Auto Reply"
        message["From"] = sender_email
        message["To"] = to_email

        part = MIMEText(email_body, "html")
        message.attach(part)

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, to_email, message.as_string())

        return True
    except Exception as e:
        print("Email sending error:", e)
        return False
