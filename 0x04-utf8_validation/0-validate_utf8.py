#!/usr/bin/python3

"""
UTF-8 Validation
Solution to:
Write a method that determines if a given data set
represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data,
therefore you only need to handle the 8 least significant bits
of each integer
"""


def validUTF8(data):
    def get_num_bytes(byte):
        """Count the number of leading 1s in the byte
        to determine the number of bytes used in the UTF-8 encoding.
        """
        if byte & 0b10000000 == 0:
            return 1
        elif byte & 0b11100000 == 0b11000000:
            return 2
        elif byte & 0b11110000 == 0b11100000:
            return 3
        elif byte & 0b11111000 == 0b11110000:
            return 4
        return 0

    i = 0
    while i < len(data):
        num_bytes = get_num_bytes(data[i])
        if num_bytes == 0:
            return False

        # Check that the next num_bytes - 1 bytes are continuation bytes.
        for j in range(i + 1, i + num_bytes):
            if j >= len(data) or data[j] & 0b11000000 != 0b10000000:
                return False

        i += num_bytes

    return True
