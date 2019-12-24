#!/usr/bin/env python3

import os


def up_one():
    """
    Move up a single directory.
    """
    print("Moving up one directory.")
    os.chdir("..")


# Commands simplified as shell names
PWD = os.getcwd
CD = os.chdir
LS = os.listdir
UP = up_one
# Names
REPO_NAME = "python_fun"
# Locations
ROOT_DIR = PWD().split(REPO_NAME).pop(0) + REPO_NAME
SRC_DIR = ROOT_DIR + "/src"
