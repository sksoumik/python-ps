"""
BFS uses queue(FIFO)
"""
from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):  # s = source
        # mark all the vertices as not visited
        visited = [False] * len(self.graph)  # a list containing all elements as False
        # create a queue for bfs
        queue = []
        # mark the source vertex as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # dequeue a vertex from the queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            """ Get all adjacent vertices of the 
            dequeued vertex s. If a adjacent 
            has not been visited, then mark it 
             visited and enqueue it 
            """
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# driver code

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS traversal is: ")
g.bfs(2)


"""
ref: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
"""