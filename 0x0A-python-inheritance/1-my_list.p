#!/usr/bin/python3

"""
Defines a subclass MyList that inherits from list.
"""


class MyList(list):
    """
    Subclass of list with additional method print_sorted().
    """

    def print_sorted(self):
        """
        Print the list in sorted order (ascending sort).
        """
        sorted_list = sorted(self)
        print(sorted_list)
