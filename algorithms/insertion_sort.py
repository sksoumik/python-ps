"""
insertion vs selection sort
Insertion sort: Keeping the similar assumption in mind but the only difference
is that this time we are selecting one number  at a time and inserting it in
the presorted part, that reduced the comparisons and hence insertion sort is more efficient.

Time Complexity of selection sort is 'always' n^2, whereas insertion sort has better time
complexity as its worst case complexity is n^2. Generally it will take lesser or equal
comparisons then n^2.
"""
def insertion(M):
    for i in range(1,len(M)):
        for j in range(i):
            if M[i] < M[j]:
                M[j],M[j+1:i+1] = M[i],M[j:i]
                break



array = [5,8,9,6,7,10]
insertion(array)
n = len(array)

for i in range(n):
    print(array[i], end=" ")

