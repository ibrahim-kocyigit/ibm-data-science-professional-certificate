import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

html_data = requests.get(URL).text

soup = BeautifulSoup(html_data, "html.parser")

tesla_revenue = pd.read_html(str(soup))[1]
tesla_revenue.rename(
    columns={
        "Tesla Quarterly Revenue (Millions of US $)": "Date",
        "Tesla Quarterly Revenue (Millions of US $).1": "Revenue",
    },
    inplace=True,
)

tesla_revenue["Revenue"] = (
    tesla_revenue["Revenue"].str.replace(",", "").str.replace("$", "")
)

tesla_revenue

URL_2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

html_data_2 = requests.get(URL_2).text

soup_2 = BeautifulSoup(html_data_2, "html.parser")

gme_revenue = pd.read_html(str(soup_2))[1]
gme_revenue.rename(
    columns={
        "GameStop Quarterly Revenue (Millions of US $)": "Date",
        "GameStop Quarterly Revenue (Millions of US $).1": "Revenue",
    },
    inplace=True,
)

gme_revenue["Revenue"] = (
    gme_revenue["Revenue"].str.replace(",", "").str.replace("$", "")
)

gme_revenue
