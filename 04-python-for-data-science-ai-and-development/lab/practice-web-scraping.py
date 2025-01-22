import requests
from bs4 import BeautifulSoup

url = "https://www.wikipedia.org/wiki/IBM"

response = requests.get(url)

html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

print(soup)
