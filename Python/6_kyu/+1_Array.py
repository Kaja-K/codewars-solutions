"""
Given an array of integers of any length, return an array that has 
1 added to the value represented by the array.

If the array is invalid (empty, or contains negative integers or integers 
with more than 1 digit), return nil (or your language's equivalent).
Examples

Valid arrays

    [4, 3, 2, 5] would return [4, 3, 2, 6] (4325 + 1 = 4326)
    [1, 2, 3, 9] would return [1, 2, 4, 0] (1239 + 1 = 1240)
    [9, 9, 9, 9] would return [1, 0, 0, 0, 0] (9999 + 1 = 10000)
    [0, 1, 3, 7] would return [0, 1, 3, 8] (0137 + 1 = 0138)

Invalid arrays

    [] is invalid because it is empty
    [1, -9] is invalid because -9 is not a non-negative integer
    [1, 2, 33] is invalid because 33 is not a single-digit integer

"""
def up_array(arr):
    if not arr:
        return None 
    result = ""
    for number in arr:
        if number < 0 or number > 9:
            return None
        result += str(number) 
    new_result = list(str(int(result) + 1))
    leading_zeros = 0
    for x in arr:
        if x == 0:
            leading_zeros += 1
        else:
            break
    if len(new_result) == len(arr) - leading_zeros:
        for i in range(leading_zeros):
            new_result.insert(i, '0')
    return [int(i) for i in new_result]