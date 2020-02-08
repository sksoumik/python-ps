"""
Checking for balanced parentheses using Queue.
"""


def check(expression):
    open_tuple = tuple('({[')
    close_tuple = tuple(')}]')
    map = dict(zip(open_tuple, close_tuple))
    queue = []

    for i in expression:
        if i in open_tuple:
            queue.append(map[i])
        elif i in close_tuple:
            if not queue or i != queue.pop():
                return "Unbalanced"

    return "Balanced"


# Driver code
string = input()
print(string, '-', check(string))
"""
Ref: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
"""
