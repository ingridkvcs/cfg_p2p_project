# Creates the Flask Application and configures and connects to the server instance using SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database.db_config import db_name, port, host, password, username

db = SQLAlchemy()
server = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/'

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = server
    db.init_app(app)
    return app

# Creates the database in the instance

engine = SQLAlchemy.create_engine(self=SQLAlchemy, sa_url=server, engine_opts={})

engine.execute(f"CREATE DATABASE {db_name}")
engine.execute("USE {db_name}")