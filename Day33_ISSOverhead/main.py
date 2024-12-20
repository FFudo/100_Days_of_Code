import smtplib
from datetime import datetime

import requests
from config import *


def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT in range(iss_latitude - 5, iss_latitude + 5) and MY_LONG in range(
        iss_longitude - 5, iss_longitude + 5
    ):
        return True
    return False


def is_dark():
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

    if time_now <= sunrise and time_now >= sunset:
        return True
    return False


if is_dark() and is_iss_close():
    with smtplib.SMTP("smtp.mailersend.net", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject: Lookup\n\nYou could see the ISS if you look up",
        )
