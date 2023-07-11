#!/usr/bin/python3
""" function that returns the number of lines of a text file
"""


def number_of_lines(filename=""):
    """ function: number_of_lines
    """
    if filename == "" or type(filename) != str:
        return 0
    line_counter = 0
    with open(filename, "r") as file_input:
        for line in file_input:
            line_counter += 1
    return line_counter
