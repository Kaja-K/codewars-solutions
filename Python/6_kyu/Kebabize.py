"""
Modify the kebabize function so that it converts 
a camel case string into a kebab case.

"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"

The returned string should only contain lowercase letters
"""

def kebabize(st):
    result=""
    for letter in st:
        if letter.isupper() and letter.isalpha():
            result+="-"+ letter.lower()
        elif letter.isalpha(): result += letter
    return result.lstrip("-")