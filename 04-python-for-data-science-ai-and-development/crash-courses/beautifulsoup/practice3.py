from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://raw.githubusercontent.com/jimdevops19/codesnippets/refs/heads/main/Python%20Web%20Scraping/01%20-%20Scraping%20Basics/home.html"

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

courses_df = pd.DataFrame(columns=["title", "description", "price"])

for div in soup.find_all("div", class_="card"):
    title = div.find(class_="card-title").text
    description = div.find(class_="card-text").text
    price_text = div.find(class_="btn-primary").text
    price = int(price_text.split()[-1].replace("$", ""))

    courses_df = pd.concat(
        [
            courses_df,
            pd.DataFrame(
                {
                    "title": [title],
                    "description": [description],
                    "price": [price],
                }
            ),
        ],
        ignore_index=True,
    )

courses_df
