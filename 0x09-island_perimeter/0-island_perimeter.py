#!/usr/bin/python3
'''
island parameter
'''


def island_perimeter(grid):
    '''
    island parameter
    '''
    per = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                per += 4
                if i > 0 and grid[i - 1][j]:
                    per -= 1
                if j < len(grid[0]) - 1 and grid[i][j + 1]:
                    per -= 1
                if i < len(grid) - 1 and grid[i + 1][j]:
                    per -= 1
                if j > 0 and grid[i][j - 1]:
                    per -= 1
    return per
