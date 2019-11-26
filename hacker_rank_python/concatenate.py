"""
https://www.hackerrank.com/challenges/np-concatenate
"""
import numpy

m, n, p = map(int, input().strip().split(' '))
arr_1 = []
arr_2 = []

for i in range(m):
    arr_1.append(list(map(int, input().strip().split(' '))))

for i in range(n):
    arr_2.append(list(map(int, input().strip().split(' '))))

np_array = numpy.array(arr_1)
np_array = numpy.array(arr_2)
concate_array = numpy.concatenate((arr_1, arr_2), axis=0)
print(concate_array)
