import requests

response = requests.get("https://analytics.usa.gov/data/live/browsers.json").json()

visits_by_browsers = response["totals"]["by_browser"]
for key, value in visits_by_browsers.items():
    print(key, "=", value)
