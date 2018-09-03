""" 
Write a function that will return the following:
Examples:
accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

"""
def accum(text):
    output_str = ""
    for index,letter in enumerate(text):
        first_character = y.upper()
        rest_character = y.lower() * x
        if index != (len(text) - 1):
            delim = "-"
        else:
            delim = ""
        output_str = output_str + first_character + rest_character + delim
    return output_st
"""

def accum(text):
    return '-'.join(letter.upper() + letter.lower() * index for index, letter in enumerate(text))


test_cases = ["ZpglnRxqenU", "NyffsGeyylB", "MjtkuBovqrU", "EvidjUnokmM", "HbideVbxncC", "phtcjsgbpzs"]
for case in test_cases:
    print(accum(case))
