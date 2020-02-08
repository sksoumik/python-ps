"""
Problem: https://www.hackerrank.com/challenges/s10-binomial-distribution-1
Tutorial: https://www.hackerrank.com/challenges/s10-binomial-distribution-1/tutorial
"""

import math

p1 = 1.09
p = p1 / (p1 + 1)
q = 1 - p
n = 6
R = []
for x in range(3, 7):
    c1 = math.factorial(n) / (math.factorial(x) * (math.factorial(n - x)))
    c2 = p**x
    c3 = q**(n - x)
    res = c1 * c2 * c3
    R.append(res)

result = sum(R)
print(round(result, 3))
