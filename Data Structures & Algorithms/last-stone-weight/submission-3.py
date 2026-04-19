class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we need to initalize a maxheap, pop the first two elements off. 
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap) 
            second = -heapq.heappop(max_heap)
            if second < first: 
                heapq.heappush(max_heap, (first - second) * -1) 
        
        if max_heap: 
            return -heapq.heappop(max_heap)
        else: 
            return 0
