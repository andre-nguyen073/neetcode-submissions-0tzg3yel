class Solution:
    from collections import Counter
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ 
        could create a frequency map iterate over it find out the most frequent element 
        - complexity could become larger if there is k = bigger number 
        maybe sort num then iterate over it? 
        """
        if not nums: 
            return []
        frequency_map = Counter(nums)
        max_heap= [(-frequency, value) for value, frequency in list(frequency_map.items())]
        print(max_heap)

        heapq.heapify(max_heap)
        res = []
        print(max_heap)
        for i in range(k): 
            val = heapq.heappop(max_heap)
            res.append(val[1])
        return res

        




