def scale(data, factor):
    for i in range(len(data)):
        data[i] = data[i] * factor
    print(data)


d = [1, 2, 3, 4, 5, 6]
f = 2
scale(d, f)
