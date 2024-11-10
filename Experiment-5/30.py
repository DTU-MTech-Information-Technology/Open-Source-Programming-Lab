import json

my_dict = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roy'}, 
        {'firstName': 'Meera', 'lastName': 'Sharma'}, 
        {'firstName': 'Arun ', 'lastName': 'Batra'}
    ], 
    'teachers': [
        {'firstName': 'Amba', 'lastName': 'Bhardwaj'}, 
        {'firstName': 'Reeya', 'lastName': 'Arora '}
    ]
}

with open("data.json", "w") as file:
    json.dump(my_dict, file)
    print("Stored JSON to file")