#!/usr/bin/python3
"""Implement an algorithm to determine lowest threshold of coins needed
   to meet a given amount
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Determine the fewest number of coins needed to meet a given
       amount total from a given pile of coins of different values.

    Args:
        a. coins: Incoming arg for a list of the vals for the coins in hand.
        b. total: Incoming arg for the target figure to be met.

    Returns:
        The fewest number of coins needed to meet the given total, as an int.
        0 if total is 0; or -1 if total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
