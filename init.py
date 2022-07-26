# Creates the Flask Application and configures and connects to the server instance using SQLAlchemy

from Lendr import Flask, SQLAlchemy, User, Order, Base, sessionmaker, scoped_session
from Lendr import exc, db_name, port, host, password, username
from Lendr import database_exists, create_database, csv, Contract

server = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{db_name}?auth_plugin=mysql_native_password'

db = SQLAlchemy()
engine = db.create_engine(sa_url=server, engine_opts={})
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = scoped_session(session)


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
    with engine.connect():
        engine.execute(f"USE {db_name};")
        Base.query = db_session.query_property()
        Base.metadata.create_all(engine)


# Populates User table with mock data
# noinspection PyArgumentList
def create_populate_users():
    try:
        with open("files/mocked_data_user.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader, None)
            for row in csvreader:
                user = User(id=row[0], first_name=row[1], last_name=row[2], email=row[3], password=row[4])
                db_session.add(user)
                db_session.commit()
        print("Populating with mock User data...")
    except exc.SQLAlchemyError:
        pass


# Populates Order table with mock data
def create_populate_orders():
    try:
        with open("files/mocked_data_orders.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader, None)
            for row in csvreader:
                order = Order(id=row[0], user_id=row[1], order_type=row[2], amount=row[3], interest_rate=row[4], )
                db_session.add(order)
                db_session.commit()
        print("Populating with Order data...")
    except exc.SQLAlchemyError:
        pass


# Populates Contract table with mock data
def create_populate_contracts():
    try:
        with open("files/mocked_data_contract.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader, None)
            for row in csvreader:
                contract = Contract(id=row[0], borrower_id=row[1], lender_id=row[2], amount=row[3], interest_rate=row[4], date_created=row[5])
                db_session.add(contract)
                db_session.commit()
        print("Populating with Contract data...")
    except exc.SQLAlchemyError as ex:
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
