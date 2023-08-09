import smtplib
import datetime as dt
import random


def send_quote_email(quote):
    my_email = "abdelhamidsalhi618@gmail.com"
    password = "zrfddsydoyadycgv"
    # my_email = "essalhi12345@yahoo.com"
    # password = "M6VP6j&2qu9RwZ*"

    # smtp.mail.yahoo.com is the gmail service provider
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="essalhi12345@yahoo.com",
                            msg=f"Subject:Today's quote\n\n{quote}")
    # connection.close()


# check if day is today then send the quote
now = dt.datetime.now()
print(now.weekday())
if now.weekday() == 3:
    with open("quotes.txt", mode="r") as file:
        quotes = file.readlines()
    quote = random.choice(quotes)
    send_quote_email(quote)
# date_of_birth = dt.datetime(2000, 5, 6)
# print(date_of_birth)

