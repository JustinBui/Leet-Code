class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cutoff = len(nums) - 1
        zeroes_moved = False

        while zeroes_moved == False:
            zeroes_moved = True

            for i in range(cutoff):
                if nums[i] == 0:
                    zeroes_moved = False
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    if cutoff == i + 1:  # If we've swapped 0's past the cutoff
                        cutoff -= 1


if __name__ == '__main__':
    s = Solution()

    nums = [1 for i in range(1, 50)] + [0, 0]
    print(f'Before: {nums}')
    s.moveZeroes(nums)

    print(f'After: {nums}')
