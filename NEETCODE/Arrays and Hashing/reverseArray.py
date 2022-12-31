class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return

        l = 0
        r = len(nums) - 1

        while l <= r: # Inverting input array
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        k %= len(nums)
        
        # Inverting subarray at nums[:k]
        l = 0
        r = k - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Inverting subarray at nums[k:] (The rest of the array)
        l = k
        r = len(nums) - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        