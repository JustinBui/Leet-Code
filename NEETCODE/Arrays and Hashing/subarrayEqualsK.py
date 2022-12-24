class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # ------------- BRUTE FORCE -------------
        # res = 0
        # subarray_size = 1

        # while subarray_size <= len(nums):
        #     for i in range(len(nums) - subarray_size + 1):
        #         if sum(nums[i:i+subarray_size]) == k:
        #             res += 1
        #     subarray_size += 1
        
        # return res

        # ------------- LINEAR TIME -------------
        res = 0
        prefixes = dict() # Keys are prefixes, values are counts (occurences) of prefixes
        prefixes[0] = 1

        total = 0
        for n in nums:
            total += n
            possible_prefix = total - k
            if prefixes.get(possible_prefix):
                res += prefixes[possible_prefix]
            if not prefixes.get(total):
                prefixes[total] = 1
            else:
                prefixes[total] += 1

        return res               
            


if __name__ == '__main__':
    nums = [1, -1, 1, 1, 1, 1]
    k = 3

    entity = Solution()
    print(entity.subarraySum(nums, k))