"""
You need to create a fibonacci function that given a signature array/list, returns the first n 
elements - signature included of the so seeded sequence. Signature will always contain 3 numbers; 
n will always be a non-negative number; if n == 0, then return an empty array

"""


def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= len(signature):
        return signature[:n]
    trib = signature[:]
    while len(trib) < n:
        next_num = sum(trib[-3:])
        trib.append(next_num)
    return trib
