#!/usr/bin/python3

def print_last_digit(ns):
    """Print the last digit of a number and return it."""
    print(abs(ns) % 10, end="")
    return (abs(ns) % 10)
