"""
https://www.hackerrank.com/challenges/no-idea/problem
"""
n, m = map(int, input().strip().split(' '))
arr = list(map(int, input().strip().split(' ')))
A = set(map(int, input().strip().split(' ')))
B = set(map(int, input().strip().split(' ')))

happiness = 0
for i in arr:
    if i in A:
        happiness += 1

for i in arr:
    if i in B:
        happiness -= 1

print(happiness)
