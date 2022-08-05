# Contains all the endpoints for this application
from Investr import logging
from Investr import render_template, request, url_for, flash
from Investr import LoginManager, login_required, current_user
from Investr import redirect

from Investr import User
from init import create_app, create_db, db, create_tables, create_populate_user

#Temporary while debugging
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)


create_db()
create_tables()

app = create_app()
app.app_context().push()

create_populate_user()

#create_db()

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


headers = ('Order Id', 'Type of Order', 'Amount', 'Interest')
orders = [

    (1234, 'Lending', 5500, 3.5),
    (3264, 'Borrowing', 5500, 3.1),
    (1434, 'Lending', 5500, 3.8),
    (5237, 'Borrowing', 7500, 5.5),
    (1838, 'Borrowing', 8800, 2.5),
    (1234, 'Lending', 5000, 1.5)
]


@app.route('/my-account')
@login_required
def my_account_page():
    return render_template("my_account.html", first_name=current_user.first_name, last_name=current_user.last_name,
                           headers=headers, orders=orders)


@app.route('/order-book')
@login_required
def order_book():
    return render_template('order_book.html')


@app.route('/create-order', methods=['POST'])
@login_required
def create_order():
    type = request.form.get('type')
    amount = request.form.get('amount')
    interest_rate = request.form.get('interest_rate')

    if not amount or not amount.isnumeric() or int(amount) <= 0:
        flash('Amount must be greater than 0.')
        return redirect(url_for('order_book'))

    if not interest_rate or not interest_rate.isnumeric() or int(interest_rate) <= 0:
        flash('Interest rate must be greater than 0.')
        return redirect(url_for('order_book'))

    return redirect(url_for('order_book'))


if __name__ == '__main__':
    app.run(debug=True)
