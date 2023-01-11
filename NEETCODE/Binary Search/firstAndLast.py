class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def boundedBinarySearch(bound):
            l, r = 0, len(nums) - 1
            i = -1
            while l <= r:
                m = (l + r) // 2
                
                if nums[m] == target:
                    i = m
                    if bound == 'l': # left bound, then continue binary search on left half
                        r = m - 1
                    elif bound == 'r': # right bound, therefore continue binary search on right half
                        l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else: # if nums[m] > target
                    r = m - 1

            return i
        
        return [boundedBinarySearch('l'), boundedBinarySearch('r')]