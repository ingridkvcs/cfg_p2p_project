# Defines the model for the database tables
from Investr import Column, ForeignKey, Integer, String, Float, Date
from Investr import UserMixin
from Investr import datetime
from Investr import declarative_base

print("Print base")
Base = declarative_base()


class User(UserMixin, Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(200), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email


class Order(Base):
    __tablename__ = "Order"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    order_type = Column(String(80), nullable=False)
    amount = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)

    def __repr__(self):
        return '<Order %r>' % self.id


class Contract(Base):
    __tablename__ = "Contract"
    id = Column(Integer, primary_key=True, autoincrement=True)
    borrower_id = Column(Integer, ForeignKey('Order.id'), nullable=False)
    lender_id = Column(Integer, ForeignKey('Order.id'), nullable=False)
    amount = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)
    date_created = Column(Date(), default=datetime.utcnow)

    def __repr__(self):
        return '<Contract %r>' % self.id
