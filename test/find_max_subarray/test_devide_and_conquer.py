import unittest

from src.find_max_subarray import find_max_subarray


class TestFindMaxSubarrayDAQ(unittest.TestCase):

    def test_find_max_1(self):
        data = [3, 4, -2, 3, -10, 32, 4, -11, 7, -3, 2]
        expected = (5, 6, 36)

        self.assertEqual(find_max_subarray(data), expected)

    def test_find_max_2(self):
        data = [-11, -9, 2, 2, -12, 9, 1, -14, 40, 1, -8, -6, -17, -16, -5]
        expected = (8, 9, 41)

        self.assertEqual(find_max_subarray(data), expected)

    def test_find_max_3(self):
        data = [-10, -14, -5, 4, 16, -10, 4, 20, -15, 4, -1, 5, -9, 12, 6, -9, -12]
        expected = (3, 14, 36)

        self.assertEqual(find_max_subarray(data), expected)
