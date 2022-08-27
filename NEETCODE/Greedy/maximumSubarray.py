class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr_sum = 0
        
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            res = max(res, curr_sum)
        
        return res
        
        