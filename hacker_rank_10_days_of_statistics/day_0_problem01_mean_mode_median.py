import numpy as np
from scipy import stats
N = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]

arr.sort()

print('{0:.1f}'.format(np.average(arr)))
print('{0:.1f}'.format(np.median(arr)))
print(int(stats.mode(np.array(arr))[0]))