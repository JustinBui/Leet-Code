# Solution: https://www.youtube.com/watch?v=73r3KWiEvyk

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        rob1, rob2 = 0, 0
        
        for n in nums:
            # rob2 is the house previous from current house
            # rob1 is the house we robbed before rob2
            # array representation = [rob1, rob2, n, n + 1, ...]
            
            temp = max(n + rob1, rob2)  # If we choose n + rob1, that means we will choose to rob the current
                                        # house n and other previous houses not contiguous.
                                        # If we choose rob2, that means we will NOT rob the current house n,
                                        # but we will stick to the very previous house and other of it's
                                        # contiguous houses.
            
            # Advancing iterators
            rob1 = rob2
            rob2 = temp
        
        return rob2 # rob2 will always be updated with the current largest value as we iterate along