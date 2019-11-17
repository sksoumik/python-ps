import numpy

m, n = map(int, input().strip().split(' '))

arr = []

for i in range(m):
    arr.append(list(map(int, input().strip().split(' '))))

arr = numpy.array(arr)
print(arr.transpose())
print(arr.flatten())