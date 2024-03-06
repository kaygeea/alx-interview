# 0x08. Making Change

### This directory contains a Python script that implements a solution to the coin change problem using dynamic programming. The coin change problem involves determining the fewest number of coins needed to meet a given amount total using a pile of coins of different values.

# APPROACH
### The function `makeChange(coins: List[int], total: int)` uses a greedy algorithm implemented with dynamic programming to efficiently determine the fewest number of coins needed to meet a given amount total using a pile of coins of different values.

- STEP 1 - Initialization:
1. First, the function initializes a dynamic programming table (dp) to store the fewest number of coins needed for each total amount from 0 to the given total.
2. The base case is set where 0 coins are needed to make a total of 0.

- STEP 2 - Selection of Coins and Updating `dp` Table:
1. The function iterates through each coin value in the provided list of coin denominations.
2. For each coin value, it iterates through each possible total amount from the coin value to the given total.
3. It updates the fewest number of coins needed to make each total by taking the minimum of its current value and the value obtained by adding one coin of value coin to the fewest number of coins needed to make the total i - coin.

- STEP 3 - Checking for Validitiy and Return:
1. After selecting coins and updating the dp table, the function checks if the fewest number of coins needed for the given total (dp[total]) is still infinity.
2. If dp[total] is infinity, it means that the total cannot be met by any combination of coins in the given list. In this case, the function returns -1.
3. Otherwise, the function returns the fewest number of coins needed for the given total.
