import unittest
from string_utils import reverse_string, is_palindrome, count_vowels


class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama".replace(" ", "").lower()))
        self.assertFalse(is_palindrome("hello"))
        
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("xyz"), 0)


if __name__ == "__main__":
    unittest.main()
