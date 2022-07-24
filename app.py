from database.database_sqlalchemy import create_app, db
from database.models import User

app = create_app()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/database_test')
def database_test():
    user_count = db.session.query(User).count()
    return f"We have {user_count} users"


if __name__ == '__main__':
    app.run()
