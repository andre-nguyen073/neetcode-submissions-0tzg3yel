class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums: 
            if len(nums) == 1: 
                return nums 
            
            prefix_product = [nums[0]]
            for i in range(1, len(nums)): 
                val = prefix_product[i - 1] * nums[i]
                prefix_product.append(val)
        
            suffix_product = [1] * len(nums)
            suffix_product[len(nums) - 1] = nums[len(nums) - 1]
            for i in range(len(nums) - 2, -1, -1): 
                suffix_product[i] = nums[i] * suffix_product[i + 1] 
            result = []
            for i in range(len(nums)): 
                if i - 1 < 0: 
                    result.append(suffix_product[i + 1])
                elif i + 1 >= len(nums): 
                    result.append(prefix_product[i - 1]) 
                else: 
                    result.append(suffix_product[i + 1] * prefix_product[i - 1])
            return result 
        return []
                    
                    

                

        

                

            