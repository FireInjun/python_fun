#!/usr/bin/env python3
import sys


def first_function(something):
    """ Does nothing with input of 'something'."""
    pass


def second_function(something):
    """Also does nothing with input of 'something'."""
    pass


if __name__ == "__main__":
    if len(sys.argv[1]) < 2:
        something = int(input("Number?").strip())
    else:
        something = int(sys.argv[1].strip())
