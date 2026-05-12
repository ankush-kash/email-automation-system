import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
from logger import logger
import time


load_dotenv()

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')

def send_email(receiver,subject,body,html_content=None,attachment_path = None):

    msg = EmailMessage()

    msg['From'] = EMAIL_USER
    msg['To'] = receiver
    msg['Subject'] = subject

    msg.set_content(body)

    msg.add_alternative(html_content, subtype="html")

    if attachment_path:

        with open(attachment_path,'rb') as file:

            file_data = file.read()
            file_name = file.name

            msg.add_attachment(
                file_data,
                maintype = 'application',
                subtype = 'octet-stream',
                filename = file_name
            )



    for attempt in range(3):

        try:

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

                smtp.login(EMAIL_USER, EMAIL_PASS)

                smtp.send_message(msg)

            logger.info(f"Email sent to {receiver}")

            print(f"Email sent to {receiver}")

            break

        except Exception as e:

            logger.error(
                f"Attempt {attempt + 1} failed for {receiver}: {e}"
            )

            with open("failed_emails.txt", "a") as file:

                file.write(f"{receiver}\n")

            print(f"Retrying for {receiver}...")


            time.sleep(3)


