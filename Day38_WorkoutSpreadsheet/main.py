import datetime as dt

import requests
from config import API_KEY, APP_ID, PASSWORD
from requests.auth import HTTPBasicAuth

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("What exercise did you do today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {"query": query}

response = requests.post(url=url, headers=headers, json=params)
response.raise_for_status()
exercises = response.json()["exercises"]

sheety_url = (
    "https://api.sheety.co/f9e12a588656150d541f4b13e64631fc/myWorkouts/workouts"
)
date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%H:%M:%S")

basic = HTTPBasicAuth("ffudo", PASSWORD)

for exercise in exercises:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(url=sheety_url, json=sheet_inputs, auth=basic)
    response.raise_for_status()
