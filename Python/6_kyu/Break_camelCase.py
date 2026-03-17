"""
Complete the solution so that the function will break up camel casing, using a space between words.

    "camelCasing"  =>  "camel Casing"
    "identifier"   =>  "identifier"
    ""             =>  ""
    
"""


def solution(s):
    new_s = ""
    for letter in s:
        if letter.isupper():
            new_s += " " + letter
        else:
            new_s += letter
    return new_s
