import unittest
import os
from file_handler import read_file, write_file, count_lines


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_temp.txt'
        
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_write_and_read_file(self):
        write_file(self.test_file, "Hello World")
        content = read_file(self.test_file)
        self.assertEqual(content, "Hello World")
        
    def test_count_lines(self):
        write_file(self.test_file, "Line 1\nLine 2\nLine 3")
        self.assertEqual(count_lines(self.test_file), 3)


if __name__ == "__main__":
    unittest.main()
