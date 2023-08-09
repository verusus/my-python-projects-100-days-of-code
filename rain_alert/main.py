import requests
from twilio.rest import Client

account_sid = 'AC4e6db2f80d2149b8fbd9cd037615b0df'
auth_token = '4216a3ca54c322a58eb6682e220ad098'

OpenWeatherMap_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "b879d00e3190f6ffdbcdf38b71ff4dd7"

parameters = {
    "lat": 64.130608,
    "lon": 28.390511,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url=OpenWeatherMap_Endpoint, params=parameters)
response.raise_for_status()
# print(response.json())
twelve_hours_data = response.json()["hourly"][0:12]  # slicing the next 12 hours

raining_hours = [hour_data["weather"][0]["id"] for hour_data in twelve_hours_data if
                 hour_data["weather"][0]["id"] < 700]
print(raining_hours)

if len(raining_hours) > 0:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="it's going to rain today. Remember to take an umbrella ☔",
        from_='+14143103612',
        to='+212618732987'
    )

    print(message.status)
