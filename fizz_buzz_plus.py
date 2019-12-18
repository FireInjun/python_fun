#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())


def case(x):
    switcher = {
        'odd': 'Weird',  # If n is odd, print Weird
        'even_2_5': 'Not Weird',  # If n is even and in the inclusive range of 2 to 5, print Not Weird
        'even_6_20': 'Weird',  # If n is even and in the inclusive range of 6 to 20, print Weird
        'even_gt_20': 'Not Weird'  # If n is even and greater than 20, print Not Weird
    }
    return switcher.get(x, "Invalid case")


def __main__(n):
    if n % 2 != 0:
        print(case('odd'))
    elif n % 2 == 0 and n in range(2, 5):
        print(case('even_2_5'))
    elif n % 2 == 0 and n in range(6, 21):
        print(case('even_6_20'))
    elif n % 2 == 0 and n > 20:
        print(case('even_gt_20'))


__main__(n)