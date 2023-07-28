#!/usr/bin/python3
"""
Pascal's Triangle Implementation
"""


def factorial(n):
    """Returns the factorial of an integer"""
    if (n == 0):
        return (1)

    return n * factorial(n - 1)


def pascal_triangle(n):
    """
    Returns a list of lists of coefficients from 0 up to the passed integer
    """
    pascal_list = []
    if (n <= 0):
        return pascal_list

    for i in range(n):
        row = []
        for x in range(i + 1):
            num = factorial(i)
            denom = factorial(x) * factorial(i - x)
            row.append(num // denom)

        pascal_list.append(row)

    return(pascal_list)
