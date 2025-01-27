import unittest
from remainder import get_remainder
"""
def get_remainder(dividend, divisor):
    
    Функция для вычисления остатка от деления двух чисел.
   
    if divisor == 0:
        raise ValueError("Делитель не может быть равен нулю")
    return dividend % divisor
"""


class TestGetRemainder(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(get_remainder(10, 3), 1)
        self.assertEqual(get_remainder(20, 5), 0)
        self.assertEqual(get_remainder(7, 2), 1)

    def test_negative_numbers(self):
        self.assertEqual(get_remainder(-10, 3), -1)
        self.assertEqual(get_remainder(-20, 5), 0)
        self.assertEqual(get_remainder(-7, 2), -1)

    def test_zero_dividend(self):
        self.assertEqual(get_remainder(0, 3), 0)
        self.assertEqual(get_remainder(0, -3), 0)

    def test_zero_divisor(self):
        with self.assertRaises(ValueError):
            get_remainder(10, 0)
        with self.assertRaises(ValueError):
            get_remainder(-10, 0)

    def test_divisor_greater_than_dividend(self):
        self.assertEqual(get_remainder(3, 10), 3)
        self.assertEqual(get_remainder(-3, 10), -3)

if __name__ == '__main__':
    unittest.main()