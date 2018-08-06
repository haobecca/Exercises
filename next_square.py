"""
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

Examples:
findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
"""

def find_next_square(num):
    root = num ** 0.5
    return (int(root) + 1) ** 2 if root.is_integer() else -1

test_cases = [121, 625, 114]

for x in test_cases:
    print(find_next_square(x))