"""
Write Number in Expanded Form

You will be given a number and you will need to 
return it as a string in Expanded Form. For example:

   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"

NOTE: All numbers will be whole numbers greater than 0.
"""

def expanded_form(num):
    result=" "
    num = str(num)
    for i, number in enumerate(num):
        if number != "0":
            result += (num[i]) + "0"*(len(num)-i-1) +  " " + "+" + " "
    return result[1:-3:]