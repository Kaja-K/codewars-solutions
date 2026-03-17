"""
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second 
character of the final pair with an underscore ('_').


    * 'abc' =>  ['ab', 'c_']
    * 'abcdef' => ['ab', 'cd', 'ef']

"""

def solution(s):
    result = []
    x =-1 if len(s)%2!=0 else 0
    for i in range(0,len(s)+x,2):
        result.append(s[i]+s[i+1])  
    if x == -1:
        result.append(s[-1]+"_")
    return result

def solution(s):
    if s == "":
        return []
    if len(s) % 2 != 0:
        s += "_"
    return [s[i : i + 2] for i in range(0, len(s), 2)]
