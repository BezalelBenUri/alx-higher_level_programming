#!usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.

    Args:
        a_dictionary: The dictionary.

    Returns:
        A key with the biggest integer value. If no score found, return None.

    """

    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    max_score = float('-inf')
    best_key = None

    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            best_key = key

    return best_key
