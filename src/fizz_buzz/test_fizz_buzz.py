#!/usr/bin/env python3

import unittest
import unittest.mock
from fizz_buzz import fizzBuzz

return_numbers = [
    [821],
    [782],
    [137],
    [64],
    [779],
    [582, "Fizz"],
    [867, "Fizz"],
    [261, "Fizz"],
    [507, "Fizz"],
    [333, "Fizz"],
    [460, "Buzz"],
    [5, "Buzz"],
    [50, "Buzz"],
    [55, "Buzz"],
    [95, "Buzz"],
    [15, "FizzBuzz"],
    [75, "FizzBuzz"],
    [120, "FizzBuzz"],
    [555, "FizzBuzz"],
    [45, "FizzBuzz"],
]


class FizzbuzzTestCase(unittest.TestCase):
    """Tests for fizzbuzz.py."""

    def test_number(self):
        """Testing for numbers that will return an integer."""
        res = fizzBuzz(return_numbers[0])
        num = return_numbers[0]
        self.assertEqual(res, num, "test_number Failure!")

    def test_zero(self):
        """Testing for zero, should return an integer."""
        pass

    def test_fizz(self):
        """Testing for numbers divisible by 3 cleanly, should return 'Fizz'."""
        pass

    def test_buzz(self):
        """Testing for numbers divisible by 5 cleanly, should return 'Buzz'."""
        pass

    def test_fizzbuzz(self):
        """Testing for numbers divisible by 3 and 5 cleanly, should return 'FizzBuzz'."""
        pass


if __name__ == "__main__":
    unittest.main(verbosity=3)
