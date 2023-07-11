#!/usr/bin/python3

"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object created from the JSON file.

    """
    with open(filename, "r") as f:
        return json.load(f)
