import smtplib
from email.message import EmailMessage


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to

    user = "essalhi12345@gmail.com"
    msg["from"] = user
    password = "fyykbkhagtivvnjz"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


if __name__ == "__main__":
    message = "Hello dear patient, please prepare yourself to enter the room in 30min. the doctor will be" \
              " waiting for you"
    email_alert("your turn", message, "youssrahakane8@gmail.com")
    print("email sent")

