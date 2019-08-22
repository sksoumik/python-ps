"""
Python program to check whether a number is Prime or not
"""


def is_prime(num):
    return all(num % i for i in range(2, num))


# driver code
n = int(input())
if is_prime(n):
    print("Prime")
else:
    print("Not prime")
