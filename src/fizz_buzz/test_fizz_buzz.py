#!/usr/bin/env python3

import unittest
import unittest.mock
from fizz_buzz import fizzBuzz


class FizzbuzzTestCase(unittest.TestCase):
    """Tests for fizzbuzz.py."""

    def test_number(self):
        """Testing for numbers that will return an integer."""
        self.assertEqual(fizzBuzz(821), 821)
        self.assertEqual(fizzBuzz(782), 782)
        self.assertEqual(fizzBuzz(137), 137)
        self.assertEqual(fizzBuzz(64), 64)
        self.assertEqual(fizzBuzz(779), 779)

    def test_zero(self):
        """Testing for zero, should return an integer."""
        self.assertEqual(fizzBuzz(0), 0)

    def test_fizz(self):
        """Testing for numbers divisible by 3 cleanly, should return 'Fizz'."""
        self.assertEqual(fizzBuzz(582), "Fizz")
        self.assertEqual(fizzBuzz(867), "Fizz")
        self.assertEqual(fizzBuzz(261), "Fizz")
        self.assertEqual(fizzBuzz(507), "Fizz")
        self.assertEqual(fizzBuzz(333), "Fizz")

    def test_buzz(self):
        """Testing for numbers divisible by 5 cleanly, should return 'Buzz'."""
        self.assertEqual(fizzBuzz(460), "Buzz")
        self.assertEqual(fizzBuzz(5), "Buzz")
        self.assertEqual(fizzBuzz(50), "Buzz")
        self.assertEqual(fizzBuzz(55), "Buzz")
        self.assertEqual(fizzBuzz(95), "Buzz")

    def test_fizzbuzz(self):
        """Testing for numbers divisible by 3 and 5 cleanly, should return 'FizzBuzz'."""
        self.assertEqual(fizzBuzz(15), "FizzBuzz")
        self.assertEqual(fizzBuzz(75), "FizzBuzz")
        self.assertEqual(fizzBuzz(120), "FizzBuzz")
        self.assertEqual(fizzBuzz(555), "FizzBuzz")
        self.assertEqual(fizzBuzz(45), "FizzBuzz")

    def test_print_list(self):
        """Testing to verify the print_list variable works correctly."""
        self.assertIs


if __name__ == "__main__":
    unittest.main(verbosity=3)
