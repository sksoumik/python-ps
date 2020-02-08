"""
Ref: https://www.codesdope.com/course/data-structures-linked-lists/
"""


# next = link
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        a = Node(data)
        self.head = a


def traversal(list):  # linkedlist = list
    temp = list.head  # temp is pointing to the head of the linked list

    a = ''
    while temp != None:  # loop runs until it finds null/ none
        a = a + str(temp.data) + "\t"
        temp = temp.next

    print(a)


def insert_at_beginning(list, node):
    node.next = list.head
    list.head = node


def insert_at_last(list, node):
    temp = list.head

    while temp != None:
        temp = temp.next
    temp.next = node


def insert_node_after(node, position):
    node.next = position.next
    position.next = node


def delete(list, node):
    temp = list.head

    if temp == node:  # if the deleted item is head
        list.head = node.next
        del node

    else:  # node to be deleted is not head
        while temp != None:
            if temp.next == node:  # node previous to node to be deleted
                temp.next = node.next
                del node
                break
            temp = temp.next


if __name__ == '__main__':
    list = LinkedList(10)

    a = Node(20)
    b = Node(50)
    c = Node(30)

    list.head.next = a
    a.next = b
    b.next = c

    traversal(list)

    z = Node(10)
    insert_at_beginning(list, z)
    traversal(list)

    x = Node(15)
    insert_node_after(x, z)  # insert x after z
    traversal(list)

    delete(list, list.head)  # deletes the head node
    traversal(list)

    delete(list, c)  # deletes the value of c = 30
    traversal(list)
