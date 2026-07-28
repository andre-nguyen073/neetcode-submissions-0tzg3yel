class Solution:
    from collections import Counter
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ 
        bucket sort - founded on the idea that a numbers frequency is only as large as the index + 1 
        """
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        #need an array in each spot cause mutiple items can have the same frequency
        freq = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items(): 
            freq[cnt].append(num)
        
        res = []
        # go to index one since no value can have 0
        for i in range(len(freq) - 1, 0, -1): 
            for num in freq[i]: 
                #appends the arrays onto it 
                res.append(num)
                if len(res) == k: 
                    return res 






        

        




