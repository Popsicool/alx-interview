#!/usr/bin/python3
'''
island parameter
'''
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    '''
    island parameter
    '''
    per = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
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
