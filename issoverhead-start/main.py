import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 32.485760  # Your latitude
MY_LONG = -7.867160  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # this line is import if the code status != 200 (success)
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


def look_up():
    my_email = "abdelhamidsalhi618@gmail.com"
    password = "zrfddsydoyadycgv"
    message = "Subject:The ISS is over you now👆👆\n\nThe ISS is over you Now, look at the sky to see it!"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="essalhi12345@yahoo.com", msg=message)


# If the ISS is close to my current position,
while True:
    time.sleep(60)
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        # and it is currently dark
        if time_now >= sunset or time_now <= sunrise:
            # Then send me an email to tell me to look up.
            look_up()
    # BONUS: run the code every 60 seconds.
    print("I did executed and time is: ", datetime.now())
    # if datetime.now().second == 0:
    #     if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
    #         # and it is currently dark
    #         if time_now >= sunset or time_now <= sunrise:
    #             # Then send me an email to tell me to look up.
    #             look_up()
    #     # BONUS: run the code every 60 seconds.
    #     print("I did executed and time is: ", datetime.now())

