class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        edges = dict()

        for row in wall:
            it = 0  # Iterator to keep track of the current crack in the current row of our wall
            for i in range(len(row) - 1):
                it += row[i]

                if not edges.get(it):
                    edges[it] = 1
                else:
                    edges[it] += 1
        
        max_edges = max(list(edges.values())) if len(edges) > 0 else 0

        return len(wall) - max_edges


if __name__ == '__main__':
    entity = Solution()

    wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    print(entity.leastBricks(wall))

    wall2 = [[10],[10],[10]]
    print(entity.leastBricks(wall2))