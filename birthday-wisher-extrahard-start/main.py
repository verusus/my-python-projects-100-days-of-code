# #################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas as pd
import random


def send_letter(letter, receiver_email):
    my_email = "abdelhamidsalhi618@gmail.com"
    password = "zrfddsydoyadycgv"
    # my_email = "essalhi12345@yahoo.com"
    # password = "M6VP6j&2qu9RwZ*"

    # smtp.mail.yahoo.com is the gmail service provider
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=receiver_email,
                            msg=f"Subject:Happy Birthday\n\n{letter}")
    # connection.close()


current_date = dt.date.today()

pdf = pd.read_csv("birthdays.csv")
for index, row in pdf.iterrows():
    if current_date.day == row.day:
        if current_date.month == row.month:
            rand_num = random.randint(1, 3)
            with open(f"letter_templates/letter_{rand_num}.txt", mode="r") as selected_letter:
                letter_data = selected_letter.read()
            letter_data = letter_data.replace("[NAME]", row["name"])  # replace result comes as an output that's why
            # we affect it to the same var
            send_letter(letter_data, row["email"])
