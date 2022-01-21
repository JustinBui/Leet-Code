class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        print(nums)
        for i in range(1, len(nums)):
            if (nums[i] == nums[i - 1]):
                return True

        return False


test = Solution()
nums = [1, 2, 3, 1]

value = test.containsDuplicate(nums)
print(value)
