#!/usr/bin/python3
'''
Minimum Operations
'''


def minOperations(n: int) -> int:
    '''
    Minimum Operations
    '''
    current = 1
    copy = 0
    count = 0
    while (current < n):
        if copy == 0:
            copy = current
            count += 1
        if current == 1:
            current += copy
            count += 1
            continue
        rem = n - current
        if rem < copy:
            return 0
        if rem % current == 0:
            copy = current
            current += copy
            count += 2
        else:
            current += copy
            count += 1
    if current != n:
        return 0
    return count
