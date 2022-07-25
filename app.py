# Contains all the endpoints for this application
from flask import render_template

from database.models import User
from init import create_app, db

app = create_app()


@app.route('/')
def main_page():
    users = db.session.query(User).count()
    return render_template("index.html", user_count=users)


@app.route('/database_test')
def database_test():
    user_count = db.session.query(User).count()
    return f"We have {user_count} users"


if __name__ == '__main__':
    app.run()
