import numpy

array = input().split(' ')
np_array = numpy.array(array).astype(int)

ch = numpy.reshape(np_array, (3, 3))
print(ch)
