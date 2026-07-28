class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ 
        naive solution just mutiply every number together and then go back dividing 
        the number at i from it - ignore 0, keep track of 0 with true or false
        """
        if not nums: 
            return []
        res = []
        has_zeros = 0
        total = 1
        for num in nums: 
            if num != 0: 
                total *= num
            else: 
                has_zeros += 1
                if has_zeros == 2: 
                    return [0 for i in range(len(nums))]
        
        for num in nums: 
            if num == 0:
                res.append(total)
            elif has_zeros == 1: 
                res.append(0)
            else: 
                res.append(int(total/num))
        
        return res
