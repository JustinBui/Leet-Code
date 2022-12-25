class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        # --------------- BRUTE FORCE ------------------
        # nums = sorted(nums)
        # self.res = 0

        # def backtrack(i, subset):
        #     if i >= len(nums):
        #         if len(subset) > 0 and min(subset) + max(subset) <= target:
        #             self.res += 1
        #         return

        #     subset.append(nums[i])
        #     backtrack(i + 1, subset)

        #     subset.pop()
        #     backtrack(i + 1, subset)

        # backtrack(0, [])

        # return self.res

        # -------------- USING 2 POINTER METHOD --------------
        res = 0
        mod = 10**9 + 7

        nums = sorted(nums) # 2 pointer methods typically need sorted arrays

        right_ptr = len(nums) - 1
        for i, left in enumerate(nums):
            while i <= right_ptr and left + nums[right_ptr] > target:
                right_ptr -= 1 # Decrement the right pointer until the sums of values at left and right <= target
            if i <= right_ptr:
                res += (2**(right_ptr - i))
        return res % mod


if __name__ == '__main__':
    nums = [2,3,3,4,6,7]
    target = 12

    entity = Solution()
    print(entity.numSubseq(nums, target))
