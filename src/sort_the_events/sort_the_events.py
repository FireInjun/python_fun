#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getEventsOrder' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING team1
#  2. STRING team2
#  3. STRING_ARRAY events1
#  4. STRING_ARRAY events2
#
# G,Y,R
# player-name time event-name
# S
# player-name time event-name second-player-name
#


# EXPECTED SORTED ORDER:

def getEventsOrder(team1, team2, events1, events2):
    """
    Returns a LIST sorted like so:
    *  team-name,  time,  G,Y,R,S
    * in case of same event/time, sort A-Z by team then player
    """

    def prepend_team(List, team):
        """ Helper function to add team to each element in events array. """
        team += "{0}"
        List = map(team.format, List)
        return List

    prepend_team(events1, team1)
    prepend_team(events2, team2)

    def parse_events_list(event_List):
        """Takes in arrays and outputs tuples."""

    rx_dict = {
        "player": re.compile("^\w+\s+[a-z]+")
        "type": re.compile("[G|Y|R|S]"),
        "plus_sign": re.compile("\++"),
        "reg_time": re.compile("[0-9]{2}"),
        "stop_time": re.compile("(?<=\+)([0-9]+)")}

    list_of_keys = ["team", "player", "type", "time", "stop_time", "player2"]


if __name__ == "__main__":
