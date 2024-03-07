# 0x0A. Prime Game

### This directory contains a python script that creates a function which leverages understanding of prime numbers, game theory and algorithm optimization to solve a competitive game scenario.

# APPROACH
The function `isWinner(x: int, nums: list[int])` determines the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers. In the function `x` is the number of rounds (assumed to always be < 10,000) for the game session and `nums` is an array of `n` (also assumed to be < 10,000).

## STEP 1 - Input Validaion
- Ensure that the number of rounds x is at least 1 and the list of upper limits nums is not empty. If either condition is not met, return None to indicate that the winner cannot be determined.

## STEP 2 - Generate Primes
- Determine the maximum upper limit n from the list nums.
- Generate a list primes of boolean values representing whether each number from 1 to n is prime.
- Use the Sieve of Eratosthenes algorithm to mark non-prime numbers and their multiples in the primes list.

## STEP 3 -  Calculate Wins
- Iterate through each round, represented by the values in the nums list.
- For each round, count the number of primes less than the round's upper limit n.
- Update the wins count for Maria and Ben based on whether the count of primes is odd or even.

# STEP 4 - Determine Winner
- Compare the wins count for Maria and Ben.
- If the wins count is equal, return None to indicate that the winner cannot be determined.
- Otherwise, return the name of the player with the higher wins count as the winner of the game session.
