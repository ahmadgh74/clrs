import unittest

from src.sort import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_merge(self):
        data = [4, 2, 5, 6, 1, 7, 3, 15, 12, 9, 8, 20, 16]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 16, 20]

        self.assertEqual(expected, merge_sort(data))
