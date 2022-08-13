from unittest import TestCase, mock

from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from Investr import Order
from Order_matching import match_orders
from database.models import Contract

# For some reason, in order to run the test, you need to right-click on this line and run in PyCharm.


class OrderMatchDbTesting(TestCase):
    def setUp(self):
        self.session = UnifiedAlchemyMagicMock(data=[
            (
                [mock.call.query(Order),
                 mock.call.filter(Order.order_type == "lend")],
                [
                    Order(id=1, user_id=11, order_type="lend", amount=4000, interest_rate=5.5),
                    Order(id=2, user_id=12, order_type="lend", amount=3000, interest_rate=5.6),
                    Order(id=3, user_id=13, order_type="lend", amount=2000, interest_rate=5.7),
                    Order(id=4, user_id=14, order_type="lend", amount=1000, interest_rate=5.9)
                ]
            ), (
                [mock.call.query(Order),
                 mock.call.filter(Order.order_type == "borrow")],
                [
                    Order(id=5, user_id=15, order_type="borrow", amount=1000, interest_rate=4.9),
                    Order(id=6, user_id=16, order_type="borrow", amount=2000, interest_rate=4.7),
                    Order(id=7, user_id=17, order_type="borrow", amount=3000, interest_rate=4.6),
                    Order(id=8, user_id=18, order_type="borrow", amount=4000, interest_rate=4.5)
                ]
            )
        ])

    def test_givenMockOrders_whenRunningATest_thenThe4LendOrdersAnd4BorrowOrdersAreLoaded(self):
        self.assertEqual(len(self.session.query(Order).filter(Order.order_type == "lend").all()), 4)
        self.assertEqual(len(self.session.query(Order).filter(Order.order_type == "borrow").all()), 4)

    def test_givenALendOrderThatMatchesNothing_whenCallingMatchOrder_thenTheNewOrderIsUnmodifiedAndNoContractsAreCreated(self):
        test_order = Order(id=100, user_id=1, order_type="lend", amount=1000, interest_rate=5)

        match_orders(self.session, test_order)

        self.assertEqual(test_order.amount, 1000)
        self.assertEqual(self.session.query(Contract).count(), 0)

    def test_givenABorrowOrderThatMatchesNothing_whenCallingMatchOrder_thenTheNewOrderIsUnmodifiedAndNoContractsAreCreated(self):
        test_order = Order(id=100, user_id=1, order_type="borrow", amount=1000, interest_rate=5)

        match_orders(self.session, test_order)

        self.assertEqual(test_order.amount, 1000)
        self.assertEqual(self.session.query(Contract).count(), 0)

    def test_givenALendOrderThatMatchesFully_whenCallingMatchOrder_thenTheNewOrderHasAmount0(self):
        test_order = Order(id=100, user_id=1, order_type="lend", amount=500, interest_rate=4)

        match_orders(self.session, test_order)

        self.assertEqual(test_order.amount, 0)

    def test_givenALendOrderThatMatchesFully_whenCallingMatchOrder_thenTheExistingOrderIsUpdated(self):
        test_order = Order(id=100, user_id=1, order_type="lend", amount=500, interest_rate=4)

        match_orders(self.session, test_order)

        borrow_orders = self.session.query(Order).filter(Order.order_type == "borrow").all()
        self.assertEqual(borrow_orders[0].id, 5)
        self.assertEqual(borrow_orders[0].amount, 500)

    def test_givenALendOrderThatMatchesFully_whenCallingMatchOrder_thenTheCorrectContractIsCreated(self):
        test_order = Order(id=100, user_id=1, order_type="lend", amount=500, interest_rate=4)

        match_orders(self.session, test_order)

        self.assertEqual(self.session.query(Contract).count(), 1)
        contract = self.session.query(Contract).one()
        self.assertIsNotNone(contract)
        self.assertEqual(contract.borrower_id, 15)
        self.assertEqual(contract.lender_id, 1)
        self.assertEqual(contract.amount, 500)
        self.assertEqual(contract.interest_rate, 4.9)

    def test_givenABorrowOrderThatMatchesFully_whenCallingMatchOrder_thenTheNewOrderHasAmount0(self):
        test_order = Order(id=100, user_id=1, order_type="borrow", amount=500, interest_rate=6)

        match_orders(self.session, test_order)

        self.assertEqual(test_order.amount, 0)

    def test_givenABorrowOrderThatMatchesFully_whenCallingMatchOrder_thenTheExistingOrderIsUpdated(self):
        test_order = Order(id=100, user_id=1, order_type="borrow", amount=500, interest_rate=6)

        match_orders(self.session, test_order)

        lend_orders = self.session.query(Order).filter(Order.order_type == "lend").all()
        self.assertEqual(lend_orders[0].id, 1)
        self.assertEqual(lend_orders[0].amount, 3500)

    def test_givenABorrowOrderThatMatchesFully_whenCallingMatchOrder_thenTheCorrectContractIsCreated(self):
        test_order = Order(id=100, user_id=1, order_type="borrow", amount=500, interest_rate=6)

        match_orders(self.session, test_order)

        self.assertEqual(self.session.query(Contract).count(), 1)
        contract = self.session.query(Contract).one()
        self.assertIsNotNone(contract)
        self.assertEqual(contract.borrower_id, 1)
        self.assertEqual(contract.lender_id, 11)
        self.assertEqual(contract.amount, 500)
        self.assertEqual(contract.interest_rate, 5.5)
