#!/usr/bin/env sh
import os
import constants
import utils


def build_boilerplate():
    """Function makes and changes into directory before making challenge, test and init files."""
    os.mkdir(constants.dir_path)
    constants.CD(constants.dir_path)
    utils.write_file(constants.file_name, constants.challenge_dict)
    utils.write_file(constants.test_file_name, constants.test_dict)
    init = open("__init__.py", "x")
    init.close()


def create_challenge():
    """ Main function for creating new challenges safely when called."""
    if constants.challenge not in constants.SRC_DIR:
        try:
            build_boilerplate()
        except FileExistsError:
            print(f"{constants.challenge_title} already exists!")


create_challenge()
