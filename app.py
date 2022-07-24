# Contains all the endpoints for this application

from database.database_sqlalchemy import create_app, db
from database.models import User

app = create_app()


@app.route('/')
def main_page():
    return


@app.route('/database_test')
def database_test():
    user_count = db.session.query(User).count()
    return f"We have {user_count} users"


if __name__ == '__main__':
    app.run()
