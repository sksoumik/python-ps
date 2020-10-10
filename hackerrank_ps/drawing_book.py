'''
https://www.hackerrank.com/challenges/drawing-book
'''
#!/bin/python3

import os
import sys


#
# Complete the pageCount function below.
#
def pageCount(n, p):
    start = p // 2
    end = n // 2 - (p // 2)
    return min(start, end)


if __name__ == '__main__':
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    print(result)
