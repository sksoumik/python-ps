# NumPy  = Numerical Python
"""
A NumPy array is a grid of values. They are similar to lists, except that every element of an numpy array must be the same type.
"""
import numpy as np


def arrays(arr):
    arr = np.array(arr)
    return arr[::-1].astype(float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
