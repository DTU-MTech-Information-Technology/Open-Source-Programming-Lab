import csv


def read_specific_columns(filename, columns):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            selected_columns = [row[column] for column in columns]
            print(selected_columns)


read_specific_columns("contacts.csv", ["Name"])
