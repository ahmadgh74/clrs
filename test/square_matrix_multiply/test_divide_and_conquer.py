import unittest
import numpy as np

from src.square_matrix_multiply import square_matrix_multiply


class TestStrassenMultiply(unittest.TestCase):

    def test_square_1(self):
        matrix_a = np.array([[1, 3],
                             [7, 5]])
        matrix_b = np.array([[6, 8],
                             [4, 2]])

        expected = np.array([[18, 14],
                             [62, 66]])

        self.assertTrue(bool((square_matrix_multiply(matrix_a, matrix_b) == expected).all()))
