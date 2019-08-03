"""
https://www.hackerrank.com/challenges/s10-interquartile-range/problem
"""
N = int(input().strip())
X_elements = [int(i) for i in input().strip().split(' ')]
X_frequency = [int(i) for i in input().strip().split(' ')]
full_array = []

for i in range(N):
    for j in range(X_frequency[i]):
        full_array.append(X_elements[i])

full_array.sort()


def median(arr):
    arr.sort()
    if len(arr) % 2 == 1:  # odd
        return arr[int((len(arr) - 1) / 2)]
    else:  # even
        return 0.5 * (arr[int((len(arr) / 2 - 1))] + arr[int(len(arr) / 2)])


Q2 = median(full_array)
left_arr = [int(i) for i in full_array if i < Q2]
right_arr = [int(i) for i in full_array if i > Q2]

Q1 = median(left_arr)
Q3 = median(right_arr)

inter_q = Q3 - Q1
print('{0:0.1f}'.format(inter_q))
