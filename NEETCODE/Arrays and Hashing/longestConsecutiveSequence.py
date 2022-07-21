class Solution:

    # ============================= BRUTE FORCED =============================
    def longestConsecutive(self, nums: list[int]) -> int:
        # if (len(nums) == 0):
        #     return 0

        # longest_len = 1
        # nums = sorted(list(set(nums)))

        # candidate = 1
        # for n in range(len(nums)):
        #     if n + 1 == len(nums):
        #         continue
        #     # Seeing if the element before nums[n] has a value of 1 above
        #     if nums[n] == (nums[n + 1] - 1):
        #         candidate += 1

        #         if candidate > longest_len:  # Taking the longest streak
        #             longest_len = candidate
        #     else:
        #         candidate = 1  # If the sequence breaks, restart the streak

        # return longest_len

        nums = set(nums)
        longest = 0

        for n in nums:
            # Seeing if this has no left neighbors (i.e start of the sequence)
            if (n - 1) not in nums:
                candidate = 0
                while (n + candidate) in nums:
                    candidate += 1

                if candidate > longest:
                    longest = candidate

        return longest


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]  # sorted = [1, 2, 3, 4, 100, 200]
    nums = [0, 0, 0, 1, 2, 3, 3, 234, 435]
    s = Solution()
    print(s.longestConsecutive(nums))  # Expected: 4
