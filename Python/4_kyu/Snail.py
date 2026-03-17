"""
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

    array = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    snail(array) #=> [1,2,3,6,9,8,7,4,5]

"""


def snail(snail):
    result = []
    while len(snail) > 0:
        result += snail[0]
        del snail[0]
        if len(snail) > 0:
            for i in snail:
                result += [i[-1]]
                del i[-1]
            if snail[-1]:
                result += snail[-1][::-1]
                del snail[-1]
            for i in reversed(snail):
                result += [i[0]]
                del i[0]
    return result
