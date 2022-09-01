class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counts_list = {}
        
        for h in hand:
            if not counts_list.get(h):
                counts_list[h] = 0
            counts_list[h] += 1
        
        minHeap = list(counts_list.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            smallest = minHeap[0]
            
            for i in range(smallest, smallest + groupSize):
                if i not in counts_list:
                    return False
                counts_list[i] -= 1
                
                if counts_list[i] == 0:
                    if i != minHeap[0]:
                        return False
                    else:
                        heapq.heappop(minHeap)
        return True