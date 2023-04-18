#!/usr/bin/python3
'''
Pascal triangle
'''


def pascal_triangle(n):
    '''
    Pascal triangle
    '''
    main = [[1]]
    if n < 1:
        return []
    i = 1
    while (i < n):
        if (i == 1):
            new = [1, 1]
        else:
            last = main[-1].copy()
            new = [1]
            j = 0
            while j < (len(last) - 1):
                new.append(last[j] + last[j + 1])
                j += 1
            new.append(1)
        i += 1
        main.append(new)
    return main
