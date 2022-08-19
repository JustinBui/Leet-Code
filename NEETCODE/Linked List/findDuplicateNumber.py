class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 # Pointers starting at beginning of (Theoretical) linked list
        
        while True:
            slow = nums[slow] # slow traverses once
            fast = nums[nums[fast]] # fast traverses twice
            if slow == fast: # If they point to the same 'node'
                break
        
        slow2 = 0 # slow2 starts at the start of Linked List
        while True:
            slow = nums[slow]  # slow traverses once 
            slow2 = nums[slow2] # slow2 traverses once
            if slow == slow2: # If slow and slow2 point together (aka start of loop of linked list)
                return slow # Return 'node' that is pointed by slow and slow2