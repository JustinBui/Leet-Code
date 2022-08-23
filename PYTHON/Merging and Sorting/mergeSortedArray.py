
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]

            # Pushing back terms from nums2 to make it go behind
            # the first value greater than it to make it sorted
            curr_it = i
            while (curr_it > 0 and nums1[curr_it] < nums1[curr_it - 1]):
                nums1[curr_it], nums1[curr_it -
                                      1] = nums1[curr_it - 1], nums1[curr_it]
                curr_it -= 1


nums1 = [7, 0, 0]
m = 1
nums2 = [4, 5]
n = 2

test = Solution()
test.merge(nums1, m, nums2, n)

print(nums1)
