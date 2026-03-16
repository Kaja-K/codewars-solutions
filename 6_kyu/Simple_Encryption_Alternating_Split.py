"""
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all 
the odd-indexed characters of S with all the even-indexed characters of S, this process should be 
repeated N times.

    encrypt("012345", 1)  =>  "135024"
    encrypt("012345", 2)  =>  "135024"  ->  "304152"
    encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

Together with the encryption function, you should also implement a decryption function which reverses the process.
If the string S is an empty value or the integer N is not positive, return the first argument without changes.

"""


def decrypt(text, n):
    if not text or n <= 0:
        return text
    for _ in range(n):
        mid = len(text) // 2
        odd  = text[:mid]
        even = text[mid:]
        result = [''] * len(text)
        result[1::2] = odd
        result[0::2] = even
        text = ''.join(result)
    return text

def encrypt(text, n):
    if not text or n <= 0:
        return text
    for _ in range(n):
        text = text[1::2] + text[0::2]
    return text