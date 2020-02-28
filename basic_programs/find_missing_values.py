"""
Find missing values from a contigious list
"""


def find_missing_values(arr):
    missing_values = []
    remove_duplicates = set(arr)
    for i in range(arr[0], arr[-1] + 1):
        if i not in remove_duplicates:
            missing_values.append(i)
    return missing_values


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 7, 8, 10, 10]
    print(find_missing_values(arr))
