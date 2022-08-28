class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        left = right = 0
        
        while right < len(nums) - 1:
            furthest_jump = 0
            for i in range(left, right + 1):
                furthest_jump = max(furthest_jump, i + nums[i])
            left = right + 1
            right = furthest_jump
            res += 1
            
        return res


nums = [2,3,1,1,4]
sol = Solution()

print(sol.jump(nums))