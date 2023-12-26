#!/usr/bin/python3
"""Provide functionality to determine the winner of a prime number game
   session with a specified number of rounds
"""


def isWinner(x: int, nums: list) -> str:
    """
    Determine the winner of a prime number game session with a specified
    number of rounds and a set of numeric limits.
    Args:
        a. x (int): Incoming arg for num of rounds for a game session.
        b. nums (list): Incoming arg for an array of `n
    Returns:
        str: Name of the player that won the most rounds or None if the winner
             cannot be determined
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0

    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
