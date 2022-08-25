import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        time = 0
        
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        
        queue = []
        
        # If either the maxHeap array or queue are not empty, that means we got more tasks to do.
        # If they are both empty, all tasks are processed and we exit this loop
        while len(maxHeap) > 0 or len(queue) > 0:
            time += 1
            if maxHeap:
                curr = heapq.heappop(maxHeap) + 1
                if curr != 0:
                    queue.append((curr, time + n))
            
            if len(queue) > 0 and queue[0][1] == time:
                cooledDown = queue.pop(0)
                heapq.heappush(maxHeap, cooledDown[0])
                
        return time


if __name__ == '__main__':
    tasks = ["A","A","A","B","B","B"]
    n = 2

    s = Solution()

    print(s.leastInterval(tasks, n))