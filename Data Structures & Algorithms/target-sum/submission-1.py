class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #this is not backtracking, you make a decision to either positive or negative at every point 
        #thinking you sort the array.   
        """ 
        Target = 0 
        1 -> 1 -> 2 -> 2 -> 2 
        +1 +1 +2 +2 +2 +2 -> obviously would not work 
        """
        #how can we improve complexity what can we cache? 
        cache = {}
        def dfs(total, i): 
            if (i, total) in cache:
                return cache[(i, total)]
            if total == target and i == len(nums): 
                return 1 
            elif total != target and i == len(nums):
                return 0
            
            positive = nums[i]
            negative = nums[i] * -1

            positive_dfs = dfs(total + positive, i + 1) 
            
            negative_dfs = dfs(total + negative, i +1)

            cache[(i,total)] = positive_dfs + negative_dfs

            return cache[(i, total)]
        return dfs(0,0)

        