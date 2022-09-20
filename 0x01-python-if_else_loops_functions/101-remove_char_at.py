#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to create a copy of the string, removing the character at
# the position n (not the Python way, the “C array index”)
# demonstrates how to use a function, and an if...elif condition to affect
# program output
#
# (C) 2022 Daniel Waweru, Nairobi, Kenya
# email danielwaweru9632@gmail.com
# -----------------------------------------------------------
def remove_char_at(str, n):
    """Removes the char at an index in a given string
    Args:
        str: string argument
        n: index argument
    Returns:
        str: edited string
    """

    # If the index is a positive integer
    if n >= 0:

        # Use slicing to ommit the character at index n
        str = str[:n] + str[n + 1:]

    # Return editied string
    return str
