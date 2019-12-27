#!/usr/bin/env python3

import os
import utils
import re

# Commands simplified as shell names
PWD = os.getcwd
CD = os.chdir
LS = os.listdir
UP = utils.up_one
# Names
REPO_NAME = "python_fun"
# Locations
ROOT_DIR = PWD().split(REPO_NAME).pop(0) + REPO_NAME
SRC_DIR = f"{ROOT_DIR}/src"
SCRIPT_DIR = f"{ROOT_DIR}/scripts"
# Regex pattern
REGEX_NAME = "[^a-zA-Z.\d\s]"

pattern = re.compile(REGEX_NAME)

challenge_input = str(input("What is the name of the challenge? \n"))
challenge = pattern.sub("", challenge_input).lower().strip().replace(" ", "_")
challenge_title = challenge.capitalize()

# Useful string variables for dictionary templates.
file_name = f"{challenge}.py"
test_file_name = f"test_{challenge}.py"
dir_path = f"{SRC_DIR}/{challenge}"
tab = "    "
trip_quo = '"""'

# Challenge file template.
challenge_dict = {
    "shebang": "#!/usr/bin/env python3",
    "first_func": "\n\n\ndef first_function(something):\n",
    "first_docstring": f"{tab}{trip_quo} Does nothing with input of 'something'. {trip_quo}",
    "first_pass": f"\n{tab}pass\n\n\n",
    "second_func": f"def second_function(something):\n",
    "second_docstring": f"{tab}{trip_quo}Also does nothing with input of 'something'.{trip_quo}",
    "second_pass": f"\n{tab}pass\n",
}

# Test file template.
test_dict = {
    "shebang": "#!/usr/bin/env python3",
    "imports": f"\nimport unittest\nfrom {challenge} import first_function\n\n\n",
    "class": f"class {challenge_title}TestCase(unittest.TestCase):\n",
    "class_docstring": f"{tab}{trip_quo}Tests for {file_name}.{trip_quo}\n\n",
    "test": f"{tab}def test_first_function(self):\n",
    "test_docstring": f"{tab}{tab}{trip_quo}Is nothing going to happen?{trip_quo}\n",
    "assert": f"{tab}{tab}self.assertTrue(first_function(5))\n",
    "execute": f"\n\nif __name__ == '__main__':\n{tab}unittest.main()",
}
