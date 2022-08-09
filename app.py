# Contains all the endpoints for this application
from sqlalchemy import or_

from Investr import logging
from Investr import render_template, request, url_for, flash
from Investr import LoginManager, login_required, current_user
from Investr import redirect, SQLAlchemy
from Investr import create_db, create_tables, create_populate_users, create_populate_orders, create_app, db
from Investr import User, Order

# Temporary while debugging
# logging.basicConfig()
# logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
# logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)
from database.models import Contract
from init import create_populate_contracts

create_db()
create_tables()

app = create_app()
app.app_context().push()

create_populate_users()
create_populate_orders()
create_populate_contracts()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def main_page():
    users = db.session.query(User).count()
    return render_template("index.html", user_count=users)


@app.route('/my-account')
@login_required
def my_account_page():
    contracts = db.session.query(Contract) \
        .filter(or_(Contract.borrower_id == current_user.id, Contract.lender_id == current_user.id)) \
        .order_by(Contract.date_created.desc()) \
        .all()

    for contract in contracts:
        if current_user.id == contract.borrower_id:
            contract.type = "borrow"
        elif current_user.id == contract.lender_id:
            contract.type = "lend"
        else:
            raise Exception("The specified user is not part of this contract.")

    orders = db.session.query(Order) \
        .filter(Order.user_id == current_user.id) \
        .all()


    return render_template("my_account.html", first_name=current_user.first_name, last_name=current_user.last_name, contracts=contracts, orders=orders)


# ("my_account.html", first_name=current_user.first_name, last_name=current_user.last_name,
#                            headers=headers, orders=orders)

@app.route('/order-book')
@login_required
def order_book():
    # Get lend orders with the lowest interest rate
    lend_orders = db.session.query(Order) \
        .filter(Order.order_type == 'lend') \
        .order_by(Order.interest_rate.asc()) \
        .limit(5) \
        .all()[::-1]

    # Get borrow orders with the highest interest rate
    borrow_orders = db.session.query(Order) \
        .filter(Order.order_type == 'borrow') \
        .order_by(Order.interest_rate.desc()) \
        .limit(5) \
        .all()

    return render_template('order_book.html', lend_orders=lend_orders, borrow_orders=borrow_orders)


@app.route('/order', methods=['POST'])
@login_required
def create_order():
    user_id = db.session.query(current_user.id)
    order_type = request.form.get('order_type')
    amount = request.form.get('amount')
    interest_rate = request.form.get('interest_rate')

    if not amount or not amount.isnumeric() or int(amount) <= 0:
        flash('Amount must be greater than 0.')
        return redirect(url_for('order_book'))

    if not interest_rate or not interest_rate.isnumeric() or float(interest_rate) <= 0:
        flash('Interest rate must be greater than 0.')
        return redirect(url_for('order_book'))

    order = Order()
    order.user_id = user_id
    order.order_type = order_type
    order.amount = int(amount)
    order.interest_rate = float(interest_rate)

    try:
        db.session.add(order)
        db.session.commit()
    except SQLAlchemy.exc.IntegrityError:
        db.session.rollback()

    return redirect(url_for('order_book'))


@app.route('/order', methods=['DELETE'])
# @login_required
def delete_order():
    id = request.form.get('id')
    return {}


if __name__ == '__main__':
    # app.run(debug=true)
    app.run()
