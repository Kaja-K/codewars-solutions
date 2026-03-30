"""Reverse every other word in a given string, then return the string. 
Throw away any leading or trailing whitespace, while ensuring there is 
exactly one space between each word. Punctuation marks should be treated 
as if they are a part of the word in this kata."""

import re
def reverse_alternate(st):
    st = re.sub(r' +', ' ', st).strip().split(" ")
    result = " ".join([word[::-1] if i % 2 != 0 else word for i, word in enumerate(st)])
    return result