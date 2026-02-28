import unittest
from safe_calculator import safe_divide, safe_convert_to_int, safe_get_element


class TestSafeCalculator(unittest.TestCase):
    def test_safe_divide_normal(self):
        self.assertEqual(safe_divide(10, 2), 5)
        
    def test_safe_divide_by_zero(self):
        self.assertEqual(safe_divide(10, 0), "Cannot divide by zero")
        
    def test_safe_convert_to_int_valid(self):
        self.assertEqual(safe_convert_to_int("42"), 42)
        
    def test_safe_convert_to_int_invalid(self):
        self.assertEqual(safe_convert_to_int("abc"), "Invalid conversion")
        
    def test_safe_get_element_valid(self):
        self.assertEqual(safe_get_element([1, 2, 3], 1), 2)
        
    def test_safe_get_element_out_of_range(self):
        self.assertEqual(safe_get_element([1, 2, 3], 10), "Index out of range")


if __name__ == "__main__":
    unittest.main()
