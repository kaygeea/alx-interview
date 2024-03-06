#!/usr/bin/python3
"""Create a function that computes the perimeter of a given island"""


def island_perimeter(grid: list[list[int]]) -> int:
    """
    Calculate the perimeter of the island in a 2D grid.

    Arg(s):
        grid(List[List[int]]): A list of lists of integers representing
                               the grid. 0 reps water, 1 reps land.

    Returns:
        The perimeter of the island as an int.
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    # Loop through the grid
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check all four neighbors
                if row - 1 < 0 or grid[row - 1][col] == 0:
                    perimeter += 1  # Top neighbor is water
                if row + 1 >= rows or grid[row + 1][col] == 0:
                    perimeter += 1  # Bottom neighbor is water
                if col - 1 < 0 or grid[row][col - 1] == 0:
                    perimeter += 1  # Left neighbor is water
                if col + 1 >= cols or grid[row][col + 1] == 0:
                    perimeter += 1  # Right neighbor is water
    return perimeter
