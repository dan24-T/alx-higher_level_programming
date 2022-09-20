#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print the ASCII alphabet in lowercase
# demonstrates how to use a loop to affect program output
#
# (C) 2022 Daniel Waweru, Nairobi, Kenya
# email danielwaweru9632@gmail.com
# -----------------------------------------------------------

# For each ascii_code in range sequence
for ascii_code in range(97, 123):

    # Print out the character format of the ascii_code
    print("{:c}".format(ascii_code), end='')
