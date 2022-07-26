from Lendr import Blueprint, render_template, url_for, redirect, request, flash
from Lendr import login_user, logout_user, login_required
from Lendr import generate_password_hash, check_password_hash
from Lendr import User, db_session

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Email or Password not correct. Try again.')
        return redirect(url_for('auth.login'))  # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('my_account_page'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


# noinspection PyArgumentList
@auth.route('/signup', methods=['POST'])
def signup_post():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')

    # check if a user already exists with this email
    user = User.query.filter_by(email=email).first()

    # if a user is found, we want to redirect back to signup page so user can try again
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user and with the password encrypted
    new_user = User(first_name=first_name, last_name=last_name, email=email,
                    password=generate_password_hash(password, method='sha256'))

    # save the user to the database
    db_session.add(new_user)
    db_session.commit()
    flash('Account successfully created, please proceed with login.')

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_page'))
