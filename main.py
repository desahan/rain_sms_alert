import requests
from twilio.rest import Client

MY_LAT = "YOUR LAT"
MY_LONG = "YOUR LONG"
MY_NUMBER = "INSERT_YOUR_TWILIO_VERIFIED_NUMBER"

api_key = "YOUR_APP_KEY_OPEN_WEATHER"

weather_url = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

data = requests.get(url=weather_url, params=parameters)
data.raise_for_status()

weather = data.json()
six_hours = weather["list"]

will_rain = False
for each in six_hours:
    code = each["weather"][0]["id"]
    code = int(code)
    if code < 700:
        will_rain = True

account_SID = "YOUR TWILIO ACCOUNT ID"
auth_token = "YOUR TWILIO AUTH TOKEN"
twilio_number = "YOUR TWILIO NUMBER"

if will_rain:
    client = Client(account_SID, auth_token)
    message = client.messages \
        .create(
        body="Bring a brolly. It's going to rain ☂️",
        from_=twilio_number,
        to=MY_NUMBER
    )
    print(message.status)
