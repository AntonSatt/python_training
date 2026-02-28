import unittest
from calculator import calculate_total


class TestCalculator(unittest.TestCase):
    def test_calculate_total(self):
        result = calculate_total("25.00", "8")
        self.assertEqual(result, "Total: $27.00")
        
    def test_calculate_total_with_different_values(self):
        result = calculate_total("100.00", "10")
        self.assertEqual(result, "Total: $110.00")


if __name__ == "__main__":
    unittest.main()
