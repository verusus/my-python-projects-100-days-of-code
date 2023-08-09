import requests
from datetime import datetime

parameters = {
    "lat": 32.485760,
    "lng": -7.867160,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()    # this is an important line
data = response.json()
sunrise_time = data["results"]["sunrise"]
sunset_time = data["results"]["sunset"]
print(sunrise_time.split("T")[1].split(":")[0])
print(sunset_time.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)
