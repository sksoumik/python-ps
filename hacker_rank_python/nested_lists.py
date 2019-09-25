"""
https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen
"""

name = []
grade = []
for i in range(int(input())):
    name.append(input())
    grade.append(float(input()))

m = min(grade)
re = []
for i in range(len(grade)):
    if grade[i] == m:
        grade[i] = 1000000000

m = min(grade)

for i in range(len(grade)):
    if grade[i] == m:
        re.append(name[i])

re.sort()

for i in re:
    print(i)
