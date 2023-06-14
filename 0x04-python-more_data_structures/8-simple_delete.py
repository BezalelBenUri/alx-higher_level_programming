def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
        a_dictionary: The dictionary.
    key: The key to delete.

    """

  # Check if the key exists in the dictionary.
    if key in a_dictionary:
    # If the key exists, delete it from the dictionary.
        del a_dictionary[key]

    return a_dictionary
