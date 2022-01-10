# Sources: https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

class Solution:
    def adjacencyList(self, prerequisites: list[list[int]]) -> dict:
        # Converting edge list to adjacency list (Directed graph)
        graph = dict()

        for edge in prerequisites:
            a, b = edge
            if (a not in graph):
                graph[a] = []
            if (b not in graph):
                graph[b] = []

            graph[a].append(b)

        return graph

    def cycleDetected(self, current: int, prerequisites: dict, visited: list[bool], recStack: list[bool]) -> bool:
        visited[current] = True
        recStack[current] = True

        for neighbor in prerequisites[current]:
            if (visited[neighbor] == False):
                if (self.cycleDetected(neighbor, prerequisites, visited, recStack) == True):
                    return True
            # A node can be visited, but not necessarily part of the recursion stack
            # The recursion stack represents the steps it takes to build up a path for a potential cycle
            elif (recStack[neighbor] == True):
                return True

        # When the node we visited is not pointing
        # to any other nodes or all of the nodes it pointed
        # to was already visited, but still found NO cycle
        # Popping current node off stack to find another path
        recStack[current] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if (len(prerequisites) == 0):   # Edge case: There are no prereqs
            return True

        adjacencyList = self.adjacencyList(prerequisites)
        visited = [False] * numCourses
        recursionStack = [False] * numCourses

        for i in prerequisites:
            if (visited[i[0]] == False):
                if (self.cycleDetected(i[0], adjacencyList, visited, recursionStack)):
                    return False    # Cannot finish course schedule if a cycle is detected

        return True


if (__name__ == "__main__"):
    testSolution = Solution()

    numCourses = 20
    prerequisites = [[0, 10], [3, 18], [5, 5], [
        6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]

    result = testSolution.canFinish(numCourses, prerequisites)
    print(result)
