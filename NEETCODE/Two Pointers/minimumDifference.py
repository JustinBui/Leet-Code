class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')

        for i in range(len(nums) - k + 1):
            res = min(res, max(nums[i:i+k]) - min(nums[i:i+k]))
        
        return res