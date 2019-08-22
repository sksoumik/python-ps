"""
Python program to print all Prime numbers in an given interval
"""


def is_prime(start, end):
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                print(i, end=" ")


is_prime(2, 56)
