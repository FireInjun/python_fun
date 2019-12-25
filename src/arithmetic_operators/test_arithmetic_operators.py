import unittest
from arithmetic_operators import sum_int
from arithmetic_operators import diff_int
from arithmetic_operators import prod_int


class ArithmeticTestCase(unittest.TestCase):
    """
    Tests for `arithmetic_operator.py`
    """

    def test_sum(self):
        """
        Is 2 and 5 combined equal to 7?
        """
        self.assertEqual(sum_int(2, 5), 7)

    def test_diff(self):
        """
        Does 7 takeaway 2 equal 5?
        """
        self.assertEqual(diff_int(7, 2), 5)

    def test_prod(self):
        """
        Does 2 times 7 equal 14?
        """
        self.assertEqual(prod_int(2, 7), 14)


if __name__ == "__main__":
    unittest.main()
