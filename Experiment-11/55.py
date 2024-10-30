import json

with open("class_data.json") as file:
    data = json.loads(file.read())
    data["students"][0]["lastName"] = "Das"
    print(data)