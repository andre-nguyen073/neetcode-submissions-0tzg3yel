class Solution:
    import heapq
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x,y in points:
            distance = None
            if x == 0: 
                distance = y 
            elif y == 0: 
                distance = x 
            else: 
                distance = math.sqrt((math.pow((x - 0),2) + math.pow((y - 0), 2)))
                
            
            heapq.heappush(max_heap, (-distance, x, y))
            if len(max_heap) > k: 
                heapq.heappop(max_heap)

            
        
        return [[x,y] for distance, x, y in max_heap]


            
            


        