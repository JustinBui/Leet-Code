# DFS: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/?ref=lbp
# BFS: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/?ref=lbp

from typing import collections


class Adjacency_List:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = dict()

    # Function to add an edge to graph
    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)

    def BFS(self, s):
        queue = collections.deque()
        visited = []

        if (s in self.graph):
            queue.append(s)

        while (len(queue) != 0):
            candidate = queue.popleft()

            if (candidate not in visited):
                print(candidate, end=" ")
                visited.append(candidate)

            for neighbor in self.graph[candidate]:
                if (neighbor not in visited):
                    queue.append(neighbor)


# CONSTRAINTS: Each node is numbered 0 - (n - 1), where n is the total number of nodes
#             Each node is UNIQUE (i.e no repeating values)
if __name__ == "__main__":
    g = Adjacency_List()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print("Following is DFS from (starting from vertex 2)")
    g.DFS(2)

    g2 = Adjacency_List()
    g2.addEdge(0, 1)
    g2.addEdge(0, 2)
    g2.addEdge(1, 2)
    g2.addEdge(2, 0)
    g2.addEdge(2, 3)
    g2.addEdge(3, 3)
    print("\nFollowing is BFS from (starting from vertex 2)")
    g2.BFS(2)
