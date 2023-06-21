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
                if not grid[i - 1][j]:
                    per += 1
                if not grid[i][j + 1]:
                    per += 1
                if not grid[i + 1][j]:
                    per += 1
                if not grid[i][j - 1]:
                    per += 1
    return per
