"""
Complete the method which returns the number which is most frequent 
in the given input array. If there is a tie for most frequent number, 
return the largest number among them. Note: no empty arrays will be given.
Examples

    [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
    [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
    [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

"""
def highest_rank(arr):
    unique = list(set(arr))
    result = [(arr.count(number))for number in unique]
    return max([unique[i] for i in range(len(unique)) if result[i] == max(result)])