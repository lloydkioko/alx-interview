#!/usr/bin/python3
"""
Making Change Interview Question
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, returns
    the fewest number of coins needed to meet a given amount total
    """
    if total < 1:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total // coin != 0 and total != 0:
            count = count + total // coin
            total = total % coin

    if total != 0:
        return -1
    return count
