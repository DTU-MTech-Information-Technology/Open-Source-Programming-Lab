import csv

with open("./people-100.csv", "r") as file:
    data = csv.reader(file)
    for row in data:
        print(row)
