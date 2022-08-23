# Solution: https://www.youtube.com/watch?v=Akt3glAwyfY


class Solution:
    def adjacencyList(self, numCourses: int, prerequisites: list[list[int]]) -> dict:
        # Converting edge list to adjacency list
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        return graph

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        visited = set()
        recusion_stack = []  # Serves as the current path traversed around the graph
        ordering = []

        hash_set = self.adjacencyList(numCourses, prerequisites)

        def dfs(node: int) -> bool:
            # -------------- Base case --------------
            if (node in recusion_stack):
                # If we repeat nodes in the recursion stack, then it is a cycle (MUST NOT HAVE)
                return False
            if (node in visited):
                # If the node's neighbors are already visited knowing we don't have a cycle, then it is a valid path
                return True

            # -------------- Recursive case --------------
            recusion_stack.append(node)
            for neighbor in hash_set[node]:
                if (dfs(neighbor) == False):
                    return False

            recusion_stack.remove(node)
            visited.add(node)
            ordering.append(node)
            return True

        for n in range(numCourses):
            if (dfs(n) == False):
                return []   # CYCLE DETECTED: Impossible to have a topological order

        return ordering


if __name__ == "__main__":
    sample = Solution()
    numCourses = 1
    prerequisites = []
    order = sample.findOrder(numCourses, prerequisites)

    print(order)
