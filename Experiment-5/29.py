my_dict = {
    'name': ['Jan', 'Feb', 'March'],
    'month': [1, 2, 3]
}

print(dict(zip(my_dict["month"], my_dict["name"])))