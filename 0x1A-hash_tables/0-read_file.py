#!/usr/bin/python3
"""Defines text file_reading func"""


def read_file(filename=""):
    """Print contents of a UTF8 text file to standard output"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
