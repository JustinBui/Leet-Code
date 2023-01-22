class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        tracker = dict()
        res = []

        for i in range(1, len(nums) + 1): # [1, n] inclusive
            tracker[i] = 0
        
        for n in nums:
            tracker[n] += 1
        
        for k in tracker.keys():
            if tracker[k] == 0:
                res.append(k)
        
        return res