import unittest
from src.my_functions import calculate_square  # 假设函数定义在 my_functions.py 中

class TestCalculateSquare(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(calculate_square(2), 4)
        self.assertEqual(calculate_square(5), 25)
        self.assertEqual(calculate_square(10), 100)

    def test_negative_number(self):
        self.assertEqual(calculate_square(-3), 9)
        self.assertEqual(calculate_square(-5), 25)
        self.assertEqual(calculate_square(-7), 49)

    def test_zero(self):
        self.assertEqual(calculate_square(0), 0)

if __name__ == '__main__':
    unittest.main()
