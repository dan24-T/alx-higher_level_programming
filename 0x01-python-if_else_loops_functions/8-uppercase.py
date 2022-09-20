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
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
    print("{:s}".format(i), end="")
    print()
