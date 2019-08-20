"""
Example: stack of plate
LIFO - Last in First out
Insertion and Deletion both happen in the same end
Basic Operations: push(), pop(), peek(), isEmpty() all take O(1) time
"""
from sys import maxsize


# Create a stack
def create_stack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print(item, "pushed onto stack")


def pop(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)
    return stack.pop()


def peek(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)
    return stack[len(stack) - 1]


# Driver code
stack = create_stack()
push(stack, 10)
push(stack, 20)
push(stack, 30)
pop(stack)  # removed 30
print(stack)
print(peek(stack))  # 20

"""
ref: https://www.geeksforgeeks.org/stack-data-structure-introduction-program/
"""
