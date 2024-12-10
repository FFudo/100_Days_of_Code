import datetime, smtplib, random

my_email = "MS_RV8TEx@trial-0p7kx4xyd78l9yjr.mlsender.net"
password = "rpcLKxav6woMNYyI"

with open("Day32_Email/quotes.txt") as f:
    data = f.readlines()
    quote = random.choice(data)

now = datetime.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with smtplib.SMTP("smtp.mailersend.net", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="", msg=f"Subject: Quote of the Day\n\n{quote}")
        connection.close()
