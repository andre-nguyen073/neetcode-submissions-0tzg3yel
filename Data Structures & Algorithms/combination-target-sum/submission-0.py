class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final = []
        if not nums: 
            return []
        def back_tracking(val, curr, index):
            if val == 0: 
                final.append(curr)
            
            #do not run anymore 
            if val < 0: 
                return 
            
            for i in range(index, len(nums)):
                returned_array = back_tracking(val - nums[i], curr + [nums[i]], i)
                if returned_array: 
                    final.append(returned_array)
        
        back_tracking(target, [], 0) 
        return final


        

        
        