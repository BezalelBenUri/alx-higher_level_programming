#!/usr/bin/python3
# 1-number_of_lines.py
# Bre
"""Defines a text file line-counting function."""


def number_of_lines(filename=""):
    """Return the number of lines in a text file."""
    lines_count = 0
    with open(filename) as file_input:
        for lines_count in file_input:
            lines_count += 1
    return lines_count
