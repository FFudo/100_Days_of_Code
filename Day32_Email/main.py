import datetime as dt
import random
import smtplib

import pandas as pd
from config import *

##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
df = pd.read_csv("Day32_Email/birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_day = now.day
current_month = now.month

result = df[(df["day"] == current_day) & (df["month"] == current_month)]
data = result.to_dict("records")

for dict in data:
    name = dict["name"]
    to_email = dict["email"]
    choice = random.randint(1, 3)
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(f"Day32_Email/letter_templates/letter_{choice}.txt") as f:
        text = f.read()
        text = text.replace("[NAME]", name)

    # # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.mailersend.net", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject: Happy Birthday\n\n{text}",
        )
