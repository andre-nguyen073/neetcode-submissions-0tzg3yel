class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: 
            print("???")
            return [[]]
        """ 
        keep track of duplicates with set()
        okay so iterate over all the negative numbers
        sort()
        try first negative number, then try the positive -> to far positive you start iterating the left pointer forward to find it 
        -> still negative, then iterate the right pointer backwards to find the right value 
        then try the next positive number and repeat until it finds all the triplets for that specific negative number 
        next iteration iterate the left pointer up 1 and try again.  
        make sure to check every number against the duplicate array 
        

        """
        nums.sort()
        res = []
        prev = None

        for left in range(len(nums)): 
            #this means its the same number again we can skip cause we do not want duplicates or do not want duplicates
            if nums[left] == prev: 
                continue 
            if nums[left] > 0: 
                break

            #check the next value 
            l = left + 1
            r = len(nums) - 1
            #now look over all combinations 
            while l < r: 
                val = nums[left] + nums[l] + nums[r]
                if val < 0: 
                    l += 1 
                elif val > 0: 
                    r -= 1
                else: 
                    res.append([nums[left], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    #skips over duplicates
                    while l < r and nums[l - 1] == nums[l]: 
                        l += 1

            prev = nums[left]
        return res


        

        