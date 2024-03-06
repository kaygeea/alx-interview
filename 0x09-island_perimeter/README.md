# 0x09. Island Perimeter

### This directory contains a Python script that creates a funtion that calculates the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers.

# APPROACH
The function `island_perimeter(grid)` calculates the perimeter of an island within a 2D grid. The grid is represented by a list of lists of integers, where 0 represents water and 1 represents land. The function iterates through each cell of the grid and counts the perimeter based on the neighboring cells.

## STEP 1 - Iterate over each cell in the grid
The function uses nested loops to iterate and reach both layers of the grid.

## STEP 2 - Identify the sorroundings for each cell in the grid
For each land cell:
- Check if the top neighbor is water or out of bounds.
- Check if the bottom neighbor is water or out of bounds.
- Check if the left neighbor is water or out of bounds.
- Check if the right neighbor is water or out of bounds.

## STEP 3 - Increment the perimeter count for each water or out of bounds neighbour
For each water or neighbour the perimeter count is incremented.
