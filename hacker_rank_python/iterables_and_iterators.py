n = int(input())
l = list(input().strip().split(' '))
k = int(input())

from itertools import combinations
contain = 0
total = 0

for i in combinations(l, k):
    if 'a' in i:
        contain += 1
    total += 1

print(float(contain / total))
