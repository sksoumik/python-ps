lowest_num = float('inf')

array = [10, 2000000, 4, 3]

for i in array:
    if i < lowest_num:
        lowest_num = i

print(lowest_num)