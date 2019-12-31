#!/bin/python3
import sys


def solution(n):
    if n % 2 != 0 or (n % 2 == 0 and 5 < n <= 20):
        print("Weird")
        return "Weird"
    elif n % 2 == 0 and (2 <= n <= 5 or n > 20):
        print("Not Weird")
        return "Not Weird"


if __name__ == "__main__":
    if len(sys.argv[1]) < 2:
        n = int(input("Number? ").strip())
else:
    n = int(sys.argv[1].strip())

    solution(n)
