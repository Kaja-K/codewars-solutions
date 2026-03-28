"""

Given an integer, return a string with dash '-' marks before and after 
each odd digit, but do not begin or end the string with a dash mark.

Ex:

274 -> '2-7-4'
6815 -> '68-1-5'
"""
def dashatize(n):
    digits=str(abs(n))
    result=[]
    for digit in digits:
        if int(digit)%2 != 0:
            result.append('-')
            result.append(digit)
            result.append('-')
        else:
            result.append(digit)
    return ''.join(result).strip('-').replace("--","-")