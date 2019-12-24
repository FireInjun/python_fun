#!/usr/bin/env python3
import shutil
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


def clear_pycache():
    """
    Delete the *__pycache__* folders, if present
    """
    CD(SRC_DIR)
    for folder in LS():
        CD(folder)
        print(PWD())
        shutil.rmtree("__pycache__", ignore_errors=True)
        UP()


clear_pycache()
