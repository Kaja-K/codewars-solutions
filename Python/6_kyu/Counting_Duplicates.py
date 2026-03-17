"""
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits 
that occur more than once in the input string. The input string can be assumed to contain only alphabets 
(both uppercase and lowercase) and numeric digits."abcde" -> 0 # no characters repeats more than once

    "aabbcde" -> 2 # 'a' and 'b'
    "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
    "indivisibility" -> 1 # 'i' occurs six times

"""


def duplicate_count(text):
    text = text.upper()
    alph = {}
    for letter in text:
        if letter not in alph:
            alph[letter] = 1
        else:
            alph[letter] += 1
    result = 0
    for key, value in alph.items():
        if value > 1:
            result += 1
    return result
