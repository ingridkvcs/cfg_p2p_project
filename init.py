# Creates the Flask Application and configures and connects to the server instance using SQLAlchemy

from Investr import Flask, SQLAlchemy, User, Base, csv
from Investr import db_name, port, host, password, username

db = SQLAlchemy()
server = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{db_name}?auth_plugin=mysql_native_password'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fCjTw#zFc%sKcyBtU^TS85KY^9NEJFaCKqpv^vV93MPv@RkRCftqmdQAVtTjrsMF'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = server
    db.init_app(app)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

# Creates the database in the instance

engine = db.create_engine(sa_url=server, engine_opts={})

def create_db():
    with engine.connect() as connection:
        connection.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
    engine.execute(f"USE {db_name};")
    Base.metadata.create_all(engine)

print("Populating with mock data")

#with engine.connect() as connection:
   # result = connection.execute("select username from users")
   # for row in result:
  #      print("username:", row['username'])


#engine.execute(f"USE {db_name}")
#with open("files/mocked_data_user.csv", "r") as csvfile:
 #       csvreader = csv.reader(csvfile)
  #      next(csvreader, None)
   #     for row in csvreader:
    #        user = User(id=row[0], first_name=row[1], last_name=row[2], email=row[3], password=row[4])
     #       db.session.add(user) 
