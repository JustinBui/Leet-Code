# SOURCE: https://www.youtube.com/watch?v=cVZMah9kEjI

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if (len(nums) == 1):    # BASE CASE
            return nums

        else:   # RECURSIVE CASE
            # Using divide and conquer
            mid = (len(nums) - 1) // 2
            left = self.sortArray(nums[:mid + 1])
            right = self.sortArray(nums[mid + 1:])

            # i is index of left subarray
            # j is index of right subarray
            i = j = 0
            newArr = []

            # Merging left and right subarrays
            while (i < len(left) and j < len(right)):
                if (left[i] < right[j]):
                    newArr.append(left[i])
                    i += 1
                else:  # if (right[j] <= left[i]):
                    newArr.append(right[j])
                    j += 1

            # Filling in the remaining numbers either from left or right
            while (i < len(left)):
                newArr.append(left[i])
                i += 1
            while (j < len(right)):
                newArr.append(right[j])
                j += 1

            return newArr


if (__name__ == "__main__"):
    mySol = Solution()

    arr = [49, 54, 23, 2, 2, 2, 45, 0, -33, -2]
    result = mySol.sortArray(arr)

    print(result)
