class KthLargest:
    import heapq
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.stream = nums
        # Turn the input list into a heap in-place
        heapq.heapify(self.stream)
        
        # Shrink the heap until only k elements remain
        while len(self.stream) > k:
            heapq.heappop(self.stream)

    def add(self, val: int) -> int:
        # 1. Add the new value
        heapq.heappush(self.stream, val)
        
        # 2. If we have k+1 elements, remove the smallest one
        if len(self.stream) > self.k:
            heapq.heappop(self.stream)
        
        # 3. The top of the min-heap is always the kth largest
        return self.stream[0]

        
