# https://www.youtube.com/watch?v=XVv6mJpFOb0

from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://raw.githubusercontent.com/jimdevops19/codesnippets/refs/heads/main/Python%20Web%20Scraping/01%20-%20Scraping%20Basics/home.html"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

titles = [title.get_text() for title in soup.find_all("h5", class_="card-title")]
descriptions = [
    description.get_text() for description in soup.find_all("p", class_="card-text")
]
price_texts = [
    price_text.get_text() for price_text in soup.find_all("a", class_="btn-primary")
]

prices = []
for price_text in price_texts:
    price = int(price_text.split()[-1].replace("$", ""))
    prices.append(price)

courses_df = pd.DataFrame(
    {
        "title": titles,
        "description": descriptions,
        "price": prices,
    }
)
