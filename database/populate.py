from db import db, User
import csv

db.create_all()

with open("../files/MOCK_DATA.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)
    for row in csvreader:
        user = User(id=row[0], first_name =row[1], last_name= row[2], email=row[3], password=row[4])
        db.session.add(user)
db.session.commit()

