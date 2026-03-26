"""
Encrypt this!

You want to create secret messages which can be deciphered by the 
Decipher this! kata. Here are the conditions:

    Your message is a string containing space separated words.
    You need to encrypt each word in the message using the following rules:
        The first letter must be converted to its ASCII code.
        The second letter must be switched with the last letter
    Keepin' it simple: There are no special characters in the input.

Examples:
    encrypt_this("Hello") == "72olle"
    encrypt_this("good") == "103doo"
    encrypt_this("hello world") == "104olle 119drlo"""

def encrypt_this(text):
    if not text:
        return ""    
    result = []
    for word in text.split():
        encrypted = str(ord(word[0]))   
        if len(word) == 1:
            result.append(encrypted)
        elif len(word) == 2:
            result.append(encrypted + word[1])
        else:
            middle = word[-1] + word[2:-1] + word[1]
            result.append(encrypted + middle)
    return " ".join(result)