"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by 
rearranging its digits.

    12 ==> 21
    513 ==> 531
    2017 ==> 2071

"""


def next_bigger(n):
    s = str(n)
    if n < 12 or len(s) == s.count(s[0]):
        return -1
    n_copy = n
    arr = list(str(n))
    n = len(arr)
    k = n - 2
    while k >= 0:
        if arr[k] < arr[k + 1]:
            break
        k -= 1
    if k < 0:
        arr = arr[::-1]
    else:
        for l in range(n - 1, k, -1):
            if arr[l] > arr[k]:
                break
        arr[l], arr[k] = arr[k], arr[l]
        arr[k + 1 :] = reversed(arr[k + 1 :])
    if int("".join(arr)) < n_copy:
        return -1
    return int("".join(arr))
