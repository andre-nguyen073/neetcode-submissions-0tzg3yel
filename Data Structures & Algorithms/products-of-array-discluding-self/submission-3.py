class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ 
        naive solution just mutiply every number together and then go back dividing 
        the number at i from it - ignore 0, keep track of 0 with true or false
        valid solution keeps prefix sums of numbers to the left and the right of it
        [1, 2, 8, 48]
        [.         ,6]
        """
        if not nums: 
            return []
        elif len(nums) == 1: 
            return nums 
        
        prefix_sum_left = [1 for i in range(len(nums))]
        prefix_sum_right = [1 for i in range(len(nums))]

        prefix_sum_left[0] = nums[0]
        for i in range(1 , len(nums)): 
            prefix_sum_left[i] = prefix_sum_left[i - 1] * nums[i]
        
        prefix_sum_right[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1): 
            prefix_sum_right[i] = prefix_sum_right[i + 1] * nums[i]

        res = []
        for i in range(len(nums)): 
            if i == 0: 
                res.append(prefix_sum_right[1])
            elif i == len(nums) - 1: 
                res.append(prefix_sum_left[len(nums) - 2])
            else: 
                res.append(prefix_sum_left[i - 1] * prefix_sum_right[i + 1])
        
        return res
        

            


            


        
