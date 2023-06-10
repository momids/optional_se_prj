import unittest

from newmain import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_large(self):
        self.assertEqual(factorial(10), 3628800)


if __name__ == "__main__":
    unittest.main()
