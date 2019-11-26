"""
https://www.hackerrank.com/challenges/np-eye-and-identity
"""

import numpy

n, m = map(int, input().strip().split(' '))
print(numpy.eye(n, m, k=0))