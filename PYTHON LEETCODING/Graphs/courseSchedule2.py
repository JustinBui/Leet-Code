from types import prepare_class


class Solution:
    def adjacencyList(self, prerequisites: list[list[int]]) -> dict:
        # Converting edge list to adjacency list
        graph = dict()
        for course, pre in prerequisites:
            if (course not in graph):
                graph[course] = []
            graph[course].append(pre)

        return graph

    def dfs(self, prerequisites: dict, current_visited: list[int], at: int, visited: set):
        visited.add(at)

        for neighbor in prerequisites[at]:
            if neighbor in visited:
                return []

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        visited = set()
        ordering = []

        for i in range(numCourses):
            current_visited = []
            self.dfs(self.adjacencyList(prerequisites),
                     current_visited, i, visited)

            if (current_visited == []):
                return []

            for cv in current_visited:
                ordering.append(current_visited)

        return ordering
