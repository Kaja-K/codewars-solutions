"""
You are going to be given an array of integers. Your job is to take that array and find an index N where the 
sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index 
that would make this happen, return -1.

    You are given the array {1,100,50,-51,1,1}: Your function will return the index 1, because at the 1st position 
    of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) 
    both equal 1.

"""


def find_even_index(arr):
    for i, j in enumerate(arr):
        if sum(arr[i + 1 :]) == sum(arr[:i]):
            return i
    return -1
