#!/bin/python3


def solution(n):
    if n % 2 != 0 or (n % 2 == 0 and 5 < n <= 20):
        print("Weird")
    elif n % 2 == 0 and (2 <= n <= 5 or n > 20):
        print("Not Weird")


if __name__ == '__main__':
    n = int(input("Number? ").strip())
    solution(n)
