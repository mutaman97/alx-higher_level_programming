#!/usr/bin/python3
"""Define text file-reading func"""


def read_file(filename=""):
    """Print the contents of UTF8 text file to stdandard output"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
