#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print a string in uppercase
# demonstrates how to use a function and if condition to affect program output
#
# (C) 2022 Daniel Waweru, Nairobi, Kenya
# email danielwaweru9632@gmail.com
# -----------------------------------------------------------

def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
