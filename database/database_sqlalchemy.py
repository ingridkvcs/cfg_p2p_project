from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database.db_config import db_name, port, host, password, username

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{db_name}'
    db.init_app(app)
    return app
