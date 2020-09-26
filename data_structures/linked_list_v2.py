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
    

    


