class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        least = nums[0]

        # Edge case for sorted arrays (With no rotations) or arrays only containing 1 element
        if nums[l] <= nums[r]:
            return nums[l]

        # Now assuming that we have an array that does have rotations
        while l <= r:
            if nums[l] < nums[r]:
                # This means we've found the pivot
                least = min(least, nums[l])
                break

            mid = (l + r) // 2
            least = min(least, nums[mid])

            # nums[mid] is located at left sorted subarray
            # (Our goal is to shift our left and right windows toward where there is likely to be a pivot of the rotation)
            if nums[mid] >= nums[l]:
                l = mid + 1

            # nums[mid] is located at right of sorted subarray
            else:  # nums[mid] < nums[l]
                r = mid - 1

        return least


if __name__ == '__main__':
    obj = Solution()

    obj.findMin()
