""""
The maximum sum subarray problem consists in finding the maximum sum of 
a contiguous subsequence in an array or list of integers:

For example:
    Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6 (Sum of [4, -1, 2, 1])

Easy case is when the list is made up of only positive numbers and the 
maximum sum is the sum of the whole array. If the list is made up of only 
negative numbers, return 0 instead. Your solution should be fast, it will 
be tested on very large arrays so slow solutions will time out.

Empty list is considered to have zero greatest sum. Note that the empty 
list or array is also a valid sublist/subarray.
"""

def max_sequence(arr):
    if  all(number <= 0 for number in arr):
        return 0
    elif  all(number > 0 for number in arr):
        return sum(arr)
    
    n=len(arr)
    result_left=max_sequence(arr[:n//2])
    result_right=max_sequence(arr[n//2:])
    r_suma = 0
    r_max = 0
    l_suma = 0
    l_max = 0
    
    for number in arr[n//2:]:
        r_suma += number
        r_max=max(r_max,r_suma)
    
    for number in reversed(arr[:n//2]):
        l_suma += number
        l_max=max(l_max,l_suma)
        
    return max(result_left, result_right, l_max + r_max)
 
 
from itertools import accumulate

def max_sequence(arr):
    if  all(number <= 0 for number in arr):
        return 0
    elif  all(number > 0 for number in arr):
        return sum(arr)
    
    n=len(arr)
    r_max = max(accumulate(arr[n//2:]))
    l_max = max(accumulate(reversed(arr[:n//2])))
        
    return max(max_sequence(arr[:n//2]), max_sequence(arr[n//2:]), l_max + r_max)
