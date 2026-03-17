"""
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.

    The score of abad is 8 (1 + 2 + 1 + 4).

"""

import string


def high(x):
    alphabet = list(string.ascii_lowercase)
    text = x.lower().split(" ")
    points = []
    for word in text:
        word_points = sum(alphabet.index(letter) + 1 for letter in word)
        points.append(word_points)
    max_points = max(points)
    index_of_max = points.index(max_points)
    return text[index_of_max]
