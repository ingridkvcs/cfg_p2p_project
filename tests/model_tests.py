from Lendr import User, Order
from Lendr import pytest, compare_digest, flash


@pytest.fixture(scope='module')
def new_user():
    user = User(first_name="Testy", last_name="McTesty", email="test@example.com", password="password")
    return user


def test_new_user(new_user):
    # Tests that the new user details and hashed password are successfully populated
    assert new_user.first_name == "Testy"
    assert new_user.last_name == "McTesty"
    assert new_user.email == "test@example.com"
    assert compare_digest(new_user.password, "password")


@pytest.fixture(scope='module')
def new_order():
    order = Order(user_id=1, order_type="lend", amount="1000", interest_rate="3.4")
    return order


def test_new_order(new_order):
    # Tests that the new user details and hashed password are successfully populated
    assert new_order.user_id == 1
    assert new_order.order_type == "lend"
    assert new_order.amount == "1000"
    assert new_order.interest_rate == "3.4"


@pytest.fixture(scope='module')
def incorrect_order_amount():
    order = Order(user_id=1, order_type="lend", amount="lend", interest_rate="3.4")
    return order


def test_order_errors(incorrect_order_amount):
    if incorrect_order_amount.amount is str:
        assert flash('Amount must be greater than 0.')


@pytest.fixture(scope='module')
def incorrect_order_rate():
    order = Order(user_id=1, order_type="lend", amount="1000", interest_rate="0")
    return order


def test_order_rate(incorrect_order_rate):
    if incorrect_order_rate.interest_rate is 0:
        flash('Interest rate must be greater than 0.')
