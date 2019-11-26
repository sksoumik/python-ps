"""
https://www.hackerrank.com/challenges/np-zeros-and-ones
"""
import numpy

dim_size = tuple(map(int, input().strip().split(' ')))
print(numpy.zeros(dim_size, int))
print(numpy.ones(dim_size, int))
