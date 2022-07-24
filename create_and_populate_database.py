import csv

from app import db
from database.database_sqlalchemy import create_app
from database.models import User

app = create_app()
app.app_context().push()

print("Creating tables")
db.create_all()

print("Populating with mock data")
with open("files/MOCK_DATA.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)
    for row in csvreader:
        user = User(id=row[0], first_name=row[1], last_name=row[2], email=row[3], password=row[4])
        db.session.add(user)

db.session.commit()
print("Successfully created the tables and populated them with mock data.")
