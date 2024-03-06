#!/usr/bin/python3
"""
This module creates a function that uses the greedy algorithm
to solve the coin change problem
"""
from typing import List, Union


def makeChange(coins: List[int], total: int) -> Union[int, None]:
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (List[int]): A list of the values of the coins in hand.
                       The value of a coin will always be an int that is > 0.
    total (int): The amount total to be met.

    Returns:
    Union[int, None]: The fewest number of coins needed to meet total; or
                      0 if total is 0 or less; or
                      -1 if total cannot be met by any num of coins at hand.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
