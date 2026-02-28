import unittest
from word_counter import count_words


class TestWordCounter(unittest.TestCase):
    def test_count_words(self):
        result = count_words("the quick brown fox")
        self.assertEqual(result['the'], 1)
        self.assertEqual(result['quick'], 1)
        
    def test_count_words_case_insensitive(self):
        result = count_words("The the THE")
        self.assertEqual(result['the'], 3)
        
    def test_count_words_with_duplicates(self):
        result = count_words("hello hello world")
        self.assertEqual(result['hello'], 2)
        self.assertEqual(result['world'], 1)


if __name__ == "__main__":
    unittest.main()
