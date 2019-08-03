"""
https://www.hackerrank.com/challenges/s10-weighted-mean/problem
"""

N = int(input().strip())

X = [int(i) for i in input().strip().split(' ')]
W = [int(i) for i in input().strip().split(' ')]

sum_of_x = 0

for i in range(N):
    sum_of_x += X[i] * W[i]

weighted_mean = sum_of_x / sum(W)
print("{0:.1f}".format(weighted_mean))
