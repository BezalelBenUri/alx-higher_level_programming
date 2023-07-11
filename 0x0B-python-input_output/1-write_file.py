#!/usr/bin/python3
"""Defines a text file line-counting function."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.

    """
    num_characters = 0
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters = file.write(text)
    return num_characters

