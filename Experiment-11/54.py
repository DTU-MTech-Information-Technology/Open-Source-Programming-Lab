import json

data = {
    "students": [
        {"firstName": "Nikki", "lastName": "Roy"},
        {"firstName": "Meera", "lastName": "Sharma"},
        {"firstName": "Arun ", "lastName": "Batra"},
    ],
    "teachers": [
        {"firstName": "Amba", "lastName": "Bhardwaj"},
        {"firstName": "Reeya", "lastName": "Arora "},
    ],
}

with open("class_data.json", "w") as file:
    file.write(json.dumps(data))

with open("class_data.json") as file:
    data = json.loads(file.read())
    print(data)