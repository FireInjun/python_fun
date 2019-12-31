#!/usr/bin/env python3

import unittest
from sort_the_events import getEventsOrder

"""
# INPUT:
# 1st line is string, name of team1
# 2nd line is string, name of team2
# 3rd line is integer n1, number of elements in events1
# 4th-n1 lines are strings for describing events1
# n1+1th line is integer n2, number of elements in events2
# n1+2-n2 lines are strings for describing events2
"""
line1 = "abc"
line2 = "cba"
line3 = 2
events1 = ["mo sa 45+2 Y", "a 13 G"]
line5 = 2
events2 = ["d 23 S f", "z 46 G"]


class Sort_the_eventsTestCase(unittest.TestCase):
    """Tests for sort_the_events.py."""

    def test_getEventsOrder(self):
        """Is nothing going to happen?"""
        self.assertTrue(getEventsOrder(5))


if __name__ == "__main__":
    unittest.main()
