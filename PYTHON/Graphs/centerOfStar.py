class Solution:
    # def constructGraph(self, edges: list[list[int]]) -> dict:
    #     # Constructing a graph as adjacency list
    #     graph = {}
    #     for edge in edges:
    #         a, b = edge
    #         if (a not in graph):
    #             graph[a] = []
    #         if (b not in graph):
    #             graph[b] = []

    #         # Adding all neighbors to current node
    #         graph[a].append(b)
    #         graph[b].append(a)

    #     return graph

    # def findCenter(self, edges: list[list[int]]) -> int:
    #     adjacency_list = self.constructGraph(edges)

    #     for node in adjacency_list:
    #         # Seeing how many neighbors each node is connected to
    #         if (len(adjacency_list[node]) == len(adjacency_list) - 1):
    #             return node

    ############################################################################
    # More efficient solution: https://www.youtube.com/watch?v=arNZUOxpXdU
    def findCenter(self, edges: list[list[int]]) -> int:

        # Finding how many total nodes in graph
        n = 0
        for edge in edges:
            n = max(n, edge[0], edge[1])

        # List representing graph:
        # - Each index is the value of a vertex
        # - The values in the index represents the number of neighbors the node has
        nodes_list = [0] * (n + 1)
        for edge in edges:
            nodes_list[edge[0]] += 1
            nodes_list[edge[1]] += 1

        # Finding the node (Represented as index i) that
        # has n - 1 neighbors
        i = 0
        while (i < len(nodes_list)):
            if (nodes_list[i] == n - 1):
                return i
            i += 1


if (__name__ == "__main__"):
    mySol = Solution()

    edges = [[1, 2], [2, 3], [4, 2]]
    result = mySol.findCenter(edges)
    print(result)
