def high_and_low(numbers):
     num_list = [int(n) for n in numbers.split(' ')]
     return str(max(num_list)) + ' ' + str(min(num_list))

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))