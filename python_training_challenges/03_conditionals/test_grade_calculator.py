import unittest
from grade_calculator import get_letter_grade


class TestGradeCalculator(unittest.TestCase):
    def test_grade_a(self):
        self.assertEqual(get_letter_grade(95), "A")
        self.assertEqual(get_letter_grade(90), "A")
        
    def test_grade_b(self):
        self.assertEqual(get_letter_grade(85), "B")
        self.assertEqual(get_letter_grade(80), "B")
        
    def test_grade_c(self):
        self.assertEqual(get_letter_grade(75), "C")
        self.assertEqual(get_letter_grade(70), "C")
        
    def test_grade_d(self):
        self.assertEqual(get_letter_grade(65), "D")
        self.assertEqual(get_letter_grade(60), "D")
        
    def test_grade_f(self):
        self.assertEqual(get_letter_grade(55), "F")
        self.assertEqual(get_letter_grade(0), "F")


if __name__ == "__main__":
    unittest.main()
