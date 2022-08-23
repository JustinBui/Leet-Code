import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We are multiplying each value in stones in the minheap (Default from Python)
        # to make a max heap... so the least number (Highest negative) is simulated to be 
        # the "highest" weight stone... we will convert this back to positive numbers
        # at the end when returning
        stones = [-st for st in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones) # "heavier stone" represented: highest neg number
            second = heapq.heappop(stones) # "lighter stone" represented: lowest neg nunber
            if first < second: 
                # If the stones are not the same, we do math and push a new value onto our heap
                heapq.heappush(stones, first - second)
                
        return -1 * stones[0] if len(stones) == 1 else 0