#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)  # Remove the key from the dictionary if it exists
    return a_dictionary
