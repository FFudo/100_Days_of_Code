import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

with open("Day45_100Movies/movies.txt", "a", encoding="utf-8") as f:
    for title in reversed(titles):
        f.write(f"{title}\n")
