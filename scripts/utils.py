#!/usr/bin/env python3
import constants


def check_if_repo():
    """
    Check if currently in *correct* repo.
    """
    if constants.REPO_NAME not in constants.PWD:
        print("NOT IN REPO")
        return False
    else:
        print("IN REPO")
        return True


def check_if_root():
    """
    Check if currently in *root* directory of repo.
    """
    if constants.PWD().endswith(constants.REPO_NAME):
        print("ROOT DIR")
        return True
    else:
        print("NOT ROOT DIR")
        return False


def go_to_root():
    """
    Change directory to the *root* directory of the repo.
    """
    constants.CD(constants.ROOT_DIR)
