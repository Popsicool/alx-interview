'''
Lockboxes open module
'''


def canUnlockAll(boxes):
    '''
    function to check f all boxes can be opened
    Args:
        boxes: An array of arrays
    '''
    num = len(boxes)
    res = {}
    for x in range(num):
        res[x] = False
    res[0] = True
    for x in range(2):
        for x in range(num):
            if res[x]:
                for y in range(len(boxes[x])):
                    res[boxes[x][y]] = True
    if False in res.values():
        return False
    return True
