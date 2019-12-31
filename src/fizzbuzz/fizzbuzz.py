#!/bin/python3

import sys


def fizzBuzz(n):
    """
    Returns 'Fizz', 'Buzz', 'FizzBuzz', or an integer, depending on input.
    """
    print_list = []
    five = (0, 5)
    three = (3, 6, 9)
    N_list = list(map(int, list(str(n))))

    for i in five:
        if N_list[-1] == i:
            print_list.append("Fizz")

    for i in three:
        if sum(N_list) == i:
            print_list.append("Buzz")

    if len(print_list) == 0:
        print(int("".join(map(str, N_list))))

    solution = "".join(map(str, print_list))
    print(solution)
    return solution


if __name__ == "__main__":
    if len(sys.argv[1]) < 2:
        n = int(input().strip())
    else:
        n = int(sys.argv[1].strip())
    fizzBuzz(n)
