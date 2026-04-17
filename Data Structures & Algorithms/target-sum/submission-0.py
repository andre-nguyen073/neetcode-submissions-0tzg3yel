class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #this is not backtracking, you make a decision to either positive or negative at every point 
        #thinking you sort the array.   
        """ 
        Target = 0 
        1 -> 1 -> 2 -> 2 -> 2 
        +1 +1 +2 +2 +2 +2 -> obviously would not work 
        """

        def backtracking(total, i): 
            if total == target and i == len(nums): 
                return 1 
            elif total != target and i == len(nums):
                return 0
            
            positive = nums[i]
            negative = nums[i] * -1

            return backtracking(total + positive, i + 1) + backtracking(total + negative, i +1)
        return backtracking(0,0)

        