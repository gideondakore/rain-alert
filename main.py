import os
import requests
from twilio.rest import Client


weather_api_key= os.environ.get("OWM_API_KEY")

account_sid = 'ACCOUNT_SSID'
auth_token = os.environ.get("AUTH_TOKEN")


MY_LAT = 6.695070
MY_LONG = -1.615800

parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":weather_api_key,
    "cnt": 4
}

weather_url = "http://api.openweathermap.org/data/2.5/forecast"
response = requests.get(url=weather_url, params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_list = weather_data["list"]

will_rain = False
for weather in weather_list:
    if weather["weather"][0]["id"] < 700:
        will_rain = True


print(will_rain)
if will_rain:
    print("rain")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:YOUR_PHONE_NUMBER_GIVEN_TO_YOU_ON_TWILIO',
        body='It\'s going to rain today. Remember to bring an umbrella',
        to='whatsapp:YOUR_VERIFIED_PHONE_NUMBER'
    )
    print(message.sid)
