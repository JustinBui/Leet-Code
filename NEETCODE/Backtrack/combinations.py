class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # # ---------------------------- BRUTE FORCE ----------------------------
        # nums = [x for x in range(1, n+1)]

        # res = []
        # sub = []

        # def dfs(i):
        #     if i >= len(nums):
        #         if len(sub) == k:
        #             res.append(sub[:])
        #         return
            
        #     sub.append(nums[i])
        #     dfs(i+1)

        #     sub.pop()
        #     dfs(i+1)
        
        # dfs(0)
        # return res

        # Optimized: O(k * n^k)
        res = []

        def backtrack(start_val, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(start_val, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        
        backtrack(1, [])
        return res