'''
Making our own summation function
'''
import operator
import functools 

def our_sum(nums):
    return functools.reduce(operator.add, nums, 0)

print(our_sum([1, 2, 3]))