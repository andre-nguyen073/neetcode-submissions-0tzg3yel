class Solution:
    import heapq
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)
        
        res = []
        for x,y in points:
            distance = None
            if x == 0: 
                distance = y 
            elif y == 0: 
                distance = x 
            else: 
                distance = math.sqrt((math.pow((x - 0),2) + math.pow((y - 0), 2)))
            
            heapq.heappush(min_heap, (distance, x, y))
        
        for i in range(k): 
            distance, x, y = heapq.heappop(min_heap)
            res.append([x,y])
        
        return res


            
            


        