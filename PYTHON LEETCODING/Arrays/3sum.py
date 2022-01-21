class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        LENGTH = len(nums)
        if (LENGTH >= 3):

            for i in range(LENGTH - 2):
                if (i == 0 or nums[i] != nums[i - 1]):  # Prevents duplicates of i
                    j, k = i + 1, LENGTH - 1

                    while (j < k):
                        if (nums[i] + nums[j] + nums[k] == 0):
                            result.append([nums[i], nums[j], nums[k]])
                            j += 1
                        elif (nums[i] + nums[j] + nums[k] > 0):
                            k -= 1
                        else:  # if (nums[i] + nums[j] + nums[k] < 0)
                            j += 1

                        # Moving j and k up if there are any repeating values
                        # to prevent getting duplicate arrays appended to result
                        while(j != i + 1 and nums[j] == nums[j - 1] and j < k):
                            j += 1
                        while (k != LENGTH - 1 and nums[k] == nums[k + 1] and j < k):
                            k -= 1

        return result


nums = [-1, 0, 1, 2, -1, -4]
myTest = Solution()

newList = myTest.threeSum(nums)
print(newList)
