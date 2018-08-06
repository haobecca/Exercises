"""
Very simple, given a number, find its opposite.
Examples:
1: -1
14: -14
-34: 34
"""

def opposite(number):
    return number * -1

test_cases = [1, 14, -34]
for n in test_cases:
    print(opposite(n))