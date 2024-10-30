import csv

with open("./people-100-tabs.csv") as file:
    data = csv.reader(file, delimiter="\t")
    for row in data:
        print(row)
