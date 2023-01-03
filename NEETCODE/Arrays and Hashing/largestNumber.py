class Solution:
    # Solution using Bubble Sort O(n^2)
    def largestNumber(self, nums: list[int]) -> str:
        nums_str = []
        # Converting to strings
        for n in nums:
            nums_str.append(str(n))
        
        if len(nums_str) == 1:
            return nums_str[0]
        
        self.is_sorted = False

        # Bubble sorting
        while self.is_sorted == False:
            self.is_sorted = True
            for i in range(len(nums_str) - 1):
                n1 = nums_str[i]
                n2 = nums_str[i + 1]
                if int(n1 + n2) < int(n2 + n1):
                    nums_str[i], nums_str[i+1] = nums_str[i+1], nums_str[i]
                    self.is_sorted = False
        
        return str(int(''.join(nums_str)))
                
                
        
if __name__ == '__main__':
    nums = [0, 0]

    entity = Solution()
    print(entity.largestNumber(nums))