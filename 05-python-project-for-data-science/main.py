import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

html_data = requests.get(URL).text

soup = BeautifulSoup(html_data, "html.parser")

tesla_revenue = pd.read_html(str(soup))[0]
tesla_revenue.rename(
    columns={
        "Tesla Annual Revenue (Millions of US $)": "Date",
        "Tesla Annual Revenue (Millions of US $).1": "Revenue",
    },
    inplace=True,
)

tesla_revenue["Revenue"] = (
    tesla_revenue["Revenue"]
    .str.replace(",", "")
    .str.replace("$", "")
    .apply(pd.to_numeric)
)
