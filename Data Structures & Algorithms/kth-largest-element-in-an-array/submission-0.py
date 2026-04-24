class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for i in range(k): 
            if i == k -1: 
                return (heapq.heappop(heap) * -1)
            heapq.heappop(heap)
        
