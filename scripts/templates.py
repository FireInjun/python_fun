import constants
import re
import sys

if len(sys.argv) < 2:
    challenge_input = str(input("What is the name of the challenge? \n"))
else:
    challenge_input = str(sys.argv[1].strip())

pattern = re.compile(constants.REGEX_NAME)

"""
** Clean up input with this **
Using regex, remove all non-alphanumeric chars,
Strip leading and trailing white space
Make lowercase
Replace " " spaces with "_"
"""
challenge = pattern.sub("", challenge_input).lower().strip().replace(" ", "_")
challenge_title = challenge.capitalize()

# Useful string variables for dictionary templates.
file_name = f"{challenge}.py"
test_file_name = f"test_{challenge}.py"
dir_path = f"{constants.SRC_DIR}/{challenge}"
pybang = "\u0023!/usr/bin/env python3\n"

# Challenge file template.
challenge_file = f"{pybang}import sys\n\n\ndef first_function(something):\n\
{constants.TAB}{constants.TRIP_Q} Does nothing with input of 'something'.\
{constants.TRIP_Q}\n{constants.TAB}pass\n\n\ndef second_function(something):\n\
{constants.TAB}{constants.TRIP_Q}Also does nothing with input of 'something'.\
{constants.TRIP_Q}\n{constants.TAB}pass\n\n\nif __name__ == \"__main__\":\
\n{constants.TAB}if len(sys.argv[1]) < 2:\n{constants.TAB}{constants.TAB}\
something = int(input(\"Number?\").strip())\n{constants.TAB}else:\n\
{constants.TAB}{constants.TAB}something = int(sys.argv[1].strip())\n"

# Test file template.
test_file = f"{pybang}\nimport unittest\nfrom {challenge} import first_function\n\n\n\
class {challenge_title}TestCase(unittest.TestCase):\n\
{constants.TAB}{constants.TRIP_Q}Tests for {file_name}.{constants.TRIP_Q}\n\n\
{constants.TAB}def test_first_function(self):\n\
{constants.TAB}{constants.TAB}{constants.TRIP_Q}Is nothing going to happen?\
{constants.TRIP_Q}\n{constants.TAB}{constants.TAB}self.assertTrue(first_function(5))\n\
\n\nif __name__ == '__main__':\n{constants.TAB}unittest.main()\n"
