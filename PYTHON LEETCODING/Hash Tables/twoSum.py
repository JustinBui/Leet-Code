class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        hashTable = dict()
        while (i < len(nums)):
            complement = target - nums[i]
            find = hashTable.get(nums[i])
            if (find == None):
                # If complement's corresponding index not found, store it into hash table
                hashTable[complement] = i
            else:
                return [hashTable[nums[i]], i]
            i += 1


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6

    mySol = Solution()
    newList = mySol.twoSum(nums, target)

    print(newList)
