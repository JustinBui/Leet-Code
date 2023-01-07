class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []

        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a-1]:
                continue # Skip repeating elements
            for b in range(a+1, len(nums)):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue # Skip repeating elements

                c, d = b+1, len(nums)-1
                while c < d:
                    four_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if four_sum < target:
                        c += 1
                    elif four_sum > target:
                        d -= 1
                    elif four_sum == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
        
        return res
        