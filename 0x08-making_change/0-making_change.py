#!/usr/bin/python3
'''
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given total total.
'''
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    '''
    give the fewest number of coin
    Args:
        coin: list of coins
        total: integer value for total
    Return:
        int value
    '''
    if total == 0:
        return 0
    if min(coins) > total:
        return -1
    tmp = [-1 for i in range(0, total + 1)]
    for i in coins:
        if i > len(tmp) - 1:
            continue
        tmp[i] = 1
        for j in range(i + 1, total + 1):
            if tmp[j - i] == -1:
                continue
            elif tmp[j] == -1:
                tmp[j] = tmp[j - i] + 1
            else:
                tmp[j] = min(tmp[j], tmp[j - i] + 1)
    return tmp[total]
