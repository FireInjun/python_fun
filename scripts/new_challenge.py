#!/usr/bin/env sh
import os
import constants

challenge = str(input())
file_name = f"{challenge}.py"
test_file_name = f"test_{challenge}.py"
dir_path = f"{constants.SRC_DIR}/{challenge}"


def create_challenge():
    os.mkdir(dir_path)
    constants.CD(dir_path)
    file = open(file_name, "+w")
    test = open(test_file_name, "+w")
    init = open("__init__.py", "+w")


create_challenge()
