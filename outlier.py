'''
You are given an array (which will have a length of at least 3, but could be very large)
containing integers. The array is either entirely comprised of odd integers or entirely 
comprised of even integers except for a single integer N. Write a method that takes the 
array as an argument and returns this "outlier" N.
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)
[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''


def find_outlier(integers):
    is_odd_list = [n % 2 for n in integers]
    return integers[is_odd_list.index(1)] if is_odd_list[0:4].count(0) > 1 else integers[is_odd_list.index(0)]

'''
0.078 seconds

def find_outlier(integers):
    odd = []
    even = []
    for n in integers:
        if n % 2:
            odd.append(n)
        else:
            even.append(n)
    return odd[0] if len(odd) == 1 else even[0]
'''
test_cases = [[2, 4, 0, 100, 4, 11, 2602, 36], [160, 3, 1719, 19, 11, 13, -21]]

for case in test_cases:
    print(find_outlier(case))