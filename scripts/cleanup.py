#!/usr/bin/env python3
import * from utils


def find_pycache():
    """
    Find the *__pycache__* folders
    """
    CD(SRC_DIR)
    for folder in LS():
        CD(folder)
        LS()
        UP()
    pass
