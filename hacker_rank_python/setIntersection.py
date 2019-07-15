"""
https://www.hackerrank.com/challenges/py-set-intersection-operation
Set-> intersection operation. Can also be expressed as & like A&B 
"""

n1 = int(input())
setA = set(map(int, input().split()))
n2 = int(input())
setB = set(map(int, input().split()))

print(len(setA.intersection(setB)))
