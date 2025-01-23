# https://www.youtube.com/watch?v=XVv6mJpFOb0

from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://raw.githubusercontent.com/jimdevops19/codesnippets/refs/heads/main/Python%20Web%20Scraping/01%20-%20Scraping%20Basics/home.html"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

card_titles = soup.find_all("h5", class_="card-title")
card_texts = soup.find_all("p", class_="card-text")
card_btns = soup.find_all("a", class_="btn-primary")

titles = []
descriptions = []
prices = []

for title in card_titles:
    titles.append(title.get_text())

for text in card_texts:
    descriptions.append(text.get_text())

for btn in card_btns:
    price_text = btn.get_text()
    price = int(price_text.split()[-1].replace("$", ""))
    prices.append(price)

print(titles)
print(descriptions)
print(prices)

df = pd.DataFrame(
    {
        "title": titles,
        "description": descriptions,
        "price": prices,
    }
)

print(df)
