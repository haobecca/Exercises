# Practicing List comprehension with dictionary, set and math
# From Python Essential Training with Bill Weinman on Lynda.com

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

def seq1():
    seq = range(11)
    from math import pi
    seq2 = [round(pi, i) for i in seq]
    print_list(seq)
    print_list(seq2)

seq1()


def seq2():
    seq = range(11)
    seq2 = {x for x in 'superduper' if x not in 'pd'}
    print_list(seq)
    print_list(seq2)

seq2()

def seq3():
    seq = range(11)
    seq2 = {x: x**2 for x in seq}
    print_list(seq)
    print(seq2)

seq3()