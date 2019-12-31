"""
Link: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
"""
import numpy

A = numpy.array(list(map(float,input().split())))
print(numpy.floor(A),numpy.ceil(A),numpy.rint(A),sep='\n')

