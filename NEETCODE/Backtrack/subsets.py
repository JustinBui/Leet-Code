# Supplemental Solution for further explanation: https://www.youtube.com/watch?v=nqfphpPwKsw

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def backtrack(ind):
            # BASE CASE
            if ind >= len(nums):
                res.append(subset.copy())
                return

            # RECURSIVE CASE (Our decision space)
            # Decision 1: To include the latest number
            subset.append(nums[ind])
            backtrack(ind + 1)

            subset.pop()  # Decision 2: To NOT include the latest number
            backtrack(ind + 1)

        backtrack(0)

        return res


if __name__ == '__main__':
    obj = Solution()

    nums = [1, 2, 3]
    obj.subsets(nums)
