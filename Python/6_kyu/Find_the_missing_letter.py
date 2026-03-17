"""
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing 
letter in the array. You will always get an valid array. And it will be always exactly one letter be missing. 

    ['a','b','c','d','f'] -> 'e'

"""
import string


def find_missing_letter(chars):
    alphabet_lst = []
    alphabet = list(string.ascii_letters)
    index = alphabet.index(chars[0])
    for i in range(index, index + len(chars) + 1):
        alphabet_lst.append(alphabet[i])
    return "".join(set(alphabet_lst) - set(chars))
