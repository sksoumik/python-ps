"""
Print duplicate elements from a list/array 
"""

def find_duplicates(ar):
    duplicates = []
    for i in range(0, len(ar)):
        for j in range(i + 1, len(ar)):
            if (ar[i] == ar[j]):
                duplicates.append(ar[j])
    return duplicates


if __name__ == "__main__":
    array = [1, 2, 4, 5, 2, 4, 10]
    print(find_duplicates(array))
