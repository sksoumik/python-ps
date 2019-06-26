n = int(input())
m = input().strip().split(' ')
res = m[::-1]
r = ""

for i in range(n):
    r = r + str(res[i]) + " "

print(r)