a = [1,2,3,4,5]
b = [11,12,13,14,15]

result = []

for first, second in zip(a, b):
    result.append(first + second)

print(result)

# output: [12, 14, 16, 18, 20]