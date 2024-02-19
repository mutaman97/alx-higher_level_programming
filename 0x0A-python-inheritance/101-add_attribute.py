#!/usr/bin/python3
"""Defines function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """Add new attribute to an object if possible.

    Args:
        obj (any): The object to add attribute to.
        att (str): name of the attribute to add to object.
        value (any): value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can not add new attribute")
    setattr(obj, att, value)
