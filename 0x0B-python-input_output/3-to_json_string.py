#!/usr/bin/python3
"""Defines string to JSON func"""
import json


def to_json_string(my_obj):
    """Return JSON representation of string object"""
    return json.dumps(my_obj)
