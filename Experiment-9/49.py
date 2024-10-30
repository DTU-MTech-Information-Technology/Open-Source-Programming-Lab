import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.google.com/rss")
soup = BeautifulSoup(response.content, "xml")

for item in soup.findAll("item"):
    print(item.title.text)
    print(item.link.text)
    print(item.pubDate.text)
    print("-" * 100)