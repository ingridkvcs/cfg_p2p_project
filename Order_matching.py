from Investr import db
from database.models import Order, Contract
from datetime import datetime


def lend(borrow_orders, current_order):
    for borrow_order in borrow_orders:
        if current_order.interest_rate <= borrow_order.interest_rate:
            if current_order.amount > 0:
                contract_amount = min(current_order.amount, borrow_order.amount)
                current_order.amount -= contract_amount
                borrow_order.amount -= contract_amount

                if borrow_order.amount == 0:
                    db.session.delete(borrow_order)

                create_contract(borrow_order.user_id, current_order.user_id, contract_amount,
                                borrow_order.interest_rate)


def borrow(lending_orders, current_order):
    for lending_order in lending_orders:
        if current_order.interest_rate >= lending_order.interest_rate:
            if current_order.amount > 0:
                contract_amount = min(current_order.amount, lending_order.amount)
                current_order.amount -= contract_amount
                lending_order.amount -= contract_amount

                if lending_order.amount == 0:
                    db.session.delete(lending_order)

                create_contract(current_order.user_id, lending_order.user_id, contract_amount,
                                lending_order.interest_rate)


def match_orders(current_order):
    # Get lend orders with the lowest interest rate
    lend_orders = db.session.query(Order) \
        .filter(Order.order_type == 'lend') \
        .order_by(Order.interest_rate.asc()) \
        .all()

    # Get borrow orders with the highest interest rate
    borrow_orders = db.session.query(Order) \
        .filter(Order.order_type == 'borrow') \
        .order_by(Order.interest_rate.desc()) \
        .all()

    if current_order.order_type == 'lend':
        lend(borrow_orders, current_order)

    elif current_order.order_type == 'borrow':
        borrow(lend_orders, current_order)


def create_contract(borrower_id, lender_id, amount, interest_rate):
    contract = Contract()
    contract.borrower_id = borrower_id
    contract.lender_id = lender_id
    contract.amount = amount
    contract.interest_rate = interest_rate
    contract.date_created = datetime.today()

    db.session.add(contract)
