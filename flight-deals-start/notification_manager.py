import smtplib
from twilio.rest import Client


TWILIO_SID = "AC4e6db2f80d2149b8fbd9cd037615b0df"
TWILIO_AUTH_TOKEN = "4216a3ca54c322a58eb6682e220ad098"
TWILIO_PHONE = "+14143103612"
TARGET_PHONE = "+212618732987"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_sms(self, message):
        # send SMS
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

        client.messages.create(
            body=message,
            from_='+14143103612',
            to='+212618732987'
        )

    def send_emails(self, message, users_data):
        my_email = "abdelhamidsalhi618@gmail.com"
        password = "pwfhplrwavlaaesx"
        email_text = f"Subject:NEW LOW PRICE ALERT!\n\n{message}"  # add the link

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for record in users_data:
                connection.sendmail(from_addr=my_email, to_addrs=record['email'], msg=email_text.encode('utf-8'))
                print("email sent")
