def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.

    Args:
        a_dictionary: The dictionary.

    Returns:
        A key with the biggest integer value. If no score found, return None.

    """

  # Get the maximum value in the dictionary.
    max_value = max(a_dictionary.values())

  # Get the key of the maximum value.
    best_key = None
    for key, value in a_dictionary.items():
        if value == max_value:
        best_key = key
        break

    return best_key
