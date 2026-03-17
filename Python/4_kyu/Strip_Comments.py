"""
Complete the solution so that it strips all text that  follows any of a set of comment markers passed in. 
Any whitespace at the end of the line should also be stripped out. 

    Given an input string of:
        apples, pears # and bananas
        grapes
        bananas !apples

    The output expected would be:
        apples, pears
        grapes
        bananas

"""


def strip_comments(strng, markers):
    s = strng.split("\n")
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] in markers:
                s[i] = s[i][:j].rstrip()
                break
    return "\n".join(s)
