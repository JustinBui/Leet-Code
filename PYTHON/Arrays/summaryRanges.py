# Solution: https://www.youtube.com/watch?v=AjE4x3Yh9xc

class Solution(object):
    def summaryRanges(self, nums):

        if (len(nums) == 0):
            return []

        ranges = []
        LENGTH = len(nums)
        start = nums[0]

        for i in range(LENGTH):
            if (i == LENGTH - 1 or nums[i]+1 != nums[i+1]):
                if (start != nums[i]):
                    ranges.append(f"{start}->{nums[i]}")
                else:
                    ranges.append(f"{start}")
                if (i != LENGTH - 1):
                    start = nums[i + 1]
            
        return ranges


if __name__ == "__main__":
    nums = [0,1,2,4,5,7]

    test = Solution()
    answer = test.summaryRanges(nums)

    print(answer)
