import numpy
# axis 0 means column wise
# axis 1 means row wise
m, n = map(int, input().strip().split(' '))
arr = []
for i in range(m):
    arr.append(numpy.array(list(map(int, input().strip().split(' ')))))

min_array = numpy.min(arr, axis=1)
print(max(min_array))
