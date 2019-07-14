"""
Priority Queue is more specialized data structure than Queue. It can be implemented using Array or Heap.
But Heap is a better solution in terms of time complexity.
Using Heap,
getHighestPriority -> O(1)
Insertion -> O(log N)
Deletion -> O(log N)
"""

from __future__ import print_function, division

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

class Heap:

    def __init__(self):
        self.h = []
        self.currsize = 0


    def leftChild(self,i):
        if 2*i+1 < self.currsize:
            return 2*i+1
        else:
            return None


    def rightChild(self,i):
        if 2*i+2 < self.currsize:
            return 2*i+2
        else:
            return None


    def maxHeapify(self, node):
        if node < self.currsize:
            m = node
            lc= self.leftChild(node)
            rc = self.rightChild(node)








