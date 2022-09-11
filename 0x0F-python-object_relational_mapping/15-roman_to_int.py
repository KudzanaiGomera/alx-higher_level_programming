#!/usr/bin/python3
"""
contains the function roman_to_int
"""


def roman_to_int(roman_string):
    """converts a Roman number to an integer"""
    if type(roman_string) is not str or roman_string is None:
        return 0
    conversion = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    max_val = 0
    total = 0
    for roman_numeral in roman_string[::-1]:
        decimal = conversion[roman_numeral]
        if decimal >= max_val:
            max_val = decimal
            total += decimal
        else:
            total -= decimal
    return total
