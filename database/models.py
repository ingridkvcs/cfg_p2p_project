# Defines the model for the database tables

from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, Table, ForeignKey, Integer, String, Float, Date

Base = declarative_base()

class User(UserMixin, Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    orders = relationship('OrderBook', backref('User'), lazy=True)

    def __repr__(self):
        return '<User %r>' % self.email

contracts = Table('contracts', Base.metadata, Column('contract_id', Integer, ForeignKey('Contract.id'), primary_key=True),
                Column('borrower_id', Integer, ForeignKey('OrderBook.id'), primary_key=True),
                Column('lender_id', Integer, ForeignKey('OrderBook.id'), primary_key=True))


class OrderBook(Base):
    __tablename__ = "OrderBook"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    order_type = Column(String(80), nullable=False)
    amount = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)
    order_status = Column(String(80), nullable=False)
    contracts = relationship('Contract', secondary=contracts, lazy = 'subquery', backref = backref('order', lazy=True))
    
    def __repr__(self):
        return '<Order %r>' % self.id

class Contract(Base):
    __tablename__ = "Contract"
    id = Column(Integer, primary_key=True, autoincrement=True)
    borrower_id = Column(Integer, ForeignKey('OrderBook.id'), nullable=False)
    lender_id = Column(Integer, ForeignKey('OrderBook.id'), nullable=False)
    amount = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)
    date_created = Column(Date(), default=datetime.utcnow)
    payment_date = Column(Date(), nullable=False)
    payment_status = Column(String(20), nullable=False)
    
    def __repr__(self):
        return '<Contract %r>' % self.id

