import unittest
from main import add, subtract, multiply, divide, remainder

class TestMath(unittest.TestCase):
   def test_add(self):
       self.assertEqual(add(2, 5),7)
       self.assertNotEqual(add(3, 7), 9)

   def test_subtract(self):
       self.assertEqual(subtract(7, 4), 3)
       self.assertNotEqual(subtract(4, 2), 1)

   def test_multiply(self):
       self.assertNotEqual(multiply(2, 5), 12)
       self.assertEqual(multiply(3, 6), 18)

   def test_divide(self):
       self.assertNotEqual(divide(4, 2), 3)
       self.assertEqual(divide(20, 5), 4)


# Тесты для функции remainder
class TestRemainderFunction(unittest.TestCase):

    # Тест на корректное вычисление остатка
    def test_remainder_positive_numbers(self):
        self.assertEqual(remainder(10, 3), 1)  # 10 % 3 = 1
        self.assertEqual(remainder(20, 7), 6)  # 20 % 7 = 6

    # Тест на отрицательные числа
    def test_remainder_negative_numbers(self):
        self.assertEqual(remainder(-10, 3), 2)  # -10 % 3 = 2
        self.assertEqual(remainder(10, -3), -2) # 10 % -3 = -2

    # Тест на ноль в качестве делимого
    def test_remainder_zero_dividend(self):
        self.assertEqual(remainder(0, 5), 0)  # 0 % 5 = 0

    # Тест на деление на ноль (должно вызывать исключение)
    def test_remainder_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            remainder(10, 0)
        self.assertEqual(str(context.exception), "Делитель не может быть равен нулю")

    # Тест на некорректные типы данных (должно вызывать исключение)
    def test_remainder_invalid_input(self):
        with self.assertRaises(TypeError):
            remainder("10", 3)  # Передача строки вместо числа



if __name__ == '__main__':
    unittest.main(verbosity=2)


