import requests
from config import api_key

parameters = {
    "lat": 48.208176,
    "lon": 16.373819,
    "appid": api_key,
    "cnt": 4,
}

respone = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", params=parameters
)
respone.raise_for_status()
data = respone.json()["list"]

will_rain = False

for hour in data:
    if int(hour["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    print("It will rain")
