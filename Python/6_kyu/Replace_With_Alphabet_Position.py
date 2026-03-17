"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.

    alphabet_position("The sunset sets at twelve o' clock.") -> "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 ..."

"""

import string


def alphabet_position(text):
    alphabet = list(string.ascii_lowercase)
    text = list(text.lower())
    result = []
    for letter in text:
        if letter in alphabet:
            result.append(alphabet.index(letter) + 1)
    return " ".join(str(i) for i in result)
