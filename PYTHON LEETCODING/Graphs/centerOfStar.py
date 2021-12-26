class Solution:
    def constructGraph(self, edges: list[list[int]]) -> dict:
        # Constructing a graph as adjacency list
        graph = {}
        for edge in edges:
            a, b = edge
            if (a not in graph):
                graph[a] = []
            if (b not in graph):
                graph[b] = []

            # Adding all neighbors to current node
            graph[a].append(b)
            graph[b].append(a)

        return graph

    def findCenter(self, edges: list[list[int]]) -> int:
        adjacency_list = self.constructGraph(edges)

        for node in adjacency_list:
            # Seeing how many neighbors each node is connected to
            if (len(adjacency_list[node]) == len(adjacency_list) - 1):
                return node


if (__name__ == "__main__"):
    mySol = Solution()

    edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
    result = mySol.findCenter(edges)
    print(result)
