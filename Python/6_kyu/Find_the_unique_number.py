"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

    find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

"""


def find_uniq(arr):
    if arr[0] != arr[1] and arr[0] != arr[2]:
        return arr[0]
    unique = arr[0]
    for number in arr:
        if unique != number:
            unique = number
            return unique
