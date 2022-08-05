# When ran, this creates all the tables and populates them with mock data.
# Make sure to create the database in MySQl manually before running this.
# Running this when the tables are already populates will result in an error. Make sure to drop the tables first.

from Investr import User, csv, db


# The auto populating of User table data is not working - I will fix this tomorrow!

with open("files/mocked_data_user.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)
    for row in csvreader:
        user = User(id=row[0], first_name=row[1], last_name=row[2], email=row[3], password=row[4])
        db.session.add(user)
    db.session.commit()

print("Successfully created the tables and populated them with mock data.")
