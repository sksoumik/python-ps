"""
Quartile
https://www.hackerrank.com/challenges/s10-quartiles/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""
N = int(input().strip())
X = [int(i) for i in input().strip().split(' ')]


def median(arr):
    arr.sort()
    if len(arr) % 2 == 1:  # odd
        return arr[int((len(arr) - 1) / 2)]
    else:  # even
        return 0.5 * (arr[int((len(arr) / 2 - 1))] + arr[int(len(arr) / 2)])


Q2 = median(X)
left_arr = [int(i) for i in X if i < Q2]
right_arr = [int(i) for i in X if i > Q2]
Q1 = median(left_arr)
Q3 = median(right_arr)

print(int(Q1))
print(int(Q2))
print(int(Q3))
