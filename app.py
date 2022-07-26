# Contains all the endpoints for this application
from flask import render_template

from database.models import User
from init import create_app, db

app = create_app()


@app.route('/')
def main_page():
    users = db.session.query(User).count()
    return render_template("index.html", user_count=users)


@app.route('/my-account')
def my_account_page():
    return render_template("my_account.html")


if __name__ == '__main__':
    app.run()
