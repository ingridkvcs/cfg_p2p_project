from unittest import TestCase
from Order_matching import match_orders

orders = (['Lending', 1000, 5.15],
          ['Borrowing', 1000, 4.8],
          ['Lending', 1000, 4.9],
          ['Borrowing', 1000, 5.1],
          ['Lending', 1500, 4.9],
          ['Borrowing', 2500, 5.1],
          ['Lending', 1500, 4.9],
          ['Borrowing', 500, 5.1],
          ['Lending', 500, 4.9],
          ['Borrowing', 10000, 6],
          ['Lending', 20000, 4.1])


class TestOrderMatchingFunction(TestCase):
    def test_borrow_list_no_interest_rate(self):
        expected = [[['Lending', 20000, 4.1],
                    ['Lending', 1000, 4.9],
                    ['Lending', 1500, 4.9],
                    ['Lending', 1500, 4.9],
                    ['Lending', 500, 4.9],
                    ['Lending', 1000, 5.15]],
                    [['Borrowing', 2500, 3.5],
                    ['Borrowing', 1000, 4.8],
                    ['Borrowing', 1000, 5.1],
                    ['Borrowing', 2500, 5.1],
                    ['Borrowing', 500, 5.1],
                    ['Borrowing', 10000, 6]]]
        returned = match_orders(['Borrowing', 2500, 3.5], orders)
        self.assertEqual(expected, returned)

    def test_lending_list_no_interest_rate(self):
        expected = [[['Lending', 2500, 3.5],
                    ['Lending', 20000, 4.1],
                    ['Lending', 1000, 4.9],
                    ['Lending', 1500, 4.9],
                    ['Lending', 1500, 4.9],
                    ['Lending', 500, 4.9],
                    ['Lending', 1000, 5.15]],
                    [['Borrowing', 1000, 4.8],
                    ['Borrowing', 1000, 5.1],
                    ['Borrowing', 2500, 5.1],
                    ['Borrowing', 500, 5.1],
                    ['Borrowing', 10000, 6]]]
        returned = match_orders(['Lending', 2500, 3.5], orders)
        self.assertEqual(expected, returned)

    def test_borrow_list_higher_total(self):
        expected = [[['Lending', 20000, 4.1],
                     ['Lending', 1000, 5.15]],
                    [['Borrowing', 1000, 4.8],
                     ['Borrowing', 500, 4.9],
                     ['Borrowing', 1000, 5.1],
                     ['Borrowing', 2500, 5.1],
                     ['Borrowing', 500, 5.1],
                     ['Borrowing', 10000, 6]]]
        returned = match_orders(['Borrowing', 5000, 4.9], orders)
        self.assertEqual(expected, returned)

    def test_lending_list_higher_total(self):
        expected = [[['Lending', 20000, 4.1],
                     ['Lending', 1000, 4.9],
                     ['Lending', 1500, 4.9],
                     ['Lending', 1500, 4.9],
                     ['Lending', 500, 4.9],
                     ['Lending', 1000, 5.1],
                     ['Lending', 1000, 5.15]],
                    [['Borrowing', 1000, 4.8],
                     ['Borrowing', 10000, 6]]]
        returned = match_orders(['Lending', 5000, 5.1], orders)
        self.assertEqual(expected, returned)

    def test_borrow_list_lower_total(self):
        expected = [[['Lending', 20000, 4.1],
                     ['Lending', 1000, 4.9],
                     ['Lending', 1500, 4.9],
                     ['Lending', 1500, 4.9],
                     ['Lending', 500, 4.9],
                     ['Lending', 500, 5.15]],
                    [['Borrowing', 1000, 4.8],
                     ['Borrowing', 1000, 5.1],
                     ['Borrowing', 2500, 5.1],
                     ['Borrowing', 500, 5.1],
                     ['Borrowing', 10000, 6]]]
        returned = match_orders(['Borrowing', 500, 5.15], orders)
        self.assertEqual(expected, returned)

    def test_lending_list_lower_total(self):
        expected = [[['Lending', 20000, 4.1],
                    ['Lending', 1000, 4.9],
                    ['Lending', 1500, 4.9],
                    ['Lending', 1500, 4.9],
                    ['Lending', 500, 4.9],
                    ['Lending', 1000, 5.15]],
                    [['Borrowing', 500, 4.8],
                    ['Borrowing', 1000, 5.1],
                    ['Borrowing', 2500, 5.1],
                    ['Borrowing', 500, 5.1],
                    ['Borrowing', 10000, 6]]]
        returned = match_orders(['Lending', 500, 4.8], orders)
        self.assertEqual(expected, returned)
