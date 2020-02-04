#!/usr/bin/env python3

import unittest
from postal_code_regex import first_function


class Postal_code_regexTestCase(unittest.TestCase):
    """Tests for postal_code_regex.py."""

    def test_first_function(self):
        """Is nothing going to happen?"""
        self.assertTrue(first_function(5))


if __name__ == '__main__':
    unittest.main()
