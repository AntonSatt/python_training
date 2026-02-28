import unittest
from sum_numbers import sum_list


class TestSumNumbers(unittest.TestCase):
    def test_sum_positive_numbers(self):
        self.assertEqual(sum_list([1, 2, 3, 4, 5]), 15)
        
    def test_sum_with_negative(self):
        self.assertEqual(sum_list([1, -1, 2, -2]), 0)
        
    def test_sum_empty_list(self):
        self.assertEqual(sum_list([]), 0)
        
    def test_sum_single_number(self):
        self.assertEqual(sum_list([42]), 42)


if __name__ == "__main__":
    unittest.main()
