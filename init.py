# Creates the Flask Application and configures and connects to the server instance using SQLAlchemy

from Investr import Flask, SQLAlchemy, User, Base, csv
from Investr import exc, db_name, port, host, password, username
from Investr import database_exists, create_database

db = SQLAlchemy()
server = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{db_name}?auth_plugin=mysql_native_password'
engine = db.create_engine(sa_url=server, engine_opts={})


# Creates the database

def create_db():
    if not database_exists(server):
        print("Creating database...")
        create_database(server)
    else:
        pass


# Creates the tables within the database.

def create_tables():
    print("Creating tables...")
    with engine.connect() as connection:
        # connection.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
        engine.execute(f"USE {db_name};")
        Base.metadata.create_all(engine)



# Populates User table with mock data

def create_populate_user():
    try:
        with open("files/mocked_data_user.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader, None)
            for row in csvreader:
                user = User(id=row[0], first_name=row[1], last_name=row[2], email=row[3], password=row[4])
                db.session.add(user)
                db.session.commit()
        print("Populating with mock data...")
    except exc.SQLAlchemyError:
        pass

# Initialises the app

def create_app():
    print("Initialising app...")
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fCjTw#zFc%sKcyBtU^TS85KY^9NEJFaCKqpv^vV93MPv@RkRCftqmdQAVtTjrsMF'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = server
    db.init_app(app)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

