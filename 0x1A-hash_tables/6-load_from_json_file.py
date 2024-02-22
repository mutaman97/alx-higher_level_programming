#!/usr/bin/python3
"""Defines JSON file_reading func"""
import json


def load_from_json_file(filename):
    """Create Python object from JSON filee"""
    with open(filename) as f:
        return json.load(f)
