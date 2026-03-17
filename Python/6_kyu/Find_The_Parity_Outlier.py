"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.

    [2, 4, 0, 100, 4, 11, 2602, 36]
    Should return: 11 (the only odd number)

    [160, 3, 1719, 19, 11, 13, -21]
    Should return: 160 (the only even number)

"""


def find_outlier(integers):
    odd_count = 0
    odd = 0
    even_count = 0
    even = 0
    for integer in integers:
        if integer % 2 == 1:
            odd_count += 1
            odd = integer
        else:
            even_count += 1
            even = integer
    if odd_count > even_count:
        return even
    return odd
