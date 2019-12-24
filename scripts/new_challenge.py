#!/usr/bin/env sh
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
SRC_DIR = f"{ROOT_DIR}/src"

challenge = str(input())
file_name = f"{challenge}.py"
test_file_name = f"test_{challenge}.py"
dir_path = f"{SRC_DIR}/{challenge}"


def create_challenge():
    os.mkdir(dir_path)
    CD(dir_path)
    file = open(file_name, "+w")
    test = open(test_file_name, "+w")
    init = open("__init__.py", "+w")


create_challenge()
