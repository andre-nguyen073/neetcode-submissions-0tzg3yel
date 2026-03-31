class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        """ 
        keep track of the beginning of every sequence 
        check the value before it to see if its # - 1 
        larger counter
        if not
            then iterate over the next values 
        if yes 
            ignore
        """

        if not nums: 
            return 0 
        
        hashSet = set(nums)
        for value in nums: 
            hashSet.add(value)
        
        largest_count = 1

        i = 0
        while i < len(nums):
            if nums[i] - 1 in hashSet: 
                i += 1
                continue
            else: 
                count = 1 
                next_val = nums[i] + 1 
                while next_val in hashSet:  
                    count += 1 
                    next_val += 1

                if count > largest_count: 
                    largest_count = count 
            i += 1
        
        return largest_count
                    

            
        

        return longest_sequence


        
        