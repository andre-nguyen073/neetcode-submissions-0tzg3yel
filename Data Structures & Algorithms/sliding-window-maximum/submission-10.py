class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """ 
        first iterate over the first 3 
        push all the values to heap 
        on k value push the highest 
        on next value pop -> if value is not within sliding window 
        pop again repeat

        """
        max_heap = []
        left = 0 
        right = 0 
        result = []
        if k == 1: 
            return nums 
        
        while right < len(nums): 
            if right < k - 1: 
                heapq.heappush(max_heap, (-1 * nums[right], right))
            elif right == k - 1: 
                #highest value is always first
                heapq.heappush(max_heap, (-1 * nums[right], right))
                result.append(max_heap[0][0] * -1)
            else: 
                left += 1 
                heapq.heappush(max_heap, (-1 * nums[right], right))
                highest = max_heap[0]

                while highest[1] < left:
                    heapq.heappop(max_heap)
                    highest = max_heap[0]

                result.append(highest[0] * -1)
            
            right += 1

        return result
        



