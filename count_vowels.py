"""
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, and u as vowels for this Kata.
The input string will only consist of lower case letters and/or spaces.
"""
'''
def getCount(inputStr):
    num_vowels = 0
    for character in inputStr:
        if character in ['a', 'e', 'i', 'o', 'u']:
            num_vowels = num_vowels + 1
    return num_vowels
'''
def getCount(inputStr):
    return len([character for character in inputStr if character in 'aeiou'])


test_cases = ["abracadabra", "aeiou", "I love you"]

for case in test_cases:
    print(getCount(case))