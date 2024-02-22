#!/usr/bin/python3
"""Defines JSON file-reading func"""
import json


def load_from_json_file(filename):
    """Create Python object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
