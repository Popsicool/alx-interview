#!/usr/bin/python3
'''
Two dimentional array matrix rotation
'''


def rotate_2d_matrix(matrix):
    '''
    Rotating a two dimentional array
    '''
    n = len(matrix[0])
    duplicate = []
    for i in range(n):
        new_array = []
        for j in range(n):
            new_array.append(matrix[i][j])
        duplicate.append(new_array)
    for i in range(n):
        pos = n - 1
        for j in range(n):
            matrix[i][j] = duplicate[pos][i]
            pos -= 1
