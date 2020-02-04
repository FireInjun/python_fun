#!/usr/bin/env python3

import os
import utils

# Commands simplified as shell names
PWD = os.getcwd
CD = os.chdir
LS = os.listdir
UP = utils.up_one
# Names
REPO_NAME = "python_fun"
# Locations
ROOT_DIR = PWD().split(REPO_NAME).pop(0) + f"{REPO_NAME}"
SRC_DIR = f"{ROOT_DIR}/src"
SCRIPT_DIR = f"{ROOT_DIR}/scripts"
# Regex pattern
REGEX_NAME = "[^a-zA-Z.\\d\\s]"
TRIP_Q = '"""'
TAB = "    "
