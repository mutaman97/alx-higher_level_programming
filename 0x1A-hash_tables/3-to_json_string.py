#!/usr/bin/python3
"""Defines string to JSON func"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of string obj"""
    return json.dumps(my_obj)
