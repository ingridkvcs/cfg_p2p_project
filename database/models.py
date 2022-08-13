# Defines the model for the database tables
from Lendr import Column, ForeignKey, Integer, String, Float, Date
from Lendr import UserMixin, declarative_base
from Lendr import datetime

print("Print base")
Base = declarative_base()


# noinspection SpellCheckingInspection
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
    amount = Column(Integer, nullable=False)
    interest_rate = Column(Float, nullable=False)
    order_status = Column(String(80), default="Pending")

    def __repr__(self):
        return '<Order %r>' % self.id


class Contract(Base):
    __tablename__ = "Contract"
    id = Column(Integer, primary_key=True, autoincrement=True)
    borrower_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    lender_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    interest_rate = Column(Float, nullable=False)
    date_created = Column(Date(), default=datetime.utcnow)

    def __repr__(self):
        return '<Contract %r>' % self.id
