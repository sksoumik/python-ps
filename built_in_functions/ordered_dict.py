"""
Ref: https://www.geeksforgeeks.org/ordereddict-in-python
"""

from collections import OrderedDict

# normal dictionary
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

print("Unordered Dictionary: Normal Dictionary")
for key, value in d.items():
    print(key, value)

print("\nOrdered Dictionary")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)
