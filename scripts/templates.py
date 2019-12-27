import constants
import re

pattern = re.compile(constants.REGEX_NAME)

# Raw input
challenge_input = str(input("What is the name of the challenge? \n"))

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

# Challenge file template.
challenge_tuple = (
    "#!/usr/bin/env python3",
    "\n\n\ndef first_function(something):\n",
    f"{constants.TAB}{constants.TRIP_Q} Does nothing with input of 'something'. {constants.TRIP_Q}",
    f"\n{constants.TAB}pass\n\n\n",
    f"def second_function(something):\n",
    f"{constants.TAB}{constants.TRIP_Q}Also does nothing with input of 'something'.{constants.TRIP_Q}",
    f"\n{constants.TAB}pass\n",
)

# Test file template.
test_tuple = (
    "#!/usr/bin/env python3",
    f"\nimport unittest\nfrom {challenge} import first_function\n\n\n",
    f"class {challenge_title}TestCase(unittest.TestCase):\n",
    f"{constants.TAB}{constants.TRIP_Q}Tests for {file_name}.{constants.TRIP_Q}\n\n",
    f"{constants.TAB}def test_first_function(self):\n",
    f"{constants.TAB}{constants.TAB}{constants.TRIP_Q}Is nothing going to happen?{constants.TRIP_Q}\n",
    f"{constants.TAB}{constants.TAB}self.assertTrue(first_function(5))\n",
    f"\n\nif __name__ == '__main__':\n{constants.TAB}unittest.main()\n",
)
