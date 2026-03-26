"""
Given a lowercase string that has alphabetic characters only and no spaces, 
return the highest value of consonant substrings. Consonants are any letters 
of the alphabet except "aeiou".

We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

For example, for the word "zodiac", let's cross out the vowels. We get: "z o d ia c"

"zodiac" -> 26

The consonant substrings are: "z", "d" and "c" with values 
"z" = 26, "d" = 4 and "c" = 3. The highest is 26.

"strength" -> 57

The consonant substrings are: "str" and "ngth" with values 
"str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. 
The highest is 57."""

import string 
def solve(s):
    max_val = 0
    current = 0
    for letter in s:
        if letter not in "aeiou":
            current += string.ascii_lowercase.index(letter) + 1 
        else:
            max_val = max(max_val, current)
            current = 0
    return max(max_val, current)