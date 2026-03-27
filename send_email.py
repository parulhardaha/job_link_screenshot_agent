import email, smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from screenshot import take_screenshots

load_dotenv()

def send_email(results):
    msg = EmailMessage()
    msg["Subject"] = "Job Screenshot Report"
    msg["From"] = os.getenv("EMAIL")
    msg["To"] = os.getenv("RECEIVER_EMAIL")

    body = "Results:\n\n"

    for r in results:
        if r["status"] == "success":
            body += f"SUCCESS: {r['url']}\n"
        else:
            body += f"FAILED: {r['url']} | {r['error']}\n"

    msg.set_content(body) #puts the body inside the email message

    #attach screenshots
    for r in results:
        if r["status"] == "success":
            with open(r["file"], "rb") as f:
                msg.add_attachment(f.read(), maintype="image", subtype="png", filename=r["file"])

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp: #connects to the gmail smtp server
        smtp.login(os.getenv("EMAIL"), os.getenv("APP_PASSWORD"))
        smtp.send_message(msg)


test_urls=[
     "https://www.linkedin.com/jobs/",
   "https://www.linkedin.com/jobs/view/0987654321/"

    ]

results=take_screenshots(test_urls)
print(results)
send_email(results)