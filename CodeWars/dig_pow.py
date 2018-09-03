'''
Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n. In other words:
Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
If it is the case we will return k, if not return -1.
Note: n, p will always be given as strictly positive integers.
'''
'''
def dig_pow(number, power):
    digit_list = []
    init_power = power
    num_list = list(str(number))
    power_inc = init_power + len(num_list) - 1
    while power < power_inc:
        for x in num_list:
            digit_list.append(int(x) ** power)
            power += 1
    k = sum(digit_list)/number
    if k.is_integer():
        return int(k)
    else:
        return -1
'''

def dig_pow(number, power):
    digit_list = [int(x) ** int(p) for p, x in enumerate(list(str(number)), power)]
    k = sum(digit_list)/number
    return int(k) if k.is_integer() else -1

test_cases = [(89, 1), (695, 2), (46288, 3)]

for case in test_cases:
    print(dig_pow(*case))

