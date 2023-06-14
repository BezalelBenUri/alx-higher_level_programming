#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    Args:
        a_dictionary: The dictionary.
    key: The key.
        value: The value.
    """
    a_dictionary[key] = value  # Add or update the key-value pair in the dictionary
    return a_dictionary
