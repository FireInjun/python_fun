#!/usr/bin/env sh
import os
import constants
import utils
import templates


def build_boilerplate():
    """
    Function makes and changes into directory
    before making challenge, test and init files.
    """
    constants.CD(constants.ROOT_DIR)
    os.mkdir(templates.dir_path)
    constants.CD(templates.dir_path)
    utils.write_file(templates.file_name, templates.challenge_file)
    utils.write_file(templates.test_file_name, templates.test_file)
    init = open("__init__.py", "x")
    init.close()


def create_challenge():
    """ Main function for creating new challenges safely when called."""
    if templates.challenge not in constants.SRC_DIR:
        try:
            build_boilerplate()
        except FileExistsError:
            print(f"{templates.challenge_title} already exists!")


create_challenge()
