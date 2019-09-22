"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""


def runner_up(arr):
    max_score = second_max_score = -1000

    for i in range(0, len(arr)):
        if arr[i] > max_score:
            max_score = arr[i]

    for i in range(0, len(arr)):
        if second_max_score < arr[i] < max_score:
            second_max_score = arr[i]

    print(second_max_score)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    runner_up(arr)
