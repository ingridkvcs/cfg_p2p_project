from Lendr import LoginManager, login_required, current_user
from Lendr import fg_oya_score, fg_oya_rating, fg_oma_rating
from Lendr import fg_oma_score, fg_owa_score, fg_owa_rating, fg_pc_rating, \
    fg_pc_score
from Lendr import create_db, create_tables, create_populate_users, create_populate_orders, \
    create_app, match_orders
from Lendr import redirect, SQLAlchemy, or_, and_, delete
from Lendr import render_template, request, url_for, flash
from Lendr import User, Order, Contract, create_populate_contracts, db_session
# from Lendr import logging

# Temporary while debugging
# logging.basicConfig()
# logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
# logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

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
    users = db_session.query(User).count()
    return render_template("index.html", user_count=users)


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('img/favicon.ico')



@app.route('/fear-and-greed')
def fear_greed():
    return render_template("fear_greed.html", prevclose_score=fg_pc_score, prevclose_rating=fg_pc_rating,
                           oneweek_score=fg_owa_score, oneweek_rating=fg_owa_rating, onemonth_score=fg_oma_score,
                           onemonth_rating=fg_oma_rating, oneyear_score=fg_oya_score, oneyear_rating=fg_oya_rating)


@app.route('/my-account')
@login_required
def my_account_page():
    contracts = db_session.query(Contract) \
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

    orders = db_session.query(Order) \
        .filter(Order.user_id == current_user.id) \
        .all()

    return render_template("my_account.html", first_name=current_user.first_name, last_name=current_user.last_name,
                           contracts=contracts, orders=orders)


# ("my_account.html", first_name=current_user.first_name, last_name=current_user.last_name,
#                            headers=headers, orders=orders)

@app.route('/order-book')
@login_required
def order_book():
    # Get lend orders with the lowest interest rate
    lend_orders = db_session.query(Order) \
                      .filter(Order.order_type == 'lend') \
                      .order_by(Order.interest_rate.asc()) \
                      .limit(5) \
                      .all()[::-1]

    # Get borrow orders with the highest interest rate
    borrow_orders = db_session.query(Order) \
        .filter(Order.order_type == 'borrow') \
        .order_by(Order.interest_rate.desc()) \
        .limit(5) \
        .all()

    return render_template('order_book.html', lend_orders=lend_orders, borrow_orders=borrow_orders)


@app.route('/create-order', methods=['POST'])
@login_required
def create_order():
    user_id = db_session.query(current_user.id)
    order_type = request.form.get('order_type')
    amount = request.form.get('amount')
    interest_rate = request.form.get('interest_rate')

    if not amount or not amount.isnumeric() or int(amount) <= 0:
        flash('Amount must be greater than 0.')
        return redirect(url_for('order_book'))

    if not interest_rate or float(interest_rate) <= 0:
        flash('Interest rate must be greater than 0.')
        return redirect(url_for('order_book'))

    order = Order()
    order.user_id = user_id
    order.order_type = order_type
    order.amount = int(amount)
    order.interest_rate = float(interest_rate)

    match_orders(db_session, order)

    # Only add the order to the database if the order wasn't fully matched
    if order.amount > 0:
        db_session.add(order)

    # Save all the changes to the database and rollback all the changes if there's any error.
    try:
        db_session.commit()
    except SQLAlchemy.exc.IntegrityError:
        db_session.rollback()

    return redirect(url_for('order_book'))


@app.route('/delete-order', methods=['POST'])
@login_required
def delete_order():
    id = request.form.get('id')

    delete_command = delete(Order).where(and_(Order.id == id, Order.user_id == current_user.id))
    result = db_session.execute(delete_command)
    db_session.commit()

    if result.rowcount == 0:
        flash("Couldn't delete order")

    return redirect(url_for('my_account_page'))


if __name__ == '__main__':
    # app.run(debug=true)
    app.run(debug=True)
