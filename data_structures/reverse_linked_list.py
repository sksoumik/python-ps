"""
Reverse a linked list
Given linked list
85 15 4 20
Reversed Linked list
20 4 15 85
"""


# create a Node, node has two part: data field, link to next node('next')
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):  # initialize head
        self.head = None

    def reverse_linked_list(self):
        previous = None
        current = self.head

        while(current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous


    def push_at_start(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def print_linked_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next



# Driver code
linked_list = LinkedList()
linked_list.push_at_start(50)
linked_list.push_at_start(40)
linked_list.push_at_start(30)
linked_list.push_at_start(20)
linked_list.push_at_start(10)

print("Original linked list")
linked_list.print_linked_list()

linked_list.reverse_linked_list()
print("\nAfter reversing the linked list")
linked_list.print_linked_list()

"""
Time complexity: O(n), reverse_linked_list()
"""