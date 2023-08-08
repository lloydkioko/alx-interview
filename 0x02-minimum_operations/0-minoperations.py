#!/usr/bin/python3

"""
Contains function minOperations(n)
"""


def minOperations(n: int) -> int:
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters
    """
    if n <= 1:
        return 0

    operations = 0
    current_chars = 1
    clipboard = 0

    while current_chars < n:
        if n % current_chars == 0:
            clipboard = current_chars
            operations += 1

        current_chars += clipboard
        operations += 1

    return operations
