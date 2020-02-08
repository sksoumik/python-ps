"""
Ref: https://www.codesdope.com/course/data-structures-doubly-linked-lists/
"""


class Node:
    def __init__(self, data):
        self.data = data
        # two pointers next and previous to make a node instead of just
        # using next as we did in the singly linked list.
        self.next = None
        self.previous = None

        # Inserting a New Node at the Front


class LinkedList:
    def __init__(self, data):
        a = Node(data)
        self.head = a


def traversal(list):
    temp = list.head  # temporary pointer to point to head
    a = ''

    while temp != None:
        a = a + str(temp.data) + '\t'
        temp = temp.next

    print(a)


def insert_at_front(list, node):
    node.next = list.head
    list.head.previous = node
    list.head = node


def insert_after_tail(list, node):
    temp = list.head

    while temp != None:
        temp = temp.next

    temp.next = node
    node.previous = temp


def insert_after(node, position_after):
    node.next = position_after.next
    position_after.next.previous = node
    position_after.next = node
    node.previous = position_after
