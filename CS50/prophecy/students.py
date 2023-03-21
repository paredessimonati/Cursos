import csv
from cs50 import SQL


# Open database
db = SQL("sqlite:///students.db")
# Read csv file
with open("students.csv", 'r') as file:
    reader = csv.reader(file)
    # Skips first line
    next(reader)
    # Initialize dictionary for houses
    houses = {}
    # Goes through each line
    for row in reader:
        # Looks in dictionary for a match with row[2]
        if row[2] not in houses.values():
            # IF there's no match, then creates a new entry in the dictionary
            houses[len(houses)] = row[2]
            # Inserts data into houses table each time the function doesnt find the house name in dictionary.
            rows = db.execute("INSERT or IGNORE INTO houses (id, house) VALUES(?, ?)", len(houses), houses[len(houses) - 1])
        # Inserts data each time the row advances
        rows = db.execute("INSERT or IGNORE INTO students (id, name) VALUES(?, ?)", int(row[0]), row[1])
        # creates variables key and value and assigns them to the key and values from dictionary
        for key, value in houses.items():
            # If the row[2] is the same as the value then insert data into assignment (so we can get the correct id from the house)
            if value == row[2]:
                rows = db.execute("INSERT or IGNORE INTO assignments (student_id, house_id) VALUES(?, ?)", int(row[0]), int(key + 1))
