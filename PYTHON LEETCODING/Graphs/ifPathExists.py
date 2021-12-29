class Solution:

    # Building a graph in the form of an adjacency matrix
    def buildGraph(self, edges: list[list[int]]) -> dict:
        graph = dict()  # Each vertex maps to list of neighboring vertices

        for edge in edges:
            a, b = edge
            if (a not in graph):
                graph[a] = []
            if (b not in graph):
                graph[b] = []

            # Adding in neighbors
            graph[a].append(b)
            graph[b].append(a)

        return graph

    def findPathDFS(self, graph: dict, current: int, end: int, visited) -> bool:
        if (current == end):
            return True
        if (current in visited):
            return False

        visited.add(current)
        for neighbor in graph[current]:
            if (self.findPathDFS(graph, neighbor, end, visited) == True):
                return True

        return False

    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:
        adjancencyMatrix = self.buildGraph(edges)
        visited = set()  # Empty set to represent visited nodes
        return self.findPathDFS(adjancencyMatrix, start, end, visited)


if (__name__ == "__main__"):
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    start = 0
    end = 2

    sol = Solution()
    result = sol.validPath(n, edges, start, end)
    print(result)
