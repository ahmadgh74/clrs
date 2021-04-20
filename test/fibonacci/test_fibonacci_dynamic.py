import unittest

from src.fibonacci import fibonacci_loop


class TestFibonacciLoop(unittest.TestCase):

    def test_fibo_0(self):
        data = 0
        expected = 0
        self.assertEqual(fibonacci_loop(data), expected)

    def test_fibo_1(self):
        data = 10
        expected = 55
        self.assertEqual(fibonacci_loop(data), expected)

    def test_fibo_2(self):
        data = 11
        expected = 89
        self.assertEqual(fibonacci_loop(data), expected)

    def test_fibo_3(self):
        data = 14
        expected = 377
        self.assertEqual(fibonacci_loop(data), expected)

    def test_fibo_4(self):
        data = 1
        expected = 1
        self.assertEqual(fibonacci_loop(data), expected)
