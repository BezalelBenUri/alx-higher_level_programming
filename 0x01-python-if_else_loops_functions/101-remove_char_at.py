#!/usr/bin/python3
def remove_char_at(str, pos):
    """Create a copy of the string without the character at position n."""
    if pos < 0:
        return (str)
    return (str[:pos] + str[pos+1:])
