#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.
    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        A set of common elements in two sets.
    """
    common_elements = set_1 & set_2
    return common_elements
