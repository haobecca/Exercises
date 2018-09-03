'''
Given a DNA strand, its transcribed RNA strand is formed by replacing

each nucleotide with its complement:

G -> C
C -> G
T -> A
A -> U
'''

def to_rna(dna_strand):
    RNA = []
    for DNA in dna_strand:
        if DNA == 'G':
            RNA.append('C')
        elif DNA == 'C':
            RNA.append('G')
        elif DNA == 'T':
            RNA.append('A')
        else:
            RNA.append('U')
    return ''.join(RNA)
