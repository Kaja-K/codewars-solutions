"""
The goal of this exercise is to convert a string to a new string where each character in the new string 
is "(" if that character appears only once in the original string, or ")" if that character appears more 
than once in the original string. Ignore capitalization when determining if a character is a duplicate.

    "din"      =>  "((("
    "recede"   =>  "()()()"
    "Success"  =>  ")())())"
    "(( @"     =>  "))((" 

"""


def duplicate_encode(text):
    text = text.lower()
    alph = {}
    for letter in text:
        if letter not in alph:
            alph[letter] = 1
        else:
            alph[letter] += 1
    result = ""
    for letter in text:
        if alph[letter] > 1:
            result = result + ")"
        else:
            result = result + "("
    return result
