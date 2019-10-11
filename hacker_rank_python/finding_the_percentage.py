"""
https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""

N = int(input())
D = {}
for i in range(N):
    Name, A, B, C = input().split()
    A = float(A)
    B = float(B)
    C = float(C)
    D[Name] = (A + B + C) / 3

print('%.2f' % D[input()])
