import smtplib
import ssl
from email.message import EmailMessage

from flask import current_app


def send_email(subject, recipients, body):
    """Send email to the recipients from the default sender specified in .env file."""
    MAIL_SERVER = current_app.config["MAIL_SERVER"]
    MAIL_PORT = current_app.config["MAIL_PORT"]
    MAIL_USERNAME = current_app.config["MAIL_USERNAME"]
    MAIL_PASSWORD = current_app.config["MAIL_PASSWORD"]

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = MAIL_USERNAME
    msg["To"] = ", ".join(recipients)
    msg.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
        try:
            server.starttls(context=context)
            server.login(MAIL_USERNAME, MAIL_PASSWORD)
            server.send_message(msg)
            current_app.logger.info("An email has been sent.\n\n" + str(msg))
        except smtplib.SMTPException as ex:
            current_app.logger.exception("Error sending mail: %r", ex)
