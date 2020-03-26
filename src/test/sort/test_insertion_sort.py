import unittest
from src.sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_insertion_sort(self):
        data = [4, 2, 5, 6, 1, 7, 3]
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(insertion_sort(data), expected)

