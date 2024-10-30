from bs4 import BeautifulSoup
import requests

response = requests.get("https://data.gov/")
soup = BeautifulSoup(response.content, "html5lib")

count = (
    soup.find("div", attrs={"class": "hero__dataset-count"})
    .find("span", attrs={"class": "text-color-red"})
    .text
)

print("Number of datasets currently listed =", count)
