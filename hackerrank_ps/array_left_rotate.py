# https://www.hackerrank.com/challenges/ctci-array-left-rotation 

def rotLeft(a, d):
    a = list(a)
    return a[d:] + a[:d]


if __name__ == "__main__":
    n, d = map(int, input().strip().split(" "))
    a = map(int, input().strip().split(" "))
    left_rotated_array = rotLeft(a, d)
    print(*left_rotated_array, sep=" ")?