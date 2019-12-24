#!/usr/bin/env python3
import shutil
import constants


def clear_pycache():
    """
    Delete the *__pycache__* folders, if present
    """
    constants.CD(constants.SRC_DIR)
    for folder in constants.LS():
        constants.CD(folder)
        print(constants.PWD())
        shutil.rmtree("__pycache__", ignore_errors=True)
        constants.UP()


clear_pycache()
