"""
Reverse an array in 4 different ways in Python
"""


def reverse_built_in(array):
    array.reverse()
    return array


def reverse_slicing(array):
    reverse_array = array[::-1]
    return reverse_array


def reverse_for_loop(array):
    x = []
    for i in range(len(array) - 1, -1, -1):
        x.append(array[i])
    return x


def reverse_while_loop(array):
    i = len(array) - 1
    x = []
    while i >= 0:
        x.append(array[i])
        i -= 1
    return x


if __name__ == '__main__':
    array = [1, 2, 3, 4]
    print(reverse_while_loop(array))
    array = [1, 2, 3, 4]
    print(reverse_slicing(array))
    array = [1, 2, 3, 4]
    print(reverse_built_in(array))
    array = [1, 2, 3, 4]
    print(reverse_for_loop(array))
