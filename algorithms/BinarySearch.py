def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid_position = (low + high) // 2
        mid_item = list[mid_position]
        if mid_item == item:
            return mid_position
        if mid_item > item:
            high = mid_position - 1
        else:
            low = mid_position + 1
    return None


my_list = [1, 3, 5, 7, 9]
print("position: ", binary_search(my_list, 9))
print("position: ", binary_search(my_list, -1))
