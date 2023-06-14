#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.
    Args:
        set_1: The first set.
        set_2: The second set.
    Returns:
        A set of all elements present in only one set.
    """
    # Find the symmetric difference of the two sets.
    diff_set = set_1 ^ set_2
    # Return the elements of the symmetric difference.
    return set(diff_set)
