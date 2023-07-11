def class_to_json(obj):
    """
    Returns the dictionary description with a
    simple data structure for JSON serialization of an object.

    Args:
        obj: The object to be serialized.

    Returns:
        dict: The dictionary representation of the object.

    """
    attributes = obj.__dict__
    if hasattr(obj, "__dict__"):
        attributes = obj.__dict__.copy()

    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            continue
        attributes[key] = str(value)

    return attributes
