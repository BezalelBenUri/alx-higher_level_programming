#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    Args:
        my_list: The list of integers.

    Returns:
        The sum of all unique integers in the list.
    """

    unique_set = set(my_list)
    sum_unique = sum(unique_set)
    return sum_unique
