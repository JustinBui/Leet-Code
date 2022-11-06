class Solution:
    # Bubble Sort Solution
    # def sortColors(self, nums: list[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     sorted = False
        
    #     while sorted == False:
    #         sorted = True
    #         for i in range(len(nums) - 1):
    #             if nums[i] > nums[i+1]:
    #                 nums[i], nums[i+1] = nums[i+1], nums[i]
    #                 sorted = False
        
    #     return nums

    # Bucket sort solution
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0
        
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
            i += 1

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    entity = Solution()

    entity.sortColors(nums)
    print(nums)