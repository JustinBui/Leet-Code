class Solution:
    # def constructGraph(self, trust: list[list[int]]) -> dict:
    #     graph = dict()

    #     for item in trust:
    #         # a, b = item
    #         if (item[0] not in graph):
    #             graph[item[0]] = []
    #         if (item[1] not in graph):
    #             graph[item[1]] = []

    #         graph[item[0]].append(item[1])

    #     return graph

    # def findJudge(self, n: int, trust: list[list[int]]) -> int:
    #     if (trust == []):
    #         if (n == 1):    # Edge case: Only person in town
    #             return 1
    #         elif (n > 1):
    #             return -1   # Edge case: No one in town trusts each other

    #     graph = self.constructGraph(trust)

    #     potential_judge = 0
    #     for person in graph:
    #         if (len(graph[person]) == 0):   # Empty array -> trusts no one
    #             potential_judge = person

    #     for person in graph:
    #         if (person == potential_judge):
    #             continue
    #         # At least 1 person doesn't trust the potential judge (i.e the person who)
    #         # trusts no one.
    #         elif (potential_judge not in graph[person]):
    #             return -1

    #     return potential_judge

    ##################################################################################

    # More Efficient Solution: https://www.youtube.com/watch?v=OVdeIkc6Zmk
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        # Determining the inderees and outdegrees for each nodes 1 - n
        for t in trust:
            # a is the one that is trusting (Pointing)
            # b is the one trusted (Being pointed at)
            a, b = t
            outdegree[a] += 1
            indegree[b] += 1

        # Finding who the judge is
        judge = -1
        i = 1
        while (i <= n):
            if (indegree[i] == n - 1 and outdegree[i] == 0):
                judge = i
            i += 1
        return judge


if (__name__ == "__main__"):
    trusts = []
    n = 2

    mySol = Solution()

    judge = mySol.findJudge(n, trusts)
    print(judge)
