"""
Given two strings, write a function to decide if one is permutation of the other
string. 
"""

import collections


def same_permutation(a, b):
    d = collections.defaultdict(int)
    for x in a:
        d[x] += 1
    for x in b:
        d[x] -= 1
    return not any(d.values())


if __name__ == '__main__':
    print(same_permutation('driving', 'drivgni'))
