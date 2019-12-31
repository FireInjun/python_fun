#!/bin/python3

import sys


def fizzBuzz(n):
    """FizzBuzz classic challenge"""
    print_list = ""
    if n > 1 and n % 3 == 0:
        print_list += "Fizz"
    if n > 1 and n % 5 == 0:
        print_list += "Buzz"
    if len(print_list) == 0 and n % 3 != 0 and n % 5 != 0 or n < 1:
        print(int(n))
        return int(n)

    print(print_list)
    return print_list


if __name__ == "__main__":
    if len(sys.argv) < 2:
        n = int(input("Please enter a number:\n").strip())
    else:
        n = int(sys.argv[1].strip())

    fizzBuzz(n)
