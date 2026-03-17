"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched.

    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !

"""


def pig_it(text):
    pig_latin = []
    for word in list(text.split(" ")):
        if word.isalpha():
            new_word = word[1:] + word[0]
            pig_latin.append(new_word + "ay")
        else:
            pig_latin.append(word)
    return " ".join(pig_latin)
