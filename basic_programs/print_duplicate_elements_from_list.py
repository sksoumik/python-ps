def find_duplicates(ar):  # O(n^2)
    duplicates = []
    for i in range(0, len(ar)):
        for j in range(i + 1, len(ar)):
            if (ar[i] == ar[j]):
                duplicates.append(ar[j])
    return duplicates


def duplicates_sorting(arr):  # TC: O(n log n) SC: O(n)
    duplicates = []
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            duplicates.append(i)
    return duplicates


def find_duplicates_hashtable(arr):  # TC: O(n) SC: O(n)
    duplicates = []
    seen = set()
    for element in arr:
        if element in seen:
            duplicates.append(element)
        seen.add(element)
    return duplicates


def find_duplicate_floyd(arr):
    duplicates = []

    if len(arr) <= 1:
        return -1
        # Find the intersection point of the two runners.
    tortoise = arr[0]
    hare = arr[arr[0]]
    while (hare != tortoise):
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]

    # Find the "entrance" to the cycle.
    hare = 0
    while (tortoise != hare):
        tortoise = arr[tortoise]
        hare = arr[hare]
    duplicates.append(tortoise)
    return duplicates


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 3, 10, 4]
    print(find_duplicates_hashtable(array))
