import unittest
from src.sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_insertion_sort(self):
        data = [4, 2, 5, 6, 1, 7, 3, 15, 12, 9, 8, 20, 16]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 16, 20]
        self.assertEqual(insertion_sort(data), expected)

    def test_insertion_sort_2(self):
        data = [51, 91, 98, 78, 15, 30, 41, 7, 98, 63, 58, 61, 91, 56, 86, 98, 45, 84, 1, 9]
        expected = [1, 7, 9, 15, 30, 41, 45, 51, 56, 58, 61, 63, 78, 84, 86, 91, 91, 98, 98, 98]

        self.assertEqual(expected, insertion_sort(data))

    def test_insertion_sort_3(self):
        data = [25, 42, 40, 24, 1, 49, 14, 13, 28, 24, 32, 46, 0, 50, 10]
        expected = [0, 1, 10, 13, 14, 24, 24, 25, 28, 32, 40, 42, 46, 49, 50]

        self.assertEqual(expected, insertion_sort(data))
