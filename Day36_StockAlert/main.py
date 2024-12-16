import requests
from config import ALPHA_APIKEY, NEWS_APIKEY

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def get_percent():
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHA_APIKEY,
    }

    response = requests.get("https://www.alphavantage.co/query", params=parameters)
    data = response.json()["Time Series (Daily)"]

    # Getting the data I want
    last_two_days = list(data.values())[:2]
    yesterday_close = float(last_two_days[0]["4. close"])
    day_before_close = float(last_two_days[1]["4. close"])

    diff = yesterday_close - day_before_close
    change_percent = (diff / yesterday_close) * 100
    return change_percent


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    parameters = {
        "apiKey": NEWS_APIKEY,
        "q": COMPANY_NAME,
        "pageSize": 3,
    }
    response = requests.get("https://newsapi.org/v2/top-headlines", params=parameters)
    data = response.json()["articles"]
    articles = []
    for article in data:
        articles.append({"headline": article["title"], "brief": article["description"]})

    return articles


def run_app():
    percent = get_percent()
    if abs(percent) >= 5:
        pass


if __name__ == "__main__":
    get_news()

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
