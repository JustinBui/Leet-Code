class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        l, r = 0, 0
        res, total = 0, 0
        left_increment = False

        while r < len(nums):
            length = (r - l + 1)

            if left_increment == False:
                total += nums[r]
                
            if nums[r] * length <= total + k:
                left_increment = False
                res = max(res, length)
                r += 1
            else:
                left_increment = True
                total -= nums[l]
                l += 1
            
        return res