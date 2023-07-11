#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and returns the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.

    """
    num_characters_added = 0
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_added = file.write(text)
    return num_characters_added
