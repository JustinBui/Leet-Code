# BRUTE FORCE
class Solution:
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


if __name__ == '__main__':
    nums = [4, 4, 4, 1, 4]

    obj = Solution()
    print(obj.subsetsWithDup(nums))
