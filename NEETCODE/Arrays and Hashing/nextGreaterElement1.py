class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # res = []
        # for n1 in nums1:
        #     curr_i = 0
        #     while nums2[curr_i] != n1:
        #         curr_i += 1
            
        #     next_greatest = -1
        #     i = curr_i
        #     while i < len(nums2):
        #         if nums2[i] > nums2[curr_i]:
        #             next_greatest = nums2[i]
        #             break
        #         i += 1
            
        #     res.append(next_greatest)

        # return res

        # Optimal method: O(nums1.length + nums2.length)
        index_tracker = {v:i for i,v in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            current = nums2[i]
            while len(stack) > 0 and stack[-1] < current:
                key = stack.pop()
                idx = index_tracker[key]
                res[idx] = current
                
            
            if index_tracker.get(current) != None: # Implies that if nums2[i] is found in nums1
                stack.append(current) # Push onto stack
        
        return res