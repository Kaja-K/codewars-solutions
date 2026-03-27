"""
Step 1: Create a function called encode() to replace all the lowercase 
vowels in a given string with numbers according to the following pattern:

    a -> 1
    e -> 2
    i -> 3
    o -> 4
    u -> 5

For example, encode("hello") would return "h2ll4". 
There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back 
into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into 
the function will correspond to vowels."""

vowels = "aeiou"
def encode(st):
    return "".join(str(vowels.index(c.lower()) + 1) if c.lower() in vowels else c for c in st)
    
def decode(st):
        return "".join(vowels[int(c) - 1] if c.isdigit() else c for c in st)