def insertion_sort(array):
    """
    Function to do insertion sort.
    
    Args:
      array (List[int]): input array.
    
    Returns:
      array (List[int]): The return value. A sorted list. 
    """

    for idx in range(1, len(array)):

        key = array[idx]

        j = idx - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


if __name__ == "__main__":
    arr = [3, 2, 1, 4, 7, 6, 10, 8]
    print(insertion_sort(arr))
