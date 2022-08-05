class Solution:
    # USING RECURSION:
    # def search(self, nums: list[int], target: int) -> int:

    #     def binary_search(start, end):
    #         if start >= end:
    #             if nums[start] == target:
    #                 return start
    #             else:
    #                 return -1

    #         mid = (start + end) // 2  # Floor division
    #         if target == nums[mid]:
    #             return mid
    #         elif target > nums[mid]:
    #             # Search upper half
    #             return binary_search(mid + 1, end)
    #         else:
    #             # Search lower half
    #             return binary_search(start, mid - 1)

    #     return binary_search(0, len(nums) - 1)

    # USING ITERATION (More optimized.. reduced to about 300 ms)

    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1

        return -1


if __name__ == '__main__':
    nums = [4, 34]
    target = 2

    obj = Solution()
    print(obj.search(nums, target))
