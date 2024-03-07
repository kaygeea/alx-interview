#!/usr/bin/python3
"""
Create a function to determine winner of a prime game
"""

def isWinner(x: int, nums: list[str]) -> str:
    """
    Determines the winner of a game played by Maria and Ben based on strategic
    removal of prime numbers and their multiples across multiple rounds.

  Args:
    x (int): The number of rounds in the game (int).
    nums: An array of consecutive integers representing the starting set for
    each round (List[int]).

  Returns:
    "Maria": If Maria wins the majority of rounds.
    "Ben": If Ben wins the majority of rounds.
    None: If the winner cannot be determined (equal number of wins).
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
