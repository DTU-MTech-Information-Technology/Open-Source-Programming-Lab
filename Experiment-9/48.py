import requests

response = requests.get("https://analytics.usa.gov/data/live/realtime.json").json()
print("Number of people visiting a U.S. government website right now =", response["data"][0]["active_visitors"])