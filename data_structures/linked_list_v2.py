from __future__ import print_function
'''
https://youtu.be/AvGNrp4Al0A

Dynamic data structure made up of nodes. Dynamic ds means that we can allocate
the required memory while the program is running. A dynamic ds can easily expand 
or shrink during runtime. So, a linkedlist does not have a predetermined fixed size.
It does not allocate memory for the next item. Array based sequences, we need large
chunk of contiguous memory, if many elements are are to be stored, while in the cases
of LL, there is a distributed representation of elemente, elements are not stored in
contiguous locations, so many items can be easily stored even if contiguous memory
is not available. 

Insertion and deletion is easier. 

LL can be implemented using list, stack, and queues. 
'''


class Node:

    def __init__(self, value):
        self.info = value
        self.link = None
    

class SingleLinkedList:

    def __init__(self):
        self.start = None
    
    # print all elements of a singly linked list 
    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is: ")
            p = self.start
            while p is not None:
                print(p.info, end=' ')
                p = p.link
            print()

    # count the number of nodes in the linked list 
    def count_nodes(self):
        p = self.start
        counter = 0
        while is not None:
            counter = counter + 1 
            p = p.link
        print(f"Number of nodes in the list: {counter}")

    # search for a specific value in the list 
    def search(self, search_value):
        position = 1
        p = self.start
        while p is not None:
            if p.info == search_value:
                print(f"{search_value} found at position {position}")
                return True
            position = position + 1
            p = p.link
        else:
            print(f"{search_value} not found in the list") 
            return False
    
    
    
    
    def insert_at_beginning(self, data):
        pass

    def insert_at_end(self, data):
        pass

    def create_list(self):
        pass
    
    # insert after  a given node 
    def insert_after(self, data, x):
        pass
    
    # insert before a given node 
    def insert_before(self, data, x):
        pass
    
    def insert_at_position(self, data, k):
        pass
    
    

    
# driver code
list = SingleLinkedList()
list.create_list()

while True:


    

    


