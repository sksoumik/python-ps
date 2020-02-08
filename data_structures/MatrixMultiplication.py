A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

B = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

res = [[0 for x in range(4)] for y in range(3)]  # 3*4 matrix

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            res[i][j] += A[i][k] * B[k][j]

for r in res:
    print(r)
