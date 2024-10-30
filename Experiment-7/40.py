with open("lorem.txt", "r") as file:
    count = len(file.readlines())
    print(count)