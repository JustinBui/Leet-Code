class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        # Finding prefix sums
        prefix_sum1 = grid[0]
        prefix_sum2 = grid[1]

        for i in range(1, len(grid[0])):
            prefix_sum1[i] += prefix_sum1[i - 1]
            prefix_sum2[i] += prefix_sum2[i - 1]

        res = float("inf")
        for i in range(len(grid[0])):
            top = grid[0][-1] - grid[0][i]
            bottom = grid[1][i-1] if i > 0 else 0

            # The second robot wants to get the MAX score it can possibly get
            second_robot_score = max(top, bottom)

            # The first robot wants to MINIMIZE the scores that second robot can get.
            # Therefore, the second robot's MAX score is the minimum it can get according to
            # first robot's perspective 
            res = min(res, second_robot_score)
        
        return res

if __name__ == '__main__':
    grid_1 = [[2,5,4],[1,5,1]]
    entity = Solution()

    print(entity.gridGame(grid_1))

    grid2 = [[1,3,1,15],[1,3,3,1]]
    print(entity.gridGame(grid_1))
