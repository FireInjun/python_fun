#!/usr/bin/env python3
import sys


if __name__ == "__main__":
    if len(sys.argv[1]) < 2:
        something = int(input("Number?").strip())
    else:
        something = int(sys.argv[1].strip())
