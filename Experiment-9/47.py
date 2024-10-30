from bs4 import BeautifulSoup
import requests

response = requests.get("https://catalog.data.gov/dataset?q=&sort=metadata_created+desc")
soup = BeautifulSoup(response.content, "html5lib")

dataset_name = soup.find("h3", attrs={"class": "dataset-heading"}).find("a").text
print("Most recently added dataset =", dataset_name)