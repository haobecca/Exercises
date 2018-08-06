'''
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
'''
'''
def persistence(number):
    persistence = 0
    while number > 9:
        product = 1
        for digit in str(number):
            product = product * int(digit)
        number = product
        persistence = persistence + 1
    return persistence
'''
import operator
import functools 

def persistence(number):
    persistence = 0
    while number > 9:
       number = functools.reduce(operator.mul, [int(digit) for digit in str(number)], 1)
       persistence += 1
    return persistence 

test_cases = [39, 4, 25, 999]

for case in test_cases:
    print(persistence(case))
