#!/usr/bin/env python3
import sys
import tempfile
import pyperclip
from random import randint
from random import seed

seed(777)  # Seed random number generator

temp_pairs = []  # Temporary list holding kv_pairs

temp = tempfile.TemporaryFile(mode="w+t")  # Create Temporary file.


def gen_pair(num_keys, k_start, k_end, v_start, v_end):
    """
    Takes in 5 inputs:
        num_keys: int
            #Number of pairs to generate
        k_start: int
            #Start range for key
        k_end: int
            #End range for key
        v_start: int
            #Start range for value
        v_end: int
            #End range for value
    Returns String of generated key/value pair and newline.
    """

    for _ in range(num_keys):
        key = randint(k_start, k_end)
        value = randint(v_start, v_end)
        temp_pairs.append(f"({key},{value})")


def write_temp():
    """
    Returns writes of generated key/value pair and newline.
    """
    first_line = "kv_pairs = (\n"
    last_line = "\n)"
    temp.writelines(first_line)
    for pair in temp_pairs:
        if pair == temp_pairs[-1]:
            temp.writelines(f"{pair}")
        else:
            temp.writelines(f"{pair},\n")

    temp.writelines(last_line)


if __name__ == "__main__":
    print("Thank you for using the Key Value Generator!\n")
    if sys.argv[1] == "default":
        num_of_keys = int(10)
        key_start = int(0)
        key_end = int(100)
        val_start = int(0)
        val_end = int(100)
        print(
            f"Using default values:\
            \n   Number of pairs is {num_of_keys}\
            \n   Key range is {key_start} to {key_end}\
            \n   Value range is {val_start} to {val_end}\n"
        )
    elif len(sys.argv) < 5:
        num_of_keys = int(
            input("Enter integer value for number of pairs\n(Default 10):\n~>")
        )
        key_start = int(
            input("\nEnter integer value for key start range\n(Default 0):\n~>")
        )
        key_end = int(
            input("\nEnter integer value for key end range\n(Default 100):\n~>")
        )
        val_start = int(
            input("\nEnter integer value for value start range\n(Default 0):\n~>")
        )
        val_end = int(
            input("\nEnter integer value for value end range\n(Default 100):\n~>")
        )
    else:
        num_of_keys = int(sys.argv[1])
        key_start = int(sys.argv[2])
        key_end = int(sys.argv[3])
        val_start = int(sys.argv[4])
        val_end = int(sys.argv[5])

try:
    gen_pair(num_of_keys, key_start, key_end, val_start, val_end)
    write_temp()
finally:
    temp.seek(0)
    pyperclip.copy(temp.read())
    temp.close()
    print("Copied key/value pairs to clipboard!")
