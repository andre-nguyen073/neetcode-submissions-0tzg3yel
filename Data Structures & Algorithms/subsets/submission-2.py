class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ 
        [1, 2, 3]
        [1], [1, 2], [2], [1, 2, 3], [2,3] [1,3] [3]
        #how do we get 2 -> 3 
        """
        if len(nums) == 0: 
            return []
        subset = [[]]
        def find_subset(current, i): 
            if i == len(nums):
                return 
            
            subset.append(current)
            for y in range(i + 1, len(nums)): 
                find_subset(current + [nums[y]], y)
            
        for i in range(len(nums)):
            find_subset([nums[i]], i)

        return subset

        