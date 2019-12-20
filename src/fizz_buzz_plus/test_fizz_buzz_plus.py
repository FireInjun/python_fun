import unittest
from fizz_buzz_plus import solution


class TestIfElse(unittest.TestCase):
    def test_odd_number(self):
        """
        The function returns 'Weird' when provided with a number that is odd
        """
        self.assertEqual(solution(3), "Weird")


if __name__ == '__main__':
    unittest.main()