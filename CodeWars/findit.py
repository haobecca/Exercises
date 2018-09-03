"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

"""
def find_it(seq):
    for n in seq:
        if seq.count(n) % 2 != 0:
            return n


computationally expensive
"""

"""
def find_it(seq):
    count_list = []
    for n in seq:
        if n not in count_list:
            count_list.append(n)
    for x in count_list:
        if seq.count(x) % 2 != 0:
            return x

takes more space 
"""

test_cases = [[20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], [5], [2, 2, 3]]

for case in test_cases:
    print(find_it(case))