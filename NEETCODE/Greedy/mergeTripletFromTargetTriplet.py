class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # This set contains all of the triplets we will keep that will be used
        # to create target
        good = set()
        
        for tri in triplets:
            if (tri[0] > target[0]) or (tri[1] > target[1]) or (tri[2] > target[2]):
                # We will completely ignore any triplet that has the value at i 
                # to be greater than the value of target at i
                continue
            
            for i, v in enumerate(tri):
                if v == target[i]:
                    good.add(i)
        
        return len(good) == 3