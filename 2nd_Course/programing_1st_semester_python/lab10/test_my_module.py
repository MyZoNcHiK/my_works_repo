import unittest
from my_module import average, maximum, minimum, even_numbers

class TestLab8(unittest.TestCase):

    def test_average_positive(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3.0)

    def test_average_negative_and_zero(self):
        self.assertEqual(average([-10, 0, 10]), 0.0)

    def test_average_empty(self):
        self.assertEqual(average([]), 0)

    def test_maximum_standard(self):
        self.assertEqual(maximum([1, 5, 3, 9, 2]), 9)

    def test_maximum_negative(self):
        self.assertEqual(maximum([-5, -1, -10]), -1)

    def test_maximum_empty_exception(self):
        with self.assertRaises(ValueError):
            maximum([])

    def test_minimum_standard(self):
        self.assertEqual(minimum([4, 2, 8, 1]), 1)

    def test_minimum_negative(self):
        self.assertEqual(minimum([-5, -1, -10]), -10)

    def test_minimum_empty_exception(self):
        with self.assertRaises(ValueError):
            minimum([])

    def test_even_numbers_mixed(self):
        self.assertEqual(even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_even_numbers_only_odd(self):
        self.assertFalse(even_numbers([1, 3, 5]))

    def test_even_numbers_only_odd(self):
        self.assertEqual(even_numbers([1, 3, 5]), [])

    def test_even_numbers_empty(self):
        self.assertEqual(even_numbers([]), [])


if __name__ == '__main__':
    unittest.main()

