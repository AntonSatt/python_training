import unittest
from list_operations import find_max, remove_duplicates, flatten_list


class TestListOperations(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max([1, 5, 3, 9, 2]), 9)
        self.assertEqual(find_max([-5, -10, -3]), -3)
        
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 3]), [1, 2, 3])
        self.assertEqual(remove_duplicates(['a', 'b', 'a', 'c']), ['a', 'b', 'c'])
        
    def test_flatten_list(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])
        self.assertEqual(flatten_list([[1], [2], [3]]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
