"""
Create a function that takes a list of integers  and a group length as parameters. 
Your task is to determine if it's possible to split all the  numbers from the list into groups 
of the  specified length, while ensuring that consecutive numbers are present within each group.

    consecutive_nums([5, 6, 3, 4], 2) ➞ True
    # Two groups of length 2: [3, 4], [5, 6]

    consecutive_nums([1, 3, 4, 5], 2) ➞ False
    # It is possible to make one group of length 2, but not a second one.

"""

from collections import Counter


def consecutive_nums(lst, size):
    c = Counter(lst)
    if len(lst) % size:
        return False
    for v in sorted(c)[: -size + 1 or None]:
        if not c[v]:
            continue
        n = c[v]
        for x in range(v, v + size):
            if c[x] < n:
                return False
            c[x] -= n
    return not sum(c.values())
