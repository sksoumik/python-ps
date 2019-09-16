"""
Find all the permutations of a given string
"""
from itertools import permutations


def permutation(string):
    p = permutations(string)

    for i in list(p):
        print(''.join(i), end=" ")


if __name__ == '__main__':
    sample = 'ABC'
    permutation(sample)
