#!/usr/bin/python3
'''
island parameter
'''
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    '''
    island parameter
    '''
    H = len(grid)
    W = len(grid[0])

    def depthFirst(r: int, c: int) -> int:
        if r < 0 or r >= H or c < 0 or c >= W or grid[r][c] == 0:
            return 1
        if grid[r][c] == 1:
            grid[r][c] = 2
            return depthFirst(r-1, c) + depthFirst(r+1, c) + depthFirst(
                r, c+1) + depthFirst(r, c-1)
    perimeter = 0
    for row in range(H):
        for col in range(W):
            if grid[row][col] == 1:
                perimeter += depthFirst(row, col)
    return perimeter



'''

island parameter

from typing import List


def island_perimeter(grid: List[List[int]]) -> int:

    island parameter

    per = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                if not grid[i - 1][j]:
                    per += 1
                if not grid[i][j + 1]:
                    per += 1
                if not grid[i + 1][j]:
                    per += 1
                if not grid[i][j - 1]:
                    per += 1
    return per

'''