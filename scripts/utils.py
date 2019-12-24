#!/usr/bin/env python3
import os
import * from script_constants


def check_if_repo():
    """
    Check if currently in *correct* repo.
    """
    if REPO_NAME not in PWD:
        print("NOT IN REPO")
        return False
    else:
        print("IN REPO")
        return True


def check_if_root():
    """
    Check if currently in *root* directory of repo.
    """
    if PWD().endswith(REPO_NAME):
        print("ROOT DIR")
        return True
    else:
        print("NOT ROOT DIR")
        return False


def go_to_root():
    """
    Change directory to the *root* directory of the repo.
    """
    CD(ROOT_DIR)
