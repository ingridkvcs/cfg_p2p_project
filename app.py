# Contains all the endpoints for this application
from flask import render_template

from database.models import User
from init import create_app, db

app = create_app()


@app.route('/')
def main_page():
    users = db.session.query(User).count()
    return render_template("index.html", user_count=users)


orders = [

    (1234, 'Lending', 5500, 3.5),
    (3264, 'Borrowing', 5500, 3.1),
    (1434, 'Lending', 5500, 3.8),
    (5237, 'Borrowing', 7500, 5.5),
    (1838, 'Borrowing', 8800, 2.5),
    (1234, 'Lending', 5000, 1.5),
    (1634, 'Borrowing', 6900, 4.5),
    (6234, 'Lending', 2500, 3.5)
]


@app.route('/my-account')
def my_account_page():
    return render_template("my_account.html", orders=orders)


if __name__ == '__main__':
    app.run()
