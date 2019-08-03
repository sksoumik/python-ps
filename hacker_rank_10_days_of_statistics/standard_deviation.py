"""
Finding standard deviation
https://www.hackerrank.com/challenges/s10-standard-deviation/problem?h_r=next-challenge&h_v=zen
"""
import math

N = int(input().strip())
X = [int(i) for i in input().strip().split(' ')]

sum_result = 0

for i in range(N):
    sum_result += X[i]

mean = sum_result / N

squared_distance = []
for i in range(N):
    u = (X[i] - mean) * (X[i] - mean)
    squared_distance.append(u)

sum_of_squared_distance = 0
for i in range(len(squared_distance)):
    sum_of_squared_distance += squared_distance[i]

std = math.sqrt(sum_of_squared_distance / N)
print("{0:.1f}".format(std))
