#!/usr/bin/python3
'''
check each round
'''


def isWinner(x, nums):
    '''
    check winner
    '''
    def rec(n):
        '''
        play for each round
        '''
        if n == 1:
            return 2
        if n == 2:
            return 1
        count = 0
        for num in range(3, n + 1):
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                count += 1
        if count % 2:
            return 2
        return 1
    if x == 0 or len(nums) < 1 or len(nums) != x:
        return None
    maria = 0
    ben = 0
    for round in nums:
        result = rec(round)
        if result == 1:
            maria += 1
        else:
            ben += 1
    if maria == ben:
        return None
    if maria > ben:
        return "Maria"
    return "Ben"
