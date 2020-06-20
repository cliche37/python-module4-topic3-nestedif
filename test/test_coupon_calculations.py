import unittest
from store.coupon_calculations import calculate_price


class FunctionUnitTestCase(unittest.TestCase):

    def test_price_under_ten(self):
        self.assertEqual(calculate_price(9.99, 5, 10), 10.71)
        self.assertEqual(calculate_price(5, 5, 15), 5.95)
        self.assertEqual(calculate_price(7.50, 5, 20), 8.07)
        self.assertEqual(calculate_price(8.79, 5, 10), 9.57)
        self.assertEqual(calculate_price(3.99, 3, 12), 6.87)
        self.assertEqual(calculate_price(4.99, 2, 11.99), 8.74)

    def test_price_between_ten_thirty(self):
        self.assertEqual(calculate_price(10, 5, 10), 10.72)
        self.assertEqual(calculate_price(25, 5, 25), 23.85)
        self.assertEqual(calculate_price(24.99, 5, 50), 16.54)
        self.assertEqual(calculate_price(29.99, 5, 15.99), 30.20)
        self.assertEqual(calculate_price(15.50, 5, 11), 15.86)
        self.assertEqual(calculate_price(21, 5, 100), 5.95)

    def test_price_between_thirty_fifty(self):
        self.assertEqual(calculate_price(35.00, 5, 10), 36.57)
        self.assertEqual(calculate_price(49.99, 0, 50), 34.44)
        self.assertEqual(calculate_price(33.99, 5, 10), 35.61)
        self.assertEqual(calculate_price(37.00, 10, 25), 29.41)
        self.assertEqual(calculate_price(39.99, 9.99, 9.99), 36.57)
        self.assertEqual(calculate_price(45.00, 5, 10), 50.11)

    def test_price_over_fifty(self):
        self.assertEqual(calculate_price(299.99, 0, 5), 302.09)
        self.assertEqual(calculate_price(99.99, 0.99, 50), 64.42)
        self.assertEqual(calculate_price(50.99, 50, 0), 7.00)
        self.assertEqual(calculate_price(499.00, 100, 5), 401.79)
        self.assertEqual(calculate_price(150.00, 25, 15), 112.62)
        self.assertEqual(calculate_price(800.00, 400, 50), 212)
