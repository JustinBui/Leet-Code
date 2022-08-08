class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # Midpoint is located in LEFT sorted portion of array.
            # For example: [4, 5, 6, 0, 1, 2] where subarray [4, 5, 6] is the left sorted array
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    # If in the left sorted array, anything on the right of nums[mid] can be
                    # either: greater than nums[mid] or less than the first value of the left sorted array.
                    l = mid + 1
                else:
                    r = mid - 1

            # Mid point is located on RIGHT sorted portion of array
            # In the example: [4, 5, 6, 0, 1, 2], subarray [0, 1, 2] is the right sorted array
            elif nums[l] > nums[mid]:
                if target < nums[mid] or target > nums[r]:
                    # If in the right sorted array, anything to the left of nums[mid] can be
                    # either: less than nums[mid] or greater than the last index of right sorted array.
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
