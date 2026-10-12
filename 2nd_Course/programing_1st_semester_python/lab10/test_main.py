from main import generate_prosti
import unittest

class TestGenerator(unittest.TestCase):
    def test_correct_generation(self):
        self.assertEqual(generate_prosti(10), [2, 3, 5, 7])
    def test_small_numbers(self):
        self.assertEqual(generate_prosti(0), [])
        self.assertEqual(generate_prosti(1), [])
    def test_value(self):
        with self.assertRaises(ValueError):
            generate_prosti(-2)

if __name__ == "__main__":
    unittest.main()  
