# Solution: https://www.youtube.com/watch?v=mQeF6bN8hMk
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Edge case where the graph is NULL
        if (node == None):
            return None

        hashMap = dict()  # Key: Original Node | Value: Copy of original node

        def dfs_clone(node):
            if (node in hashMap):
                # There is already a copy of the node, so no need for
                # further procedures, just return the node
                return hashMap[node]

            # If copy does NOT exist:
            # create a new copy and recursively add it's neigbors
            copy = Node(node.val)
            hashMap[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs_clone(n))
            return copy

        return dfs_clone(node)
