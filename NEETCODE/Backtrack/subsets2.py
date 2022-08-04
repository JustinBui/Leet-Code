# BRUTE FORCE
class Solution:
    # MY VERSION
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        sub = []

        def dfs(ind):
            if ind >= len(nums):
                s = sorted(sub[:])
                if s not in res:
                    res.append(s)
                return

            sub.append(nums[ind])
            dfs(ind + 1)

            sub.pop()
            dfs(ind + 1)

        dfs(0)

        return res

    # NEETCODE's VERSION
    def subsetsWithDup2(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []

        def dfs_backtrack(index, subset):
            if index >= len(nums):
                res.append(subset[:])
                return

            subset.append(nums[index])
            dfs_backtrack(index + 1, subset)

            subset.pop()  # Excluding nums[index] from decision space
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                # Moving index forward to prevent duplicates in our list
                index += 1

            dfs_backtrack(index + 1, subset)

        dfs_backtrack(index=0, subset=[])
        return res


if __name__ == '__main__':
    nums = [4, 4, 4, 1, 4]

    obj = Solution()
    print(obj.subsetsWithDup(nums))
