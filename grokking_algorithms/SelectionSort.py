def find_smallest_index(array):
    smallest_item = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest_item:
            smallest_item = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        smallest_item = find_smallest_index(array)
        new_array.append(array.pop(smallest_item))
    return new_array


array = [2, 4, 1, 5, 6]
print(selection_sort(array))
"""
For travelling n number of items for n times the time complexity is
O(n^2)
"""