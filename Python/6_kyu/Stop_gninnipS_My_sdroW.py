"""
Write a function that takes in a string of one or more words, and returns the same string, but 
with all five or more letter words reversed  (Just like the name of this Kata). 
Strings passed in will consist of only letters  and spaces. Spaces will be included only when more 
than one word is present.

    spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
    spinWords( "This is a test") => returns "This is a test" 

"""


def spin_words(s):
    s = s.split(" ")
    for i, word in enumerate(s):
        if len(word) >= 5:
            s[i] = word[::-1]
    return " ".join(s)
