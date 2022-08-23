import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        
        # FInding distance of each point and adding that onto our containers
        for x, y in points:
            d = sqrt(pow(x, 2) + pow(y, 2))
            distances.append((d, [x,y]))
            
        heapq.heapify(distances)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(distances)[1])
        
        return res
        
        