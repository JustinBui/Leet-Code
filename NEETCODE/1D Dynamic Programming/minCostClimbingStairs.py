class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        # Looping backwards starting at third to last position
        for i in range(len(cost) - 3, -1, -1):
            # Comparing (Backwards) on which steps we should take (1 or 2?)
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
        
        # This is because we can either start at the 0th step (With 1 step)
        # OR the 1st step (With 2 steps)
        return min(cost[0], cost[1])