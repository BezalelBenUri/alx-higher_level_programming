#!/usr/bin/
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer.
    Args:
        roman_string: A string representing a Roman numeral.
    Returns:
        The integer value of the Roman numeral.
    Raises:
        ValueError: If the roman_string is not a valid Roman numeral.
    """

    if not isinstance(roman_string, str):
        return 0

    roman_numerals = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
    }

    value = 0
    for i in range(len(roman_string)):
        if roman_numerals[roman_string[i]] < roman_numerals[roman_string[i + 1]]:
            value -= roman_numerals[roman_string[i]]
        else:
            value += roman_numerals[roman_string[i]]
    return value
