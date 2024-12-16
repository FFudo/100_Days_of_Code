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
    percent = round(get_percent(), 2)

    if abs(percent) >= 1:
        news = get_news()

        print(f"{STOCK}: {percent}%")
        for n in news:
            print(f"Headline: {n["headline"]}\nBrief: {n["brief"]}")


if __name__ == "__main__":
    run_app()

